from django.shortcuts import render, redirect
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import PostForm
from datetime import date


def add_model(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = date.today()
            post.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blogging/add.html', {'form': form})


class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__isnull=True).order_by(
        "published_date"
    )
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__isnull=True)
    template_name = "blogging/detail.html"
