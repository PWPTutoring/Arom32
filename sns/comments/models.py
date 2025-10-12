from django.db import models

# Create your models here.
class Comment(models.Model): #새 테이블
    content = models.CharField(max_length=200) #col 생성
    created_at = models.DateTimeField(auto_now_add=True)

    # max_length 데이터 최대길이, 
    # auto_now_add=True 데이터 생성 시, 생성 시각 저장.

    def __str__(self):
        return f"{self.content[:20]}..." 
    # Commemt 객체 출력시의 출력 값 
    # 보통 admin 페이지에서의 데이터 보여줌 + logging debug 용도