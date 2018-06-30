from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import UserRegisterGroup
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from main_page.forms import *
from main_page.models import *
from django.http import HttpResponseRedirect



def register(request):
    form = UserRegistrationForm(request.POST or None)
    form1=UserRegisterGroup
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])
        new_form = form.save()
        path = "templates//"
        name_html=new_form.name
        path_with_name = path +name_html+'.html'
        template="""
       {% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Первый анонимный Дата Центр</title>
    <link rel="stylesheet" href="{% static 'main_page/css/style.css' %}">
        <link rel="stylesheet" href="{% static 'main_page/css/bootstrap.min.css' %}">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  	<a class="navbar-brand navbar-brand1" href="/">Data Center</a>
  	<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar1" aria-controls="navbar1" aria-expanded="false" aria-label="Toggle navigation">
    	<span class="navbar-toggler-icon"></span>
  	</button>

  	<div class="collapse navbar-collapse" id="navbar1">
    	<ul class="navbar-nav mr-auto">
      		<li class="nav-item active">
        		<a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      		</li>
		    <li class="nav-item">
		    	<a class="nav-link" href="#">Link</a>
		    </li>
      		<li class="nav-item dropdown">
        		<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown1" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Dropdown</a>
        		<div class="dropdown-menu" aria-labelledby="navbarDropdown1">
          			<a class="dropdown-item" href="#">Action</a>
          			<a class="dropdown-item" href="#">Another action</a>
          			<div class="dropdown-divider"></div>
          			<a class="dropdown-item" href="#">Something else here</a>
        		</div>
      		</li>
    	</ul>
  	</div>
</nav>
<div class="container my-container">
    <form class="form-horizontal" method="post" enctype="multipart/form-data">{% csrf_token %}
<div class="form-group">

<div class="form-group">
<label for="file" class="col-sm-2 control-label">Файл</label>
<div class="col-sm-8">
<input type="file" name="{{ form.file_obj.name }}" id="file">
</div>
</div>
<div class="form-group">
<div class="col-sm-offset-2 col-sm-8">
<button type="submit" id="submit" class="btn btn-primary" onclick="location.href='/1/'">Отправить</button>
<div></div>
</div>
</div>
</div>
</form>
</div>

{% for file in all_files %}
     <img src="{% static 'main_page/img/rar.png' %}">
    <a href="{{ file.file_obj.url }}" download>download</a>
{% endfor %}

<link rel="stylesheet" href="{% static 'main_page/js/bootstrap.min.js' %}">
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
</body>
</html>
        """
        user_html = open(path_with_name, 'w', encoding='UTF-8')
        user_html.write(template)
        user_html = open(path_with_name, 'r', encoding='UTF-8')
        return render(request, name_html+'.html',{'form': form})

    return render(request, 'register.html', {'form': form})

def user_cabinet(request):
    return render(request, 'auth_error.html', locals())













