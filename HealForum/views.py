from django.contrib import messages
from django.shortcuts import HttpResponseRedirect, redirect
from django.shortcuts import render

from HealUsers.models import Doctor
from .forms import CommentForm
from .models import Comment
from .models import Post


# Create your views here.
def table_department(request):
    if not request.user.is_anonymous:
        try:
            c = {
                "user": request.user,
                "posts": Post.objects.all(),
                "comments": Comment.objects.all(),
            }
            c["doctors"] = Doctor.objects.all()
            if request.method == "POST" and "post_btn" in request.POST:
                title = request.user.username
                context = request.POST.get("post")
                Post.objects.create(title=title, description=context, created_by=c["user"])
                c["posts"] = Post.objects.all()
                return HttpResponseRedirect("Forum/table_department.html", c)
            return render(request, "Forum/table_department.html", c)
        except:
            return render(request, "index.html")
    else:
        return render(request, "auth/login.html")


# @login_required
def create_comment(request, id):
    c = {
    }
    if request.method == "POST" and 'comment_btn' in request.POST:
        com = CommentForm(data=request.POST)


        # print("HELLOOOOOOOOOOOOO" + com)
        if com.is_valid():
            com.save(commit=False)
            com.commented_by = request.user
            com.comment = Post.objects.get(pk=id)
            # com.description_comment = request.POST.get('description_comment')
            com.save()
        # else:
        #     messages.warning(request, 'Please enter valid data for your profile')
        #     return redirect('forum')
            # Comment.objects.create(comment=Post.objects.get(pk=p_id), description="Umar is the best", commented_by=request.user)
    return redirect('forum')
