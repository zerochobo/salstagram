from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Board
from django.http.response import HttpResponseRedirect
from django.contrib import messages


# Create your views here.

class BoardList(ListView):
    model = Board
    template_name_suffix = '_list'
    paginate_by = 4


class BoardCreate(CreateView):
    model = Board
    fields = ['author', 'title', 'text', 'key']
    template_name_suffix = '_create'
    success_url = "/board"


class BoardDelete(DeleteView):
    model = Board
    template_name_suffix = '_delete'
    success_url = "/board"

    def delete(self, request, *args, **kwargs):
        if request.method == "POST":
            if request.POST["key"] != request.POST["key2"]:
                messages.warning(request, "삭제 비밀번호를 틀리셨습니다.")
                return HttpResponseRedirect('/board')
            else:
                return super(BoardDelete, self).delete(request, *args, **kwargs)


class BoardDetail(DetailView):
    model = Board
    template_name_suffix = '_detail'


class BoardUpdate(UpdateView):
    model = Board
    fields = ['title', 'text']
    template_name_suffix = '_update'
    success_url = "/board"

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            if request.POST["key"] != request.POST["key2"]:
                messages.warning(request, "비밀번호를 틀리셨습니다.")
                return HttpResponseRedirect('/board')
            else:
                return super(BoardUpdate, self).post(request, *args, **kwargs)
