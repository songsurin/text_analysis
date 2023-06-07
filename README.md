# 여행지 추천 Chatbot
## 데이터 출처
- AI Hub: 주제별 텍스트 일상 대화 데이터, 일반 상식, 용도별 목적대화 데이터, 여행 정보 데이터셋
- 네이버 지식인: 여행지 추천 질문 & 답변
- 네이버 여행정보: 국내 여행지 정보

## 사용한 언어 및 라이브러리, 프레임워크
- Python: konlpy, jpype, pickle, tensorflow, pandas, os, glob, re, json, time, selenium, numpy, seqeval, matplotlib, sklearn, pymysql, logging, random, threading, socket, MySQLdb, itertools, ast
- HTML, JS
- MySQL
- Django

## 순서
#### 1. 텍스트 전처리기 생성
  - Travel/chatbot/Preprocess.py

#### 2. 데이터 전처리
  - 서로 다른 형식의 원본 데이터를 필요한 데이터만 추출, 결측값 처리 후 csv로 통일화
    - Travel/chatbot/Data_To_Csv.ipynb
  - 단어사전 생성
    - Travel/chatbot/Create_dict.py
  - 사용자 사전 생성
    - Travel/data/user_dic.tsv
  - 의도 분류 모델 생성을 위한 학습용 데이터 생성
    - Travel/chatbot/Create_train_data.ipynb
  - 명사들만 추출 후 BIO태깅
    - Travel/chatbot/texts_to_nouns.ipynb
    - 엑셀 작업
  - 개체명 인식 모델 생성을 위한 학습용 데이터 생성
    - Travel/chatbot/labeling.ipynb

#### 3. 단어 시퀀스 벡터 크기 설정
  - Travel/chatbot/GlobalParams.py

#### 4. 의도 분류 모델 생성
  - Travel/chatbot/Train_model.py
  - Travel/chatbot/IntentModel.py

#### 5. 개체명 인식 모델 생성
  - Travel/chatbot/Train_ner_model.py
  - Travel/chatbot/NerModel.py

#### 6. 예상 질답 DB생성
  - Travel/chatbot/db/Database.py
  - Travel/chatbot/db/DatabaseConfig.py
  - Travel/chatbot_train_data_create.sql

#### 7. 답변 검색 모듈 생성
  - Travel/chatbot/FindAnswer.py

#### 8. 소켓 모듈 생성
  - Travel/chatbot/server/BotServer.py
  - Travel/chatbot/server/bot.py

#### 9. 웹 구현
  - Travel/travel

#### 10. 상세답변 DB생성
  - Travel/chatbot/Detail_Ans_DB.ipynb

#### 11. DB에 없는 답변 크롤링
  - Travel/chatbot/AnswerModel.py
  - Travel/chatbot/Crawling_Answer.ipynb

#### 12. Chatbot에 연결

## 개선사항
- BIO태깅 보완
- 답변DB 보완
- 예약 시스템 구축
- 예상 질문 추가 및 세분화

---

맞춤법 검사기
https://github.com/ssut/py-hanspell

참고용 글
https://ebbnflow.tistory.com/246

- *맞춤법 검사기 돌릴때 haspell파일과 코드를 같은 폴더에 넣어서 하세요.*
- *C드라이브에 받아서 사용하세요. 만약 다른 경로로 받으신다면 Travle/travle/mychatbot.py 안에 사전과 모델의 절대경로를 수정해서 사용하세요.*
- *사용된 모델과 데이터 링크: https://drive.google.com/drive/folders/1F8M1SzRHX6DfyY3j6fUac4DDs1O51H53*
