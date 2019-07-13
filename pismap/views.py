from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def panel(request):
    return  render(request,"panel.html")


from fr import AFRTest
from django.http import HttpResponse

def face(request):
    res = AFRTest.checkFace(u'static/facedata/base/niewzh.jpg', u'static/facedata/base/niewzh.jpg')
    return HttpResponse(res)