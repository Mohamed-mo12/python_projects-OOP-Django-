from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import Board
from django.contrib.auth.models import User
from .models import Topic , Post
from .forms import TopicForm

def Boards(requset):
    boards = Board.objects.all()
    return render(requset,'home.html',{'boards':boards})

def board_topic(request,board_id):

    board =get_object_or_404(Board,pk= board_id)

    return render(request,'topic.html',{'board':board})


def new_topic(request,board_id):
    boards = get_object_or_404(Board,id=board_id)
    user = User.objects.first()
    form = TopicForm()
    if request.method == 'POST':
        form = TopicForm(request.POST)

        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = boards
            topic.created_by = user
            topic.save()

            post = Post.objects.create(
                message = form.cleaned_data,
                topic = topic ,
                created_by = user ,

            )
            return redirect('home')

    return render(request,'new_topic.html',{'board':boards,'form':form})























