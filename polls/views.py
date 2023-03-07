from django.http import HttpResponse
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
    return HttpResponse("hey you are looking at detail of %s" % question_id)
#vote
def vote(request,question_id):
    return HttpResponse("hey you are voteing of %s" % question_id)