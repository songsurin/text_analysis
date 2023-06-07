from django.shortcuts import render, redirect
from travel.mychatbot import getMessage
from travel.models import Chat
import socket
import json

def get_answer(query):
    # 챗봇 엔진 서버 연결
    mySocket = socket.socket()
    mySocket.connect(("127.0.0.1", 5050))
     # 챗봇 엔진 질의 요청
    json_data = {
        'Query': query,
    }
    message = json.dumps(json_data)
    mySocket.send(message.encode())
    # 챗봇 엔진 답변 출력
    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)
    # 챗봇 엔진 서버 연결 소켓 닫기
    mySocket.close()
    return ret_data

def recommend(request):
    return render(request, 'travel/recommend.html')


def query(request):
    question = request.GET["question"]
    # message = json.dumps(json_data)
    # mySocket.send(message.encode())
    #
    # # 챗봇 엔진 답변 출력
    # data = mySocket.recv(2048).decode()
    # ret_data = json.loads(data)
    msg = getMessage(question)
    query=msg['Query']
    answer=msg['Answer']
    intent=msg['Intent']
    # Chat(query=query,intent=intent).save()
    Chat(query=query, answer=answer,intent=intent).save()
    items=Chat.objects.order_by('idx')

    return render(request, 'travel/result.html',{'items':items})

def delete_chat(request):
    Chat.objects.all().delete()
    return redirect('/result')


def research1(request):

    question = request.GET["question"]
    msg = getMessage(question)
    ans = msg["in"]
    Q = msg['q']
    I = msg['Item']
    answer = ans.research(Q, I)
    intent = msg['Intent']

    Chat(answer=answer, query=question, intent=intent).save()
    items = Chat.objects.order_by('idx')

    return render(request, 'travel/result.html',{'items':items})
