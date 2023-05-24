import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
from chatbot.Preprocess import Preprocess
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional
from tensorflow.keras.optimizers import Adam

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)

# 학습용 데이터 로드
nur = pd.read_csv('../data/수정데이터/명사들.csv', encoding='cp949', index_col=0)
nur.dropna(inplace=True)

p = Preprocess(word2index_dic='../data/chatbot_dict.bin',
               userdic=None)

# 말뭉치 데이터에서 단어와 BIO태그만 불러와 학습용 데이터셋 생성
words, tags = nur['nouns'], nur['label']
# tagged_words = list(zip(nur['nouns'], nur['label']))

print('샘플 개수:\n', len(words))
print('0번 째 샘플 단어 시퀀스:\n', words[0])
print('0번 째 샘플 bio 태그:\n', tags[0])
print('샘플 단어 시퀀스 최대 길이:\n', max(len(l) for l in words))
print('샘플 단어 시퀀스 평균 길이:\n', (sum(map(len, words)) / len(words)))

# 토크나이저 정의
tag_tokenizer = preprocessing.text.Tokenizer(lower=False)
tag_tokenizer.fit_on_texts(tags)

# 단어사전 및 태그 사전 크기
vocab_size = len(p.word_index) + 1
tag_size = len(tag_tokenizer.word_index) + 1
print('BIO 태그 사전 크기:', tag_size)
print('단어 사전 크기:', vocab_size)

# 학습용 단어 시퀀스 생성
x_train = [p.get_wordidx_sequence(word) for word in words]
y_train = tag_tokenizer.texts_to_sequences(tags)
index_to_ner = tag_tokenizer.index_word # 시퀀스 인덱스를 NER로 변환 하기 위해 사용
index_to_ner[0] = 'PAD'

# 시퀀스 패딩 처리
max_len = 40
x_train = preprocessing.sequence.pad_sequences(x_train, padding='post', maxlen=max_len)
y_train = preprocessing.sequence.pad_sequences(y_train, padding='post', maxlen=max_len)

# 학습 데이터와 테스트 데이터 분리
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=.2, random_state=10)

# 출력 데이터를 원핫인코딩
y_train = tf.keras.utils.to_categorical(y_train, num_classes=tag_size)
y_test = tf.keras.utils.to_categorical(y_test, num_classes=tag_size)

print('학습 샘플 시퀀스 형상:', x_train.shape)
print('학습 샘플 레이블 형상:', y_train.shape)
print('테스트 샘플 시퀀스 형상:', x_test.shape)
print('테스트 샘플 레이블 형상:', y_test.shape)

# 모델 정의 (Bi-LSTM)
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=30, input_length=max_len, mask_zero=True))
model.add(Bidirectional(LSTM(200, return_sequences=True, dropout=0.50, recurrent_dropout=0.25)))
model.add(TimeDistributed(Dense(tag_size, activation='softmax')))
model.compile(loss='categorical_crossentropy', optimizer=Adam(0.01), metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=128, epochs=10)
model.save('./model/ner_model.h5')

# 모델 평가
from tensorflow import keras
model = keras.models.load_model('./model/ner_model.h5')
print('평가 결과:', model.evaluate(x_test, y_test)[1])

# 시퀀스를 NER 태그로 변환하는 함수
def sequences_to_tag(sequences):
    result = []
    for sequence in sequences:
        temp = []
        for pred in sequence:
            pred_index = np.argmax(pred)
            temp.append(index_to_ner[pred_index].replace('PAD', '0'))
        result.append(temp)
    return result

# f1 스코어
from seqeval.metrics import f1_score, classification_report
y_predicted = model.predict(x_test) # 테스트 데이터셋의 NER 예측
pred_tags = sequences_to_tag(y_predicted) # 예측된 NER
test_tags = sequences_to_tag(y_test) # 실제 NER
print(classification_report(test_tags, pred_tags))
print('F1-score: {:.1%}'.format(f1_score(test_tags, pred_tags)))