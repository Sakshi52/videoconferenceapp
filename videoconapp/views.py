from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def user_register(request):
    content={}
    regobj=UserForm
    # print(regobj)
    content['userform']=regobj
    if request.method=="POST":
        regobj=UserForm(request.POST)
        if regobj.is_valid():
            regobj.save()
            content['success']='User Created Successfully'
            return render(request,'user_register.html',content)
        else:
            print("error give")
    return render(request,'user_register.html',content)

def login_view(request):
    if request.method=="POST":
        dataobj=AuthenticationForm(request=request,data=request.POST)
        # print('reuquest user',request.user.first_name)
        if dataobj.is_valid():
            uname=dataobj.cleaned_data['username']
            upass=dataobj.cleaned_data['password']
            u=authenticate(username=uname,password=upass)
            if u:
                login(request,u)
                # return render(request,'dashboard.html')
                return redirect('/dashboard')
            
    else:
             
        lobj=AuthenticationForm
        content={}
        content['loginform']=lobj
        return render(request,'user_login.html',content)
            

@login_required
def dashboard(request):
    return render(request,'dashboard.html',{'name':request.user.first_name})

@login_required
def videocall(request):
    return render(request,'videocall.html',{'name':request.user.first_name+' '+request.user.last_name})

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'joinroom.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('/login')