from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main.views import index, test, sample # main의 views.py에서 index 모듈 가져다 사용할 거야!
from a.views import indexA
from b.views import indexB, indexBdetail
#from c.views import indexC
from c.views import BlogList, BlogDetail
from d.views import indexD, testview, SignupView, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('sample', sample),
    path('testtest/', test), # main의 views.py 파일에 test 함수 작성하자
    path('aa/', include('a.urls')),
    path('bb/', indexB),
    path('bb/<int:pk>/', indexBdetail), # 숫자로 오는 값을 받아서 인자로 넘겨줌
    #path('cc/', indexC),
    path('cc/', BlogList.as_view()),
    path('cc/<int:pk>/', BlogDetail.as_view()),
    path('dd/', indexD),
    path('dd/test', testview),
    path('dd/signup/', SignupView.as_view()),
    path('dd/login/', LoginView.as_view()),
    path('dd/logout/', LogoutView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)