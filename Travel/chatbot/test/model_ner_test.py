from chatbot.Preprocess import Preprocess
from chatbot.NerModel import NerModel
p = Preprocess(word2index_dic='../../data/chatbot_dict.bin',
               userdic='../../data/user_dic.tsv')
ner = NerModel(model_name='../model/ner_model.h5',
               preprocess=p)
querys = ['1박2일로 놀러가려고 하는데 여행지 추천 좀 해주세요.', '주말에 친구들이랑 놀러가려고 하는데 추천해 주세요.', '부모님 결혼기념일에 여행보내드리려고 합니다. 좋은 곳 없을까요?']
for query in querys:
    predicts = ner.predict(query)
    tags = ner.predict_tags(query)
    print(predicts)
    print(tags)