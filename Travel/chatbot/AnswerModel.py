from itertools import product
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AnswerModel:
    def __init__(self, predicts):
        self.predicts = predicts

    # 검색 질문을 생성하기 위한 개체명 정제
    def refine(self, predicts):
        region, attraction, datetime, companion, purpose = [], [], [], [], []
        for i in range(len(predicts)):
            if predicts[i][1] in 'B_R':
                if (predicts[i][0] != '여행지') & (predicts[i][0] != '장소') & (predicts[i][0] != '곳'):
                    region.append(predicts[i][0])
            elif predicts[i][1] in 'B_A':
                attraction.append(predicts[i][0])
            elif predicts[i][1] in 'B_DT':
                datetime.append(predicts[i][0])
            elif predicts[i][1] in 'B_C':
                companion.append(predicts[i][0])
            elif predicts[i][1] in 'B_P':
                purpose.append(predicts[i][0])
            elif predicts[i][1] in 'O':
                if predicts[i][0] in ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월', '1박2일']:
                    datetime.append(predicts[i][0])
        item = [region, attraction, datetime, companion, purpose]
        return item

    # 검색 질문 생성
    def create_query(self, item):
        keywords = [i for i in item if len(i) != 0]
        keywords = list(product(*keywords))
        queries = []
        for keyword in keywords:
            query = ''
            for i in range(len(keyword)):
                query = f'{query} {keyword[i]}'
            if '맛집' in query:
                query += ' 추천'
            else:
                query += ' 여행지 추천'
            queries.append(query.strip())
        return queries

    def research(self, queries, item):
        region, attraction, datetime, companion, purpose = item
        datetimes = ['요즘', '봄', '여름', '가을', '겨울', '1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월',
                     '12월']
        if (len(purpose) == 0) and (len(companion) == 0) and (len(datetime) == 0):
            answer = '아직 학습되지 않은 부분입니다. 죄송합니다.'
            return answer

        temma_idx = -1
        if len(purpose) != 0:
            if purpose[0] in ['신혼', '신혼여행']:
                temma_idx = 2

        if len(companion) != 0:
            if companion[0] == '혼자':
                temma_idx = 0
            elif companion[0] in ['자녀', '아들', '딸', '애기', '아기', '아이']:
                temma_idx = 1
            elif companion[0] in ['부모', '할아버지', '할머니', '조부모', '아버지', '어머니', '아빠', '엄마']:
                temma_idx = 3
            elif companion[0] in ['친구', '여자친구', '남자친구']:
                temma_idx = 4

        loc_idx = 0
        if len(region) != 0:
            if region[0] in ['서울', '인천', '경기']:
                loc_idx = 1
            elif region[0] in ['경북', '경남', '경상북도', '경상남도']:
                loc_idx = 2
            elif region[0] in ['전북', '전남', '전라북도', '전라남도']:
                loc_idx = 3
            elif region[0] in ['강원', '강원도']:
                loc_idx = 4
            elif region[0] in ['충북', '충남', '충청북도', '충청남도']:
                loc_idx = 5
            elif region[0] in ['제주', '제주도']:
                loc_idx = 6

        # 옵션 생성
        options = webdriver.ChromeOptions()
        # 창 숨기는 옵션 추가
        options.add_argument("headless")

        url = 'https://travel.naver.com/domestic'
        driver = webdriver.Chrome(options=options)
        for query in queries:
            driver.get(url)

            if len(datetime) != 0:
                for dt in datetime:
                    if dt in datetimes:
                        dt_idx = datetimes.index(dt)
                        driver.find_element(By.CLASS_NAME, 'filter_button__2KgQ_').click()
                        time.sleep(0.5)
                        driver.find_elements(By.CLASS_NAME, 'filter_button__2KgQ_')[dt_idx + 1].click()
                        time.sleep(0.5)
                        driver.find_elements(By.CLASS_NAME, 'filter_button__2KgQ_')[2].click()
                        time.sleep(0.5)
                        driver.find_elements(By.CLASS_NAME, 'filter_button__2KgQ_')[loc_idx + 2].click()
                time.sleep(2)

            elif temma_idx >= 0:
                driver.find_elements(By.CLASS_NAME, 'filter_tab__2U5Lx')[1].click()
                driver.find_element(By.CLASS_NAME, 'filter_button__2KgQ_').click()
                time.sleep(0.5)
                driver.find_elements(By.CLASS_NAME, 'filter_button__2KgQ_')[temma_idx + 1].click()
                time.sleep(0.5)
                driver.find_elements(By.CLASS_NAME, 'filter_button__2KgQ_')[1].click()
                time.sleep(0.5)
                driver.find_elements(By.CLASS_NAME, 'filter_button__2KgQ_')[loc_idx + 2].click()
                time.sleep(2)

            des_list = driver.find_elements(By.CLASS_NAME, 'item_name__2TMMW')[0:5]
            top5 = des_list[0:5]
            try:
                if '맛집' in query:
                    loc = query.split(' ')[0]
                    answer = f'{loc} 추천 맛집으로는 '
                else:
                    answer = '추천하는 여행지로는 '
                for i in range(len(top5)):
                    answer += top5[i].text
                    if i == len(top5) - 1:
                        answer += ' '
                    else:
                        answer += ', '
                answer += '등이 있습니다.'
            except:
                answer = '아직 학습되지 않은 부분입니다. 죄송합니다.'
        driver.close()
        return answer

    # 네이버 크롤링
    def search(self, queries):
        # 옵션 생성
        options = webdriver.ChromeOptions()
        # 창 숨기는 옵션 추가
        options.add_argument("headless")

        url = 'https://www.naver.com/'
        driver = webdriver.Chrome(options=options)
        for query in queries:
            driver.get(url)
            driver.find_element(By.CLASS_NAME, 'search_input').send_keys(query)
            driver.find_element(By.CLASS_NAME, 'btn_search').click()
            des_list = driver.find_elements(By.CLASS_NAME, 'keyword-UDtbe')
            top5 = des_list[0:5]

            if len(top5) == 0:
                res_list = driver.find_elements(By.CLASS_NAME, 'place_bluelink')
                top5 = res_list[0:5]
                time.sleep(0.5)

            try:
                if '맛집' in query:
                    loc = query.split(' ')[0]
                    answer = f'{loc} 추천 맛집으로는 '
                else:
                    answer = '추천하는 여행지로는 '
                for i in range(len(top5)):
                    answer += top5[i].text
                    if i == len(top5) - 1:
                        answer += ' '
                    else:
                        answer += ', '
                answer += '등이 있습니다.'
            except:
                answer = '아직 학습되지 않은 부분입니다. 죄송합니다.'
        driver.close()
        return answer

