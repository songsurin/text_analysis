# 텍스트 전처리 테스트

from chatbot.Preprocess import Preprocess

sentence = "여행지 추천해 주세요~~!"

# 전처리 객체 생성
p = Preprocess()

# 형태소 분석기 실행
pos = p.pos(sentence)

# 품사 태그와 같이 키워드 출력
keywords = p.get_keywords(pos, without_tag=False)
print(keywords)

# 품사 태그 없이 키워드 출력
keywords = p.get_keywords(pos, without_tag=True)
print(keywords)