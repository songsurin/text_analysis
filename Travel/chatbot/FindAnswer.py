import random

class FindAnswer:
    def __init__(self, db):
        self.db = db

    # 검색 쿼리 생성
    def _make_query(self, intent_name, ner_tags):
        sql = 'select * from chatbot_train_data'
        if intent_name != None and ner_tags == None:
            sql = sql + " where intent = '{}' ".format(intent_name)
            sql += " and (ner is null) "
        elif intent_name != None and ner_tags != None:
            where = ' where intent="%s" ' % intent_name
            if (len(ner_tags) > 1):
                where += 'and ('
                for ne in ner_tags:
                    where += " ner like '%{}%' and ".format(ne)
                where = where[:-4] + ')'
            elif (len(ner_tags) == 1):
                where += "and (ner='%s')" % ner_tags[0]
            # 동일한 답변이 2개 이상일 경우, 랜덤으로 선택
            sql += where + " order by rand() limit 1"
        return sql

    # 답변 검색
    def search(self, intent_name, ner_tags):
        # 의도명, 개체명으로 답변 검색
        sql = self._make_query(intent_name, ner_tags)
        answer = self.db.select_one(sql)
        # 검색되는 답변이 없으면 의도명만 검색
        if answer is None:
            sql = self._make_query(intent_name, None)
            answer = self.db.select_one(sql)
        return answer['answer']

    # NER 태그를 실제 입력된 단어로 변환
    def tag_to_word(self, ner_predicts, answer):
        for word, tag in ner_predicts:
            # 변환해야 하는 태그가 있는 경우 추가
            if tag == 'B_R' or tag == 'B_DT' or tag == 'B_C' or tag == 'B_A' or tag == 'B_T':
                answer = answer.replace(tag, word)
        answer = answer.replace('{', '')
        answer = answer.replace('}', '')
        return answer

    def answersearch(self, item):
        region = item[0]
        attraction = item[1]
        companion = item[3]
        reg_key, att_key = None, None
        if len(companion) != 0:
            if '아이' in companion:
                att_key = '아이와함께'
        if len(region) != 0:
            if '여행지' in region:
                att_key = '여행지'
            reg_key = ['시도명', '시군구명', '읍면동명']
        if len(attraction) != 0:
            if '맛집' in attraction:
                att_key = '맛집'
        else:
            att_key = '여행지'

        sql = f"select 어트랙션_목록 from total_attraction"
        if reg_key != None:
            for reg in region:
                sql += f" where (시도명 like '{reg}%' or 시군구명 like '{reg}%' or 읍면동명 like '{reg}%')"
            if att_key != None:
                sql += f" and 어트랙션='{att_key}'"
        elif (reg_key == None) & (att_key != None):
            sql += f" where 어트랙션='{att_key}'"
        lst = []
        ans = self.db.select_all(sql)
        for select in ans:
            lst.append(list(select.values())[0])
        if len(lst) != 0:
            sh = str(lst).replace("[", '').replace(']', '').replace("'", '').replace(" ", '').split(',')
            result = random.sample(sh, 5)
            return (', ').join(result) + ' 등'
        return None