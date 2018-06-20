from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import  IssuePostForm, IssueCommentForm
from django.contrib.auth.decorators import login_required

@login_required
def get_posts(request):
    """
    get a list of post were published prior to now and
    render them to the 'issueposts.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'issueposts.html', {'posts': posts})

@login_required    
def post_detail(request, pk):
    """
    return a singe post based on post.id from issueposts.html's
    list.
    """
    post = get_object_or_404(Post, pk=pk)
    post.save()
    return render(request, "post_detail.html", {'post': post})

@login_required
def create_or_edit_post(request, pk=None):
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = IssuePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # update for data
            form.save()  # save form to DB
            return redirect(post_detail, post.pk)
        else:
            return redirect(get_posts)
    elif post:
            print("elif post")
            print("{0}--{1}--{2}".format(post.id, post.title, post.content))
            form = IssuePostForm(data = {'title': post.title, 'content': post.content, 'published_date': post.published_date, 'tag' : post.tag, 'image': post.image}, instance=post)  
    else:
            form = IssuePostForm()
    return render(request, 'issuepostform.html', {'form': form})    
    
    
@login_required
def create_or_edit_comment(request, pk=None):    
    comment = get_object_or_404(Comment, pk=pk) if pk else None
    
    if request.method == "POST":
        form = IssueCommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            form.save()
            return redirect(post_detail, comment.post.pk)
    elif comment:
        form = IssueCommentForm({'comment': comment.comment, 'post': comment.post.title}, instance=comment)
        
    else:
        form = IssueCommentForm()
        
    return render(request, 'commentform.html', {'form': form})
    
        
        
