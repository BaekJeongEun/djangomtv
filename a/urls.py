from django.urls import path, include
from a.views import indexA, indexaaa, indexbbb, indexccc

app_name = 'a' # 앱 이름 지정

urlpatterns = [
    path('', indexA, name='sampleA'), # name 지정해서 html 파일에서 템플릿 태그로 사용할 거야!
    path('aaa/', indexaaa, name='sampleaaa'), # aaa 다음 어떤 문자열이 나오던 간에 a.urls.py로 이동해라
    path('bbb/', indexbbb),
    path('ccc/', indexccc),
]
