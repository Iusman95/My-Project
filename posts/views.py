from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from posts.models import Post, Comment, Like
from posts.forms import CommentForm
from django.shortcuts import redirect

class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/new_post.html'
    fields = ['title', 'content', 'image']    



def comment_add(request, pk):
    posts = get_object_or_404(Post, id = pk)
    comment = Comment.objects.filter(posts=posts)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = posts 
            comment.save()
    else:
        form = CommentForm()
    
    return render(request, 'posts/detail.html', {'posts':posts, 'comment':comment, 'form':form})

def add_like(request, pk):
    post = get_object_or_404(Post, id=pk)
    Like.objects.create(post=post)
    return redirect('index')

