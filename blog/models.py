from django.db import models

class Post(models.Model):    #일종의 DB 구조, field 설정
    title = models.CharField(max_length=30)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #auto_now_add=True : 현재 날짜의 시간을 자동으로 저장
    #auto_now=True : 수정 시 시간을 자동으로 바꿈

    def __str__(self):
        return f'[{self.pk}] {self.title}'
        #f'[]' : []안에 내용을 문자열로 변경
        #self.pk : primary key로 고정
