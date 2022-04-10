from django.db import models
import random
from django.contrib.auth.models import User

class Blog(models.Model): # 클래스 작성시 변수만 지정하면 됨
    title = models.CharField(max_length=100) # 게시물제목: 문자열 field, 최대 길이 100 제한
    # author : 인증 뒤에서 언급함
    # 저자는 한 명뿐이어야 하기 때문에 외래키 관계로 지정
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    contents= models.TextField() # 내용
    #img = models.ImageField(blank=True)
    r = random.randint(1, 10000)
    img = models.ImageField(upload_to='bb/%Y/%m/%d/{r}', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True) # 처음 생성한 날짜를 저장하고 다시 갱신하지 않음
    modified_at = models.DateTimeField(auto_now=True, null=True) # 수정될 때마다 시간 저장
    
    def __str__(self):
        return f'제목 : {self.title}, 좋아요 수 : {self.contents}' 
    
#lass 댓글():    # 게시물 : 댓글  =>  1:N 혹은 N:N