from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Message
from membership.models import Member
from .forms import MessageForm


def sendMessage(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = Member.objects.get(username=form.cleaned_data.get("recipient"))
            message.content = form.cleaned_data.get("content")
            message.save()
            return redirect('listMessage')
        
        else:
            return HttpResponse('해당하는 아이디가 존재하지 않습니다. 다시 확인해주세요.')
            
    else:
        form = MessageForm()
        return render(request, 'sendMessage.html', {'form': form}
