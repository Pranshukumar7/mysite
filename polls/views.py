from django.http import HttpResponse , Http404 ,HttpResponseRedirect
from .models import Question , Choice
from django.urls import reverse
from django.shortcuts import get_object_or_404

from django.shortcuts import render
def owner(request):
    return HttpResponse("Hello, world. e6d13316 is the polls index.")

def index(request):
    output = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': output}
    return render(request, 'index.html',context)

# result
def result(request,question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html',{'question':question})
# detail
def detail(request,question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    return render(request,'details.html',{'question':question})
def vote(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    try : 
        selected_choice = Choice.objects.get(pk = request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'details.html',{'question':question,'error_message':"you didn't select a choice"})
    else:
        selected_choice.votes+=1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:result',args = (question_id,)))
