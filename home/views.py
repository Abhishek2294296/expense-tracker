from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate , login as loginUser,logout
 
 

def home(request):
    profile = Profile.objects.filter(user = request.user).first()
    expenses = Expense.objects.filter(user = request.user)
    if request.method == 'POST':
        text = request.POST.get('text')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('expense_type') 

        expense = Expense(name=text , amount=amount , expense_type=expense_type , user= request.user)
        expense.save()
        
        if expense_type == 'Positive':
            profile.balance += float(amount)
        else:
            profile.expenses += float(amount)
            profile.balance -= float(amount)
            
        profile.save()
        return redirect('/')

    context = {'profile' : profile , 'expenses' : expenses}
    return render(request , 'home.html' , context) 
def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form' : form
        }
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data = request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            context = {
                'form' : form
            }
            return render(request, 'login.html', context=context)

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form              
        }
        return render(request, 'signup.html', context=context)
    
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            "form" : form              
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context=context)

def signout(request):
    logout(request)
    return redirect('login')    