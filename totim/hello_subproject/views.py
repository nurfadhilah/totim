from django.shortcuts import render
from hello_subproject.models import Student, Shobby, Mentor
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


# Create your views here.
def index(request):
    mystudents =Student.objects.all().values()
    context = {

        'nama':'Fadhilah',
        'mystudents':mystudents,
        'message':'CONGRATS, DONE CALLING'
    }
    return render(request,'index.html', context)


def newmentor(request):
    mymentor=Mentor.objects.all().values()
    if  request.method=='POST':
        idmentor=request.POST['id']
        idname=request.POST['name']
        idroom=request.POST['room']
        data=Mentor(menid=idmentor, menname=idname, menroomno=idroom)
        data.save()

        context = {
        'mymentor':mymentor,
        'message':'SUCCESS'

        }

        return render(request, "newmentor.html", context)

    else:
        dict={
            'message':'',
            'mymentor':mymentor,
        }
    return render(request,"newmentor.html",dict)

def newstudent(request):
    mystudent=Student.objects.all().values()
    mymentor=Mentor.objects.all().values()

    if request.method=='POST':
        idstud=request.POST['id']
        namestud=request.POST['name']
        emailstud=request.POST['email']
        agestud=request.POST['age']

        mentorstud=request.POST['mentor']
        mentornew = Mentor.objects.get(menid=mentorstud)
        data1=Student(stuid=idstud, stuname=namestud, stuemail=emailstud, stuage=agestud, stumentor=mentornew )
        data1.save()

        context = {

        'mystudent':mystudent,
        'mymentor':mymentor,
        'message':'SUCCESS'
        }
    
        return render(request,"newstudent.html", context)

    else:
        dict={
            'mystudent':mystudent,
            'message':'SORRY',
            'mymentor':mymentor,
        }
    
    return render(request,"newstudent.html", dict)

def update(request,stuid):
    updateid=Student.objects.get(stuid=stuid)
    dict={
        'updateid':updateid
    }

    return render(request, "studentupdate.html",dict)

def updatedata(request,stuid):
    data=Student.objects.get(stuid=stuid)
    sname=request.POST['sname']
    email=request.POST['email']
    age=request.POST['age']

    data.stuname=sname
    data.stuemail=email
    data.stuage=age
    data.save()

    return HttpResponseRedirect(reverse("newstudent"))

def delete(request,stuid):
    deleteid=Student.objects.get(stuid=stuid)
    dict={
        'deleteid':deleteid
    }

    return render(request, "studentdelete.html",dict)

def deletedata(request,stuid):
    data=Student.objects.get(stuid=stuid)
    data.delete()
    
    return HttpResponseRedirect(reverse("newstudent"))

def searchpage(request):
    search_query = request.GET.get('search', '')
    mymentor = Mentor.objects.filter(Q(stuid__icontains=search_query)) if search_query else []

    if search_query:
        return render(request, 'resultresearch.html', {'mymentor': mymentor})
    else:
        return render(request, 'search.html', {'mymentor': mymentor})





