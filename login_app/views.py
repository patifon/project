from django.shortcuts import render
from login_app.forms import AuthUserForm
from register_app.views import *
from register_app.models import UserRegisterGroup
def login(request):
    form=AuthUserForm(request.POST or None)

    if request.method=='POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data['user_name'])
        print(data['user_password'])
        new_form = form.save()
        name=data['user_name']
        password=data['user_password']
        name_html = new_form.user_name
        try:
            if UserRegisterGroup.objects.get(password=password, name=name):
                return render(request, name_html+'.html', locals())
        except UserRegisterGroup.DoesNotExist:
            return render(request, 'auth_error.html', locals())




    return render(request, 'login.html', {'form': form})












