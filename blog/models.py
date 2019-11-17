from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='Photo/%Y/%m/%d')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "text : " + self.text

    class Meta:
        ordering = ['-created_date', ]  # 생성 날짜를 이용해 최신 글이 위에 올 수 있도록 역순 ordering 정렬 사용.

    def delete(self, *args, **kwargs):  # delete 인스턴스 메서드 호출 / 모델을 삭제하는 기능 호출 시 파일 삭제 기능 수행
        self.image.delete()
        super(Blog, self).delete(*args, **kwargs)  # 함수가 넘겨받는 인자를 알지 못하기 때문에 args, kwargs 사용
        # 모델 객체 자체를 삭제하기 위해 super 함수를 사용하여 상속받은 부모 클래스의 delete 인스턴스 메서드 호출

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.id])

