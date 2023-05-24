# 챗봇에 사용하는 사전 파일

from chatbot.Preprocess import Preprocess
from tensorflow.keras import preprocessing
import pickle
import pandas as pd

# 말뭉치 데이터 읽어오기
purpose = pd.read_csv("../data/수정데이터/용도별 목적대화 데이터.csv")
topic = pd.read_csv("../data/수정데이터/주제별 텍스트 일상 대화 데이터.csv")
sense = pd.read_csv("../data/수정데이터/일반상식 데이터.csv")
travelinfo = pd.read_csv("../data/수정데이터/여행정보 데이터.csv")
recommend = pd.read_csv("../data/수정데이터/여행지추천 데이터.csv")

purpose.dropna(inplace=True)
topic.dropna(inplace=True)
sense.dropna(inplace=True)
travelinfo.dropna(inplace=True)
recommend.dropna(inplace=True)

text1 = list(purpose["text"])
text2 = list(topic["text"])
text3 = list(sense["question"]) + list(sense["answer"])
text4 = list(travelinfo["city"]) + list(travelinfo['sigungu']) + list(travelinfo["title"])
text5 = list(recommend["question"]) + list(recommend["answer"])

corpus_data = text1 + text2 + text3 + text4 + text5

# 말뭉치 데이터에서 키워드만 추출해서 사전 리스트 생성
p = Preprocess()
dict = []
for c in corpus_data:
    pos = p.pos(c)
    for k in pos:
        dict.append(k[0])

# 사전에 사용될 word2index 생성(사전의 첫 번째 인덱스에는 OOV 사용)
tokenizer = preprocessing.text.Tokenizer(oov_token="OOV", num_words=100000)
tokenizer.fit_on_texts(dict)
word_index = tokenizer.word_index
print(len(word_index))

# 사전 파일 생성
f = open("../data/chatbot_dict.bin", "wb")
try:
    pickle.dump(word_index, f)
except Exception as e:
    print(e)
finally:
    f.close()
print("완료되었습니다.")
