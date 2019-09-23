from django.shortcuts import render, redirect
from .models import Tutorial


# Create your views here.

def homepage(request):
    return render(
        request=request,
        template_name='main/homepage.html',
        context={"tutorials": Tutorial.objects.all}
    )


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login


def register(request):
    # check if request is a post
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(
        request=request,
        template_name='main/register.html',
        context={"form": form}
    )
