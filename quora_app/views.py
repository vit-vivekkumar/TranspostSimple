from django.http import JsonResponse
from .form import PostForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Like, Post, Comment
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    post_list = Post.objects.all().order_by('-created_on')
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')  # Redirect to refresh the post list
    else:
        form = PostForm()
    
    return render(request, 'home.html', {'post_list': post_list, 'form': form})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)

    if not created:
        like.delete()  # Unlike if already liked
        liked = False
    else:
        liked = True

    return JsonResponse({'likes_count': post.likes.count(), 'liked': liked})

@login_required
def comment_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(post=post, author=request.user, content=content)

    comments = post.comments.all()  # Fetch all comments
    return render(request, "partials/comments_list.html", {"post": post, "comments": comments})
