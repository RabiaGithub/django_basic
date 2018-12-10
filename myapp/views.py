from django.shortcuts import render
from .forms import RegisterForm


def index(request):
        if request.method == "POST":
                form = RegisterForm(request.POST)
                if form.is_valid():
                        name = form.cleaned_data['name']
                        email = form.cleaned_data['email']
                        print(name,email)
                        form.save()
        form = RegisterForm()
        return render(request,'formapp/index.html',{'form':form})

def modal_detail(request):
        return render(request,'formapp/form.html')


