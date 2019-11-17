from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Blog


# Create your views here.


class BlogList(ListView):  # 제네릭 뷰 사용
    model = Blog
    template_name_suffix = '_list'  # Django 에게 템플릿 접미사를 _list 로 사용하겠다는 뜻


class BlogCreate(CreateView):
    model = Blog
    fields = ['text', 'image']  # 사용할 필드
    template_name_suffix = '_create'
    success_url = '/'  # 기능이 성공하면 이동하는 페이지

    def form_valid(self, form):  # 입력받는 폼이 유효한지 확인하는 함수
        form.instance.author_id = self.request.user.id  # 요청한 유저의 아이디가 폼 유저의 아이디와 같은지 확인
        if form.is_valid():  # form 의 모든 검증기 API 인 validators 호출 유효성 검증 수행
            form.instance.save()  # 참이면 폼을 저장
            return redirect('/')  # / 로 재연결
        else:
            return self.render_to_response({'form': form})  # 거짓이면 렌더링할 템플릿 값들을 딕셔너리 형태로 폼으로 넘겨줌.


class BlogUpdate(UpdateView):
    model = Blog
    fields = ['text', 'image']
    template_name_suffix = '_update'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):  # request 요청을 검사해서 HTTP 메소드를 검사하는 메소드
        object = self.get_object()  # 오브젝트 변수에 현재 오브젝트들을 받아옴
        if object.author != request.user:  # 오브젝트 변수에 있는 유저 데이터가 요청한 유저와 다를 시
            messages.warning(request, "수정할 권한이 없습니다.")  # 메시지 출력
            return HttpResponseRedirect('/')  # 이 링크로 요청 및 재이동
        else:
            return super(BlogUpdate, self).dispatch(request, *args, **kwargs)  # 같을 시엔 상위 메서드로 값을 가지고 복귀


class BlogDelete(DeleteView):
    model = Blog
    template_name_suffix = '_delete'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, "삭제할 권한이 없습니다.")
            return HttpResponseRedirect('/')
        else:
            return super(BlogDelete, self).dispatch(request, *args, **kwargs)


class BlogDetail(DetailView):
    model = Blog
    template_name_suffix = '_detail'


class BlogMyList(ListView):
    model = Blog
    template_name = 'blog/blog_mylist.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:   # 만약에 요청할 때 로그인이 되지 않았다면
            messages.warning(request, '로그인 하세요!')
            return HttpResponseRedirect('/')
        return super(BlogMyList, self).dispatch(request, *args, **kwargs)
