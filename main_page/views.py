from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from .models import Article
from .forms import ArticleForm


def Upload_file(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('1/')
  else:
    form = ArticleForm()

  return render(request, 'main_page.html', {'form': form})

def files(request):
  all_files = Article.objects.all()
  return render(request, 'file_upload.html', locals())
