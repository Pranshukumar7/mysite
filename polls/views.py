from django.http import HttpResponse
from .models import Question

def owner(request):
    return HttpResponse("Hello, world. e6d13316 is the polls index.")

def index(request):
    qu = Question.objects.order_by('-pub_date')
    output = ",".join([q.question_text for q in qu])
    return HttpResponse(output)

# result
def result(request,question_id):
    return HttpResponse("hey you are looking at result of %s" % question_id)
# detail
def detail(request,question_id):
    return HttpResponse("hey you are looking at detail of %s" % question_id)
#vote
def vote(request,question_id):
    return HttpResponse("hey you are voteing of %s" % question_id)