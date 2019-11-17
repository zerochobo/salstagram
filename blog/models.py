from django.db import models
from django.contrib.auth.models import User  # 유저 기능을 위한 장고 모델 import
from django.urls import reverse  # absolute url 사용을 위한 reverse 기능 호출


# Create your models here.


class Blog(models.Model):  # 블로그 전체 모델 DB 구조
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # User 기능을 위해 호출한 장고의 기본 모델에서 User 키를 1:N 구조를 위해 ForeignKey 로 받아옴.
    text = models.TextField(max_length=500, null=True, blank=True)
    # 본문 기능, 본문의 글자의 한계치를 500글자로 한정했고, null, blank 를 True 로 줌으로써 본문을 쓰지 않아도 되게 함.
    image = models.ImageField(upload_to='Photo/%Y/%m/%d')
    # 이미지 업로드 기능, 필수적으로 채워야 하며, 여기에 업로드한 파일은 프로젝트 내 Photo/연도/월/일 순으로 저장됨.
    created_date = models.DateTimeField(auto_now_add=True)
    # 생성일로, 연,월,일 모두 작성 시 추가되게 해놨으며, auto_now_add=True 를 이용해 그 당시 딱 한 번만 저장되게 함.
    updated_date = models.DateTimeField(auto_now=True)
    # 수정일로, 연,월,일 모두 작성 시 추가되게 해놨으며, auto_now=True 를 이용해 수정할 때 마다 갱신되어 저장되게 함.

    def __str__(self):
        return self.text

    def delete(self, *args, **kwargs):  # delete 인스턴스 메서드 호출 / 모델을 삭제하는 기능 호출 시 파일 삭제 기능 수행
        self.image.delete()  #
        super(Blog, self).delete(*args, **kwargs)  # 함수가 넘겨받는 인자를 알지 못하기 때문에 args, kwargs 사용
        # 모델 객체 자체를 삭제하기 위해 super 함수를 사용하여 상속받은 부모 클래스의 delete 인스턴스 메서드 호출

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.id])
    # views 에서 모델 인스턴스가 개별 데이터에 접속할 때 마다 자동으로 호출되게 함.

    class Meta:
        ordering = ['-created_date', ]  # 생성 날짜를 이용해 최신 글이 위에 올 수 있도록 역순 ordering 정렬 사용.


