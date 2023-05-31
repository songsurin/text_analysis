from chatbot.Preprocess import Preprocess
from chatbot.IntentModel import IntentModel
p = Preprocess(word2index_dic='../../data/chatbot_dict.bin', userdic=None)
intent = IntentModel(model_name='../model/intent_model.h5', preprocess=p)

query = "렌트카 예약하고 싶어요 제주도 놀러가는데"
predict = intent.predict_class(query)
predict_label = intent.labels[predict]
print(query)
print("의도 예측 클래스: ", predict)
print("의도 예측 레이블: ", predict_label)
print("=" * 30)