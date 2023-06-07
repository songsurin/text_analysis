# 의도 분류 모델 테스트

from chatbot.Preprocess import Preprocess
from chatbot.IntentModel import IntentModel
p = Preprocess(word2index_dic='../../data/chatbot_dict.bin', userdic=None)
intent = IntentModel(model_name='../model/intent_model.h5', preprocess=p)

querys = ["호텔 예약 해주세요", "1박2일로 놀러갈만한 장소 좀 알려주세요.", "혼자 머리 식힐만한 곳이 있을까요?"]

for query in querys:
    predict = intent.predict_class(query)
    predict_label = intent.labels[predict]
    print(query)
    print("의도 예측 클래스: ", predict)
    print("의도 예측 레이블: ", predict_label)
    print("=" * 30)