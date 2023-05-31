from chatbot.db.DatabaseConfig import *
from chatbot.db.Database import Database
from chatbot.Preprocess import Preprocess
from chatbot.IntentModel import IntentModel
from chatbot.NerModel import NerModel
from chatbot.FindAnswer import FindAnswer
# 전처리 객체 생성
p = Preprocess(word2index_dic='../../data/chatbot_dict.bin',
               userdic='../../data/user_dic.tsv')
# 질문/답변 학습 디비 연결 객체 생성
db = Database(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    db_name=DB_NAME
)
db.connect() # 디비 연결
queries = ['부모님과 놀러갈만한 데 어디 없을까요','안녕하세요','새끼']

# 의도 파악 모델
intent = IntentModel(model_name='../model/intent_model.h5',
                     preprocess=p)

# 개체명 인식 모델
ner = NerModel(model_name='../model/ner_model.h5',
               preprocess=p)

# 의도 파악
for query in queries:
    predict = intent.predict_class(query)
    intent_name = intent.labels[predict]
    predicts = ner.predict(query)
    ner_tags = ner.predict_tags(query)
    print("질문 : ", query)
    print("=" * 100)
    print("의도 파악 : ", intent_name)
    print("개체명 인식 : ", predicts)
    print("답변 검색에 필요한 NER 태그 : ", ner_tags)
    print("=" * 100)
    # 답변 검색
    try:
        f = FindAnswer(db)
        answer_text = f.search(intent_name, ner_tags)
        answer = f.tag_to_word(predicts, answer_text)
    except:
        answer = "죄송해요 무슨 말인지 모르겠어요"
        print("답변: ", answer)
        db.close() # 디비 연결 끊음