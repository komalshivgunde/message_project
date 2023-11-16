from django.shortcuts import render,HttpResponse,redirect
from message_app.models import Msg
#from .model import Msg

# Create your views here.
def create(request):
    if request.method=='POST':
        print("request is:",request.method)
        #access values from form
        n=request.POST['uname']
        mail=request.POST['uemail']
        mobile=request.POST['mobile']
        msg=request.POST['msg']
        m=Msg.objects.create(name=n,email=mail,mobile=mobile,msg=msg)
        m.save()
        '''
        print(n)
        print(mail)
        print(mobile)
        print(msg)
        '''
       # return HttpResponse("data fetched successfully")
        return redirect('/dashboard')
    else:
       # print("request is:",request.method)
        return render(request,'create.html')

def dashboard(request):
    m=Msg.objects.all()
    print(m)
    context={}
    context['data']=m
    #return HttpResponse("data fetched")
    return render(request,'dashboard.html',context)

def delete(request,rid):
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')
    #return HttpResponse("id to be deleted"+rid)

def edit(request,rid):
    if request.method=='POST':
        #submit form with new values
        n=request.POST['uname']
        mail=request.POST['uemail']
        mobile=request.POST['mobile']
        msg=request.POST['msg']
        m=Msg.objects.filter(id=rid)
        m.update(name=n,email=mail,mobile=mobile,msg=msg)
        return redirect('/dashboard')
    else:
        #display form with old data
        m=Msg.objects.get(id=rid)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
    #return HttpResponse("id to be edited"+rid)