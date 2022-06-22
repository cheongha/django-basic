# DB 관련
# 모델 설정 전 $ python manage.py migrate : 데이터베이스에 테이블 생성
import datetime

from django.db import models
from django.utils import timezone

# 모델 생성
# Question 테이블
class Question(models.Model): # models.Model을 상속받고 시작
    question_text = models.CharField(max_length=200) # 스키마 선언
    pub_date = models.DateTimeField('date published')
    def __str__(self): # Question.objects.all() 조회할 때 가독성을 높이기 위해 커스텀
        return self.question_text
    def was_published_recently(self): # 지금으로부터 하루 전 발행되는지
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Choice 테이블
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 1번 Question이 삭제되면, 1번 question을 가지고 있는 모든 choice들도 삭제
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
# 모델 활성화
# mysite/settings.py INSTALLED_APPS = ['polls.apps.PollsConfig',~] 추가
# $ python manage.py makemigrations polls
# polls/migrations/0001_initial.py 파일 생성됨 : 각 DB를 스키마를 나타내는 파일