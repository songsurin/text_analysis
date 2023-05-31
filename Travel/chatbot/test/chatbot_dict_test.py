# 단어사전 테스트

import pickle
from chatbot.Preprocess import Preprocess

# 단어 사전 불러오기
f = open("../../data/chatbot_dict.bin", "rb")
word_index = pickle.load(f)
f.close()

sent = "테스트입니다. 단어사전 확인 중. 제대로 작동하면 성공. 예약 시스템을 만들 기초가 됩니다. 홍대에 놀러가려 하는데 놀거리 추천 좀~"

# 전처리 객체 생성
p = Preprocess(word2index_dic="../../data/chatbot_dict.bin", userdic="../../data/user_dic.tsv")

# 형태소분석기 실행
pos = p.pos(sent)

# 품사 태그 없이 키워드 출력
keywords = p.get_keywords(pos, without_tag=True)

for word in keywords:
    try:
        print(word, word_index[word])
    except KeyError:
        # 해당 단어가 사전에 없는 경우 OOV 처리
        print(word, word_index['OOV'])