from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

def index(request):
    print(request) # 터미널에 사용자의 요청 사항 출력하기
    print(type(request))
    print(dir(request))
    print('============')
    print(request.POST) # 터미널에 POST 방식으로 넘어온 사용자의 요청 사항 출력하기
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

# def test(request):
#     return redirect('/') # 요청 받고 root 파일로 가라

# def test(request):
#     return HttpResponse('Hello world') # url에 /testtest 추가하면 Hello world 출력됨

def test(request):
    d = {'name':'princess', 'age':24}
    return JsonResponse(d)