from django.db import models

# Create your models here.
class Notice(models.Model): # 클래스 작성시 변수만 지정하면 됨
    title = models.CharField(max_length=100) # 게시물제목: 문자열 field, 최대 길이 100 제한
    likeCount = models.IntegerField() # 좋아요수
    viewCount= models.IntegerField() # 뷰수
    contents= models.TextField() # 내용
    
    def __str__(self):
        return f'{self.title} : {self.likeCount}' # title이 Notice를 대표하는 문자열 값이야
    
#lass 댓글():    # 게시물 : 댓글  =>  1:N 혹은 N:N