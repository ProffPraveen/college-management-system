from email.message import Message

from django.shortcuts import render
from django.http import HttpResponse
from docutils.nodes import description
#from tensorboard.plugins.custom_scalar.layout_pb2 import Category

from .models import *

# Create your views here.
def index(request):
    data=tbl_notice.objects.all().order_by('-id')[0:6]
    data1=tbl_feedback.objects.all().order_by('-id')[0:4]
    data2=tbl_slider.objects.all().order_by('-id')[0:4]
    data3 = tbl_event.objects.all().order_by('-id')[0:5]
    md={"ndata":data,"fdata":data1,"sdata":data2,"edata":data3}
    return render(request, 'index.html',md)

def about(request):
    return render(request,'about.html')

def contact(request):
    mydict={}
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mobile')
        d=request.POST.get('subject')
        e=request.POST.get('msg')
        contactus(Name=a,Email=b,Mobile=c,Subject=d,Message=e).save()
        return HttpResponse("<script>alert('Data Save Successful');location.href='/contact/'</script>")

       #mydict={"name":a,"email":b,"mobile":c,"subject":d,"message":e}
    return render(request,'contact.html',mydict)

def courses(request):
    data=tbl_courses.objects.all().order_by('-id')
    md={"cdata":data}
    return render(request,'course.html',md)


def faculty(request):
    data=tbl_faculty.objects.all().order_by('-id')
    md={'fdata':data}
    return render(request,'faculty.html',md)


def feedback(request):
    mydict={}
    if request.method=="POST":
        name=request.POST.get('name')
        picture=request.FILES['fu']
        message=request.POST.get('message')
        tbl_feedback(name=name,feedback=message,picture=picture).save()
        return HttpResponse("<script>alert('Thanks for your valuable feedback.....');location.href='/contact/';</script>")
    return render(request,'feedback.html',mydict)

def gallery(request):
    data=tbl_gallery.objects.all().order_by('-id')[0:21]
    mydict={'gdata':data}
    return render(request,'gallery.html',mydict)

def infra(request):
    data=tbl_infra.objects.all().order_by('-id')
    md={"idata":data}
    return render(request,'infra.html',md)

def recruiters(request):
    data=tbl_recruiter.objects.all().order_by('-id')
    md={'gdata':data}
    return render(request,'recruiters.html',md)

def alumony(request):
    data=tbl_alumni.objects.all().order_by('-id')
    md={"adata":data}
    return render(request,'alumony.html',md)

def principal(request):
    data=tbl_principal.objects.all().order_by('-id')
    md={"mdata": data}
    return render(request,'principal message.html',md)

def portfolio(request):
    return render(request,'my profile.html')

def faqs(request):
    return render(request,'FAQS.html')

def help(request):
    mydict={}
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('description')
        d=request.POST.get('category')
        tbl_help(Name=a,Email=b,Description=c,Category=d).save()
        return HttpResponse("<script>alert('Data Save Successful');location.href='/help/'</script>")

    return render(request, 'help.html', mydict)

def chat(request):
    return render(request,'chat.html')



#def helpdesk(request):
 #   mydict={}
 #   if request.method=="POST":
 #       a=request.POST.get('name')
       # b=request.POST.get('email')
   #     c=request.POST.get('description')
     #   helpdesk(Name=a,Email=b,Description=c).save()
     #   return HttpResponse("<script>alert('Data Save Successful');location.href='/help/'</script>")

    #return render(request, 'help.html', mydict)
