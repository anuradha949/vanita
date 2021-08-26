
from django.shortcuts import HttpResponseRedirect, render
from.forms import LoginForm,SignupForm
from .models import Login,Signup
from django.contrib import auth




# Create your views here.
def login_Form(request):
    if request.method == 'POST':
        fm=LoginForm(request.POST)
        if fm.is_valid():
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
           
            #  print(em)
            #  print(pw)
        
            regi = Login(email=em)
            regi.save()
            fm=LoginForm() 
            
    else:
        fm=LoginForm() 
    return render(request,'app/login.html',{'form':fm})




# Create your views here.
# @login_required
def Sign_Up(request):
    if request.method == 'POST':
        fm=SignupForm(request.POST)
        if fm.is_valid():
            
            nm = fm.cleaned_data['username']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            cp = fm.cleaned_data['confirm_password']
            ad = fm.cleaned_data['address']
            #  print(un)
            #  print(em)
            #  print(ps)
            #  print(cp)
            #  print(ad)
            regis = Signup(username=nm, email=em, address=ad)
            regis.save()
            
    else:
        fm=SignupForm() 
    return render(request,'app/signup.html',{'form':fm})






# Create your views here.
# this function will give user detail
def user_detail(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['username']
            em = fm.cleaned_data['email']
            ad = fm.cleaned_data['address']
            reg = Signup(username=nm, email=em, address=ad)
            reg.save()
            fm = SignupForm()
    else:
        fm = SignupForm()
    stud = Signup.objects.all()

    return render(request, 'app/userdetail.html',{'form':fm, 'stu':stud})


# this function will update items 
def update_data(request, id):
    if request.method == 'POST':
        pi = Signup.objects.get(pk=id)
        fm = SignupForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Signup.objects.get(pk=id)
        fm = SignupForm(instance=pi)
    return render(request, 'app/updateuser.html', {'form':fm})




# this function will delete items 
def delete_data(request, id):
    if request.method == "POST":
        pi = Signup.objects.get(pk=id)
        pi.delete()
        # return HttpResponseRedirect('app/userdetail.html')
        return render(request, 'app/userdetail.html')