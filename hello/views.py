from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myview(request):
    num_visit = request.session.get('num_visit',0)+1
    request.session['num_visit'] = num_visit
    oldval = request.COOKIES.get('pp', None)
    resp = render(request, 'hello/main.html',{'num_visit':num_visit})
    if oldval:
        resp.set_cookie('pp', int(oldval)+1)
    else:
        resp.set_cookie('pp',69,max_age = 6969)
    return resp
    return render(request, 'hello/main.html')