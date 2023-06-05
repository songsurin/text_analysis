from chatbot.db.DatabaseConfig import *
from chatbot.db.Database import Database
from chatbot.Preprocess import Preprocess
from chatbot.IntentModel import IntentModel
from chatbot.NerModel import NerModel
from chatbot.FindAnswer import FindAnswer
from chatbot.AnswerModel import AnswerModel

# 전처리 객체 생성
p = Preprocess(word2index_dic='C:/Users/tjoeun/Desktop/surin/text_analysis/Travel/data/chatbot_dict.bin', userdic='C:/Users/tjoeun/Desktop/surin/text_analysis/Travel/data/user_dic.tsv')

# 의도 파악 모델
intent = IntentModel(model_name='C:/Users/tjoeun/Desktop/surin/text_analysis/Travel/chatbot/model/intent_model.h5', preprocess=p)

# 개체명 인식 모델
ner = NerModel(model_name='C:/Users/tjoeun/Desktop/surin/text_analysis/Travel/chatbot/model/ner_model.h5', preprocess=p)


def getMessage(query):
    try:
        db = Database(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME
        )
        db.connect()

        # 의도 파악
        intent_predict = intent.predict_class(query)
        intent_name = intent.labels[intent_predict]
        # 개체명 파악
        ner_predicts = ner.predict(query)
        ner_tags = ner.predict_tags(query)
        # 답변 검색 모델
        ans = AnswerModel(ner_predicts)
        item = ans.refine(ner_predicts)
        Q = ans.create_query(item)
        A = ans.search(Q)
        # 답변 검색
        try:
            f = FindAnswer(db)
            answer_text = f.search(intent_name, ner_tags)
            answer = f.tag_to_word(ner_predicts, answer_text)
            if intent_name != '기타':
                answer = answer + ' ' + A
        except:
            answer = "죄송합니다. 질문 내용을 이해하지 못했습니다."
        json = {
            "in": ans,
            "Query": query,
            "Answer": answer,
            "Intent": intent_name,
            "NER": str(ner_predicts),
            "Item": item,
            "q": Q
        }
        return json
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    msg = getMessage('')
    print(msg)