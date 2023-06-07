from chatbot.Preprocess import Preprocess
from chatbot.IntentModel import IntentModel
from chatbot.NerModel import NerModel
from chatbot.AnswerModel import AnswerModel

question = '노원구 놀만한데 추천좀 해주세요.'

# 전처리 객체 생성
p = Preprocess(word2index_dic='../../data/chatbot_dict.bin',
               userdic='../../data/user_dic.tsv')

# 의도 파악 모델
intent = IntentModel(model_name='../model/intent_model.h5',
                     preprocess=p)

# 개체명 인식 모델
ner = NerModel(model_name='../model/ner_model.h5',
               preprocess=p)

predict = intent.predict_class(question)
intent_name = intent.labels[predict]
predicts = ner.predict(question)
ner_tags = ner.predict_tags(question)
print("질문:", question)
print("=" * 100)
print("의도 파악:", intent_name)
print("개체명 인식:", predicts)
print("답변 검색에 필요한 NER 태그:", ner_tags)
print("=" * 100)

# 답변 크롤링 모델
Ans = AnswerModel(predicts)
items = Ans.refine(predicts)
query = Ans.create_query(items)
answer = Ans.search(query, items)
print("답변:", answer)