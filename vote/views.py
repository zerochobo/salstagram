from django.shortcuts import get_object_or_404, redirect
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]   #
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)

from django.shortcuts import get_object_or_404, redirect

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'blog/results.html', {'question': question})

    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice']) #
    except:
        return render(request, 'blog/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question_id = question_id)

def results(request, question_id):
    question = get_object_or_404(Question, qk = question_id)
    return render(request, 'blog/results.html', {'question': question})



