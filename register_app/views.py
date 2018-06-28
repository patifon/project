from django.shortcuts import render
from .forms import UserRegistrationForm



def register(request):
    name = "idroid"
    current_day='01.01.2018'
    form = UserRegistrationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'register.html', {'form': form})


