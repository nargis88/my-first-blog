from django.conf import settings
from django.db  import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Post(게시글)               객체
# --------           
# title(제목)                속성
# text(내용)                 속성
# author(글쓴이)             속성
# created_date(작성일)       속성
# published_date(게시일)     속성

# publish                   행위(메서드)  
