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
        form.instance.author_id = self.request.user.id  # 요청한 유저의 아이디가 폼 유저의 아이디와 같다면
        if form.is_valid():  # form : 모델폼
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})


class BlogUpdate(UpdateView):
    model = Blog
    fields = ['text', 'image']
    template_name_suffix = '_update'
    # success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, "수정할 권한이 없습니다.")
            return HttpResponseRedirect('/')
        else:
            return super(BlogUpdate, self).dispatch(request, *args, **kwargs)


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
        if not request.user.is_authenticated:
            messages.warning(request, '로그인 하세요!')
            return HttpResponseRedirect('/')
        return super(BlogMyList, self).dispatch(request, *args, **kwargs)
