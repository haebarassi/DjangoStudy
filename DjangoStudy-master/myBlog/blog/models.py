from django.db import models

# Create your models here.
from django.db import models

# Post 모델은 models 모델의 Model 클래스를 확장해서 만든 파이썬 클래스이다
class Post(models.Model):
    title = models.CharField(max_length=30) # 최대 길이 30인 CharField 사용해서 만든다
    content = models.TextField()    # 문자열 길이 제한이 없는 textfield 사용해서 만든다

    created_at = models.DateTimeField(auto_now_add=True)     # DateTimeField는 월, 일, 시, 분, 초까지 기록할 수 있게 해주는 필드 만들 때 사용한다.
    updated_at = models.DateTimeField(auto_now=True)           # DateTimeField의 auto_now 속성
    # author 나중에 작성하기 <- 외래키 구현할 때 다룬다.

    def __str__(self):
        return f'[{self.pk}]{self.title}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}'