![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=%20국내%20여행지%20추천%20Chatbot&fontSize=50)

### 수행기간 : 2023.05.18 ~ 2023.06.08

## 주제
코로나 종식 선언 이후, 국내 여행을 계획 중인 사람들을 위한 여행지 추천 챗봇 생성 프로젝트

## 팀원
<ul>
  <li><a href="https://github.com/SpearXirus">김창균</a></li>
  <li><a href="https://github.com/songsurin">송수린</a></li>
  <li><a href="https://github.com/cesong2">송찬의</a></li>
  <li><a href="https://github.com/HyunJW">현정환</a></li>
</ul>

## 데이터 출처
<ul>
  <li><a href="https://www.aihub.or.kr/">AI Hub</a> : 주제별 텍스트 일상 대화 데이터, 일반 상식, 용도별 목적대화 데이터, 여행 정보 데이터셋</li>
  <li>네이버 지식인 : 여행지 추천 질문 & 답변</li>
  <li><a href="https://travel.naver.com/domestic">네이버 여행정보</a> : 국내 여행지 정보</li>
</ul>

## 사용한 언어 및 라이브러리, 프레임워크
#### 언어
<div align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/HTML-239120?&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS-239120?&logo=css3&logoColor=white"/>
  <img src="https://img.shields.io/badge/Javascript-F7DF1E?&logo=javascript&logoColor=black"/>
</div>

#### 라이브러리
<div align="left">
  <img src="https://img.shields.io/badge/Pandas-2C2D72?style=flat-square&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Numpy-777BB4?style=flat-square&logo=numpy&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat-square&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=flat-square&logo=TensorFlow&logoColor=white"/>
  <img src="https://img.shields.io/badge/-selenium-%43B02A?style=flat-square&logo=selenium&logoColor=white"/>
</div>
<div align="left">
  <img src="https://img.shields.io/badge/KoNLPy-003366?style=flat-squar&logo=KoNLPy&logoColor=white"/>
  <img src="https://img.shields.io/badge/JPype-9999ff?style=flat-squar&logo=JPype"/>
  <img src="https://img.shields.io/badge/Socket-0066ff?style=flat-squar&logo=Socket"/>
  <img src="https://img.shields.io/badge/Matplotlib-F2F2F2?style=flat-square&logo=Matplotlib&logoColor=black"/>
  <img src="https://img.shields.io/badge/PyMySQL-ff00ff?style=flat-squar&logo=PyMySQL"/>
</div>

#### DBMS
<div align="left">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white"/>
</div>
  
#### 프레임워크
<div align="left">
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-092E20?&logo=django&logoColor=white"/>
</div>  

#### 툴
<div align="left">
  <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white"/>
  <img src="https://img.shields.io/badge/pycharm-143?style=flat-square&logo=pycharm&logoColor=black&color=black&labelColor=green"/>
</div>

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
  <br/><img src="https://github.com/songsurin/text_analysis/assets/121409507/26434c0f-69e9-4410-bc9e-4cc76cb08772" width=70%/>

#### 5. 개체명 인식 모델 생성
  - Travel/chatbot/Train_ner_model.py
  - Travel/chatbot/NerModel.py
  <br/><img src="https://github.com/songsurin/text_analysis/assets/121409507/8e104b2a-d1d5-466c-b43c-1bb49cd0f220" width=70%/>

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

## 결과
| 화면 예시 |
| --- |
| <img src="https://github.com/songsurin/text_analysis/assets/121409579/ab446c8f-98db-48ef-9208-87efe8300748" width=70%/> | 
| <img src="https://github.com/songsurin/text_analysis/assets/121409579/45170293-7d9a-45aa-9405-87293d90f784"/> |

## 개선사항
- BIO태깅 보완
- 답변DB 보완
- 예약 시스템 구축
- 예상 질문 추가 및 세분화

## 비고
- <a href="https://github.com/ssut/py-hanspell">맞춤법 검사기</a> - *맞춤법 검사기 돌릴때 haspell파일과 코드를 같은 폴더에 넣어서 하세요.*
- <a href="https://ebbnflow.tistory.com/246">참고용 글</a>
- <a href="https://drive.google.com/drive/folders/1F8M1SzRHX6DfyY3j6fUac4DDs1O51H53">사용된 모델과 데이터 링크</a>
- *C드라이브에 받아서 사용하세요. 만약 다른 경로로 받으신다면 Travle/travle/mychatbot.py 안에 사전과 모델의 절대경로를 수정해서 사용하세요. 하드코딩 죄송합니다...*
