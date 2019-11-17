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