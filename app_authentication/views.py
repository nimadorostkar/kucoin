from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse, HttpResponseRedirect, request
from django.contrib import messages








#------------------------------------------------------------------------------
def login(request):
    if request.method == "POST":
        user = authenticate( username=request.POST['username'], password=request.POST['password'] )
        login(request, user)
        return redirect("/")
    return render(request, "account/login.html")









'''
#------------------------------------------------------------------------------
def register_user(request):
    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'کاربر ایجاد شد - <a href="/login">ورود</a>.'
            success = True

            #return redirect("/login/")

        else:
            msg = 'اطلاعات فرم معتبر نیست'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })
'''
