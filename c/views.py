from django.shortcuts import render
from django.views.generic import ListView, DetailView
from b.models import Blog

# def indexC(request):
#     return render(request, 'indexC.html')

class BlogList(ListView):
    model = Blog
    template_name = 'indexC.html' #class명_list.html 파일을 자동으로 찾음

class BlogDetail(DetailView):
    model = Blog
    template_name = 'indexCdetail.html' #class명_detail.html 파일을 자동으로 찾음