from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Board, Reply, Category
from .forms import BoardForm, ReplyForm
from aptcomplex.models import Houseinfo
from common.models import User


def main(request):
    return render(request, "board/board-dong.html")

# 게시글 목록
@login_required(login_url="common:login")
def board_list(request, category_name):
    login_session = request.session.get('login_session', '')
    context = {'login_session': login_session}
    user = User.objects.get(user_id=login_session)
    building_num = user.user_house_holder.building_num
    house_info = Houseinfo.objects.filter(building_num = building_num)
    users = User.objects.get(user_house_holder__in= house_info)

    category = Category.objects.get(slug =category_name)
    board_list = Board.objects.filter(author = users , category = category).order_by("-created_date")



    page = request.GET.get("page", 1)
    paginator = Paginator(board_list, 10)
    object_list = paginator.get_page(page)
    context = {"board_list": object_list, 'category': category}

    return render(request, "board/board-dong.html", context)










def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류',
        board_list = Board.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        board_list = Board.objects.filter(category=category)

    return render(
        request,
        'board/post_list.html',
        {
            'board_list': Board.objects.filter(category=category),
            'categories': Category.objects.all(),
            'no_category_post_count': Board.objects.filter(category=None).count(),
            'category': category
        }
    )

# 게시글 등록
@login_required(login_url="common:login")
def board_create(request):
    login_session = request.session.get('login_session', '')
    user = User.objects.get(user_id = login_session)

    category_list = Category.objects.all()
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = user
            selected_category = get_object_or_404(Category, pk = request.POST.get('selected_category'))
            board.category = selected_category
            board.save()
            return redirect("board:board_list" , category_name = board.category.name)
    else:
        form = BoardForm()
    context = {"form": form, "category_list" : category_list}
    return render(request, "board/create.html", context)


# 게시글 보기
@login_required(login_url="common:login")
def board_read(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    reply_list = Reply.objects.filter(board=board.id).order_by("-created_date")
    context = {"board": board, "reply_list": reply_list}
    return render(request, "board/read.html", context)


# 게시글 수정
@login_required(login_url="common:login")
def board_update(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if board.author != request.user:
        messages.error(request, "수정 권한이 없습니다.")
        return redirect("board:board_read", board_id=board.id)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.save()
            messages.success(request, "글을 수정하였습니다.")
            return redirect("board:board_read", board_id=board.id)
    else:
        form = BoardForm(instance=board)
    context = {"form": form, "board": board}
    return render(request, "board/update.html", context)


# 게시글 삭제
@login_required(login_url="common:login")
def board_delete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if board.author != request.user:
        messages.error(request, "삭제 권한이 없습니다.")
        return redirect("board:board_read", board_id=board.id)
    board.delete()
    messages.success(request, "글을 삭제하였습니다.")
    return redirect("board:board_list")


# 댓글 등록
@login_required(login_url="common:login")
def reply_create(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    reply_list = Reply.objects.filter(board=board.id).order_by("-created_date")
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.board = board
            reply.save()
            return redirect("board:board_read", board_id=board.id)
    else:
        form = ReplyForm()
    context = {"form": form, "board": board, "reply_list": reply_list}
    return render(request, "board/read.html", context)


# 댓글 수정
@login_required(login_url="common:login")
def reply_update(request, board_id, reply_id):
    board = get_object_or_404(Board, pk=board_id)
    reply = get_object_or_404(Reply, pk=reply_id)
    if reply.author != request.user:
        messages.error(request, "수정 권한이 없습니다.")
        return redirect("board:board_read", board_id=board.id)
    if request.method == "POST":
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.save()
            return redirect("board:board_read", board_id=board.id)
    else:
        form = ReplyForm()
    context = {"form": form, "board": board, "reply": reply}
    return render(request, "board/read.html", context)


# 게시글 삭제
@login_required(login_url="common:login")
def reply_delete(request, board_id, reply_id):
    board = get_object_or_404(Board, pk=board_id)
    reply = get_object_or_404(Reply, pk=reply_id)
    if reply.author != request.user:
        messages.error(request, "삭제 권한이 없습니다.")
        return redirect("board:board_read", board_id=board.id)
    reply.delete()
    messages.success(request, "댓글을 삭제하였습니다.")
    return redirect("board:board_read", board_id=board.id)

