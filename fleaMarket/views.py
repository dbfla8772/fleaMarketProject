from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404  #404는 서버가 요청한 페이지를 찾을 수 없다.
from django.core.paginator import Paginator
from .models import FleaMarket
from .forms import FleaMarketForm
from django.utils import timezone
import os, json

def home(request):
    # blogObject = FleaMarket.objects.all()   
    blogObject = FleaMarket.objects.order_by("-pub_date") # 최신글 순서대로 저장

    paginator = Paginator(blogObject, 6) # 넣어야 하는 페이지 개수
    page = request.GET.get('page')  # GET 정보가 오지 않아도 넘어감. 페이지의 정보를 받음.
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogObject':blogObject, 'posts':posts})

def detail(request, id):  # Read
    blogModel = get_object_or_404(FleaMarket, pk = id)  # pk = Primary Key (데이터베이스의 식별자), Table의 row 하나하나를 구별하는 ID값
    blogDict = {
        'lat': blogModel.lat,
        'long': blogModel.long,
    }
    blogJson = json.dumps(blogDict)
    return render(request, 'detail.html', {'blogModel':blogModel, 'blogJson':blogJson})

def new(request):  #new.html을 보여줌.
    if request.method == 'POST':
        post_form = FleaMarketForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)  # 임시저장
            new_post.writer = request.user
            new_post.pub_date = timezone.now()
            new_post.save()
            return redirect('detail', new_post.id)
        return redirect('home')
    else:
        post_form = FleaMarketForm()
        return render(request, 'new.html', {'post_form':post_form})

def edit(request, id):  # edit.html을 보여줌. 
    edit_post = get_object_or_404(FleaMarket, pk=id)
    if request.method == 'GET':
        post_form = FleaMarketForm(instance = edit_post)
        return render(request, 'edit.html', {'post_form':post_form})
    else:
        post_form = FleaMarketForm(request.POST, request.FILES, instance = edit_post)
        if post_form.is_valid():
            edit_post = post_form.save(commit=False)  # 임시저장
            edit_post.pub_date = timezone.now()
            edit_post.save()
            return redirect('detail', edit_post.id)      

def delete(request, id):    # Delete
    delete_post = FleaMarket.objects.get(id=id)
    delete_post.delete()
    return redirect('home') 

def file_download(request, id):
    blog = get_object_or_404(FleaMarket, pk = id)

    file_path = blog.file.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/file")
            response['Content-Disposition'] = 'inline;filename='+ blog.get_filename()
            return response