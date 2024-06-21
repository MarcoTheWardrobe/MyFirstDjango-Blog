from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from blog.forms import PostForm 
from .models import Post
import string, random
from django.http import HttpResponse, HttpResponseRedirect


from .forms import Ni
from django.http import HttpResponse
from django.template import loader
import json




def random_string(length):
    pool = string.ascii_lowercase + string.digits
    return ''.join(random.choice(pool) for i in range(length))

 


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
  
  
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.delete()
    return redirect('post_list')

def test_css(request):
   rnd = random_string(10)
   return render(request, 'blog/test.html',
                 {"rnd":rnd})

def test_pagina(request):
   rnd = random_string(10)
   return render(request, 'blog/test_pagina1.html',
                 {"rnd":rnd})

def final_test(request):
     
    rnd = random_string(10)
    return render(request, 'blog/final_test.html',
            {"rnd":rnd})

def final_eye(request):
    rnd = random_string(10)
    return render(request,'blog/final_eye.html', 
                {"rnd":rnd})



def get_form(request):
    
    form = Ni()

    return render(request, "blog/form.html", {"form": form})


def save_form(request):
    context_json = {}
    context_json["status"] = "error"
    context_json["msg"] = "Errore Generico"
    context_json["error_json"] = {}
    if request.method != "POST":
        return HttpResponse(json.dumps(context_json), content_type="application/json")
    data = json.loads(request.body)
    tform = Ni(data)
    if not tform.is_valid():
        print(tform.errors)
        context_json["msg"] = "Errore Nei Dati"
        return HttpResponse(json.dumps(context_json), content_type="application/json")
    context_json["status"] = "success"
    context_json["msg"] = "Salvato con successo"
    return HttpResponse(json.dumps(context_json), content_type="application/json")



        


def hey_txt(request):
    return render(request, "blog/hey.html", {})