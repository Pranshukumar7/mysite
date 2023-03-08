from django.http import HttpResponse , Http404
from .models import Question

from django.shortcuts import render
def owner(request):
    return HttpResponse("Hello, world. e6d13316 is the polls index.")

def index(request):
    output = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': output}
    return render(request, 'index.html',context)

# result
def result(request,question_id):
    return HttpResponse("hey you are looking at result of %s" % question_id)
# detail
def detail(request,question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    return render(request,'details.html',{'question':question})
def vote(request,question_id):
    return HttpResponse("hey you are voteing of %s" % question_id)