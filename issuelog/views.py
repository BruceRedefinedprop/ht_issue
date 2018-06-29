from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Issue, Comment
from .forms import  IssuePostForm, IssueCommentForm
from django.contrib.auth.decorators import login_required

@login_required
def get_issues(request):
    """
    get a list of issue were published prior to now and
    render them to the 'issueposts.html' template
    """
    issues = Issue.objects.exclude(issue_status = "closed").order_by('-published_date')
    print(issues)
    return render(request, 'issueposts.html', {'issues': issues})

@login_required    
def issue_detail(request, pk):
    """
    return a singe post based on post.id from issueposts.html's
    list.
    """
    issue = get_object_or_404(Issue, pk=pk)
    issue.save()
    return render(request, "issue_detail.html", {'issue': issue})

@login_required
def create_or_edit_issue(request, pk=None):
    issue = get_object_or_404(Issue, pk=pk) if pk else None
    if request.method == "POST":
        form = IssuePostForm(request.POST, request.FILES, instance=issue)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.author = request.user  # update for data
            if pk:
                issue.rating = ((issue.rating * issue.votes) - issue.rating + int(request.POST["rating"]))/issue.votes
            else:
                issue.rating = request.POST["rating"]
                issue.votes = 1
                issue.ht_product = request.POST["ht_product"]
            form.save()  # save form to DB
            print("reached save")
            print("rating value: {0}".format(request.POST["rating"]))
            print("rating value: {0}".format(request.POST["ht_product"]))
            return redirect(issue_detail, issue.pk)
        else:
            print("being redirect without saving")
            return redirect(get_issues)
    elif issue:
            print('post being edited')
            print("elif post")
            print("{0}--{1}--{2}".format(issue.id, issue.title, issue.content))
            print(issue.rating)
            form = IssuePostForm(data = {'title': issue.title, 'content': issue.content, 'published_date': issue.published_date, 'tag' : issue.tag, 'image': issue.image, 'ht_product': issue.ht_product}, instance=issue)  
            return render(request, 'issuepostform.html', {'form': form, 'rate' : issue.rating})    
            
    else:
            # new post
            print('new post')
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
            comment.rating = request.POST["rating"]
            print("comment rating {0}".format(comment.rating))
            issue = comment.issue
            if pk:
                issue.rating = ((issue.rating * issue.votes) - issue.rating + int(request.POST["rating"]))/issue.votes
                issue.save()
            else:
                comment.rating = int(request.POST["rating"])
                issue.votes +=  1
                issue.rating = (issue.rating + comment.rating)/issue.votes
                issue.save()
            form.save()
            return redirect(issue_detail, comment.issue.pk)
    elif comment:
        form = IssueCommentForm({'comment': comment.comment, 'issue': comment.issue}, instance=comment)
        return render(request, 'issuepostform.html', {'form': form, 'rate' : comment.rating }) 
    else:
        form = IssueCommentForm()
    return render(request, 'commentform.html', {'form': form})
    
@login_required
def del_comment(request, pk):  
    cur_comment =  get_object_or_404(Comment, pk=pk)
    issue = cur_comment.issue
    issue.rating = ((issue.rating * issue.votes) - cur_comment.rating )/(issue.votes-1)
    issue.votes = issue.votes - 1
    issue.save()
    cur_comment.delete()
    return render(request, "issue_detail.html", {'issue': issue})
    
        
