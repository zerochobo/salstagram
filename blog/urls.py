from django.urls import path
from .views import BlogList, BlogCreate, BlogDelete, BlogDetail, BlogUpdate, BlogMyList
from django.conf.urls.static import static
from django.conf import settings

app_name = "blog"
urlpatterns = [
    path("create/", BlogCreate.as_view(), name='create'),
    path("delete/<int:pk>/", BlogDelete.as_view(), name='delete'),
    path("update/<int:pk>/", BlogUpdate.as_view(), name='update'),
    path("detail/<int:pk>/", BlogDetail.as_view(), name='detail'),
    path("", BlogList.as_view(), name='index'),
    path("mylist/", BlogMyList.as_view(), name='mylist')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 미디어 파일 제공하는 URL 패턴 수정 static 함수가 첫 번째 인자로 setting.py 에 설정된 MEDIA_URL 을 가져오고,
# 키워드 인자로 미디어 파일이 위치한 경로를 전달함. - 이미지가 오류로 보이는 것을 막아 줌.
