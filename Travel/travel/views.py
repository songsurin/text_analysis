from django.shortcuts import render, redirect
from travel.mychatbot import getMessage
from travel.models import Chat
from django.http import JsonResponse
import socket
import json
import sys

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
    print(question)
    # message = json.dumps(json_data)
    # mySocket.send(message.encode())
    #
    # # 챗봇 엔진 답변 출력
    # data = mySocket.recv(2048).decode()
    # ret_data = json.loads(data)
    msg = getMessage(question)
    print(msg)
    query=msg['Query']
    answer=msg['Answer']
    intent=msg['Intent']
    tf=msg['TF']

    Chat(query=query,intent=intent,tf=tf).save()
    Chat(answer=answer,intent=intent,tf=tf).save()
    items=Chat.objects.order_by('idx')
    print(items)

    return render(request, 'travel/result.html',{'items':items})

def delete_chat(request):
    Chat.objects.all().delete()
    return redirect('/result')

def research(request):
    return redirect('/result')