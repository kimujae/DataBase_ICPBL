from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Board, Reply, Category, Photo
from .forms import BoardForm, ReplyForm, PhotoForm
from aptcomplex.models import Houseinfo
from common.models import User
from common.decorators import login_required



# 게시글 목록
@login_required
def board_list_dong(request, category_name):
    context = {}

    login_session = request.session.get('login_session', '')
    user = User.objects.get(user_id=login_session)
    building_num = user.user_house_holder.building_num
    house_info = Houseinfo.objects.filter(building_num = building_num)
    users = User.objects.get(user_house_holder__in = house_info )

    category = Category.objects.get(slug =category_name)
    board_list = Board.objects.filter(author = users , category = category).order_by("-created_date")



    page = request.GET.get("page", 1)
    paginator = Paginator(board_list, 10)
    object_list = paginator.get_page(page)
    context = {"board_list": object_list, 'category': category , 'user':user}

    if login_session =='':
        context['login_session']= False
    else :
        context['login_session']=True

    context['complaint'] = False

    return render(request, "board/board-dong.html", context)

@login_required
def board_list_complaint(request, category_name):
    login_session = request.session.get('login_session', '')
    context = {'login_session': login_session}

    user = User.objects.get(user_id=login_session)

    category = Category.objects.get(slug=category_name)
    board_list = Board.objects.filter(category=category).order_by("-created_date")

    page = request.GET.get("page", 1)
    paginator = Paginator(board_list, 10)
    object_list = paginator.get_page(page)
    context = {"board_list": object_list, 'category': category, 'user':user}
    if login_session =='':
        context['login_session']= False
    else :
        context['login_session']=True

    context['complaint'] = True
    return render(request, "board/board-dong.html", context)
@login_required
def board_list_joonggo(request, category_name):
    login_session = request.session.get('login_session', '')
    context = {'login_session': login_session}

    user = User.objects.get(user_id=login_session)

    category = Category.objects.get(slug=category_name)
    board_list = Board.objects.filter(category=category).order_by("-created_date")
    photo_list =Photo()
    for board in board_list :
        photo_list = Photo.objects.filter(post = board).order_by("-post_id")

    page = request.GET.get("page", 1)
    paginator = Paginator(board_list, 10)
    object_list = paginator.get_page(page)
    context = {"board_list": object_list,"photo_list":photo_list ,'category': category, 'user':user}
    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True

    return render(request, "board/joonggo.html", context)


@login_required
def board_list_bunsil(request, category_name):
    login_session = request.session.get('login_session', '')
    context = {'login_session': login_session}

    user = User.objects.get(user_id=login_session)

    category = Category.objects.get(slug=category_name)
    board_list = Board.objects.filter(category=category).order_by("-created_date")
    photo_list =Photo()
    for board in board_list :
        photo_list = Photo.objects.filter(post = board).order_by("-post_id")

    page = request.GET.get("page", 1)
    paginator = Paginator(board_list, 10)
    object_list = paginator.get_page(page)
    context = {"board_list": object_list,"photo_list":photo_list ,'category': category, 'user':user}
    if login_session =='':
        context['login_session']= False
    else :
        context['login_session']=True
    context['bunsil'] = True
    return render(request, "board/joonggo.html", context)


@login_required
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
@login_required
def board_create(request):
    login_session = request.session.get('login_session', '')


    user = User.objects.get(user_id = login_session)

    category_list = Category.objects.all()
    if request.method == "POST":
        #form = BoardForm(request.POST)
        #photoform = PhotoForm(request.POST)

        board = Board()
        board.subject =request.POST['subject']
        board.content = request.POST['content']
        #board = form.save(commit=False)
        board.author = user
        category = Category.objects.get(name  ='공지')
        board.category = category
        board.save()

        #for img in request.FILES['Photo']:
            # Photo 객체를 하나 생성한다.
        if request.FILES.get('img') :
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = board
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = request.FILES.get('img')
            # 데이터베이스에 저장
            photo.save()
        return redirect("board:board_list_dong" ,category_name= category)
    else:
        form = BoardForm()

    context = {"form": form, "category_list" : category_list, 'user':user}
    if login_session =='':
        context['login_session']= False
    else :
        context['login_session']=True
    return render(request, "board/board-dong-create.html", context)

@login_required
def board_create_minwon(request):
    login_session = request.session.get('login_session', '')


    user = User.objects.get(user_id = login_session)

    category_list = Category.objects.all()
    if request.method == "POST":
        #form = BoardForm(request.POST)
        #photoform = PhotoForm(request.POST)

        board = Board()
        board.subject =request.POST['subject']
        board.content = request.POST['content']
        #board = form.save(commit=False)
        board.author = user
        category = Category.objects.get(name  ='민원')
        board.category = category
        board.save()

        #for img in request.FILES['Photo']:
            # Photo 객체를 하나 생성한다.
        if request.FILES.get('img'):
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = board
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = request.FILES.get('img')
            # 데이터베이스에 저장
            photo.save()
        return redirect("board:board_list_dong" ,category_name= category)
    else:
        form = BoardForm()
    context = {"form": form, "category_list" : category_list, 'user':user}
    if login_session =='':
        context['login_session']= False
    else :
        context['login_session']=True
    return render(request, "board/board-dong-create.html", context)

@login_required
def board_create_joonggo(request):
    login_session = request.session.get('login_session', '')

    user = User.objects.get(user_id = login_session)

    category_list = Category.objects.all()
    if request.method == "POST":
        #form = BoardForm(request.POST)
        #photoform = PhotoForm(request.POST)

        board = Board()
        board.subject =request.POST['subject']
        board.content = request.POST['content']
        #board = form.save(commit=False)
        board.author = user
        category = Category.objects.get(name  ='중고')
        board.category = category
        board.save()

        #for img in request.FILES['Photo']:
            # Photo 객체를 하나 생성한다.
        if request.FILES.get('img'):
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = board
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = request.FILES.get('img')
            # 데이터베이스에 저장
            photo.save()
        return redirect("board:board_list_joonggo" ,category_name= category)
    else:
        form = BoardForm()
    context = {"form": form, "category_list" : category_list, 'user':user}

    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True
    return render(request, "board/board-dong-create.html", context)

@login_required
def board_create_bunsil(request):
    login_session = request.session.get('login_session', '')


    user = User.objects.get(user_id = login_session)

    category_list = Category.objects.all()
    if request.method == "POST":
        #form = BoardForm(request.POST)
        #photoform = PhotoForm(request.POST)

        board = Board()
        board.subject =request.POST['subject']
        board.content = request.POST['content']
        #board = form.save(commit=False)
        board.author = user
        category = Category.objects.get(name  ='분실물')
        board.category = category
        board.save()

        #for img in request.FILES['Photo']:
            # Photo 객체를 하나 생성한다.
        if request.FILES.get('img'):
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = board
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = request.FILES.get('img')
            # 데이터베이스에 저장
            photo.save()
        return redirect("board:board_list_bunsil" ,category_name= category)
    else:
        form = BoardForm()
    context = {"form": form, "category_list" : category_list, 'user':user}
    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True
    return render(request, "board/board-dong-create.html", context)
# 게시글 보기

@login_required
def board_read(request, board_id):
    login_session = request.session.get('login_session', '')


    user = User.objects.get(user_id=login_session)
    context ={}
    board = get_object_or_404(Board, pk=board_id)

    if Photo.objects.filter(post = board) :
        photo = Photo.objects.get(post=board)
        context["photo"] = photo

    reply_list = Reply.objects.filter(board=board.id).order_by("-created_date")
    context["board"] =board
    context["reply_list"] = reply_list
    context["user"] = user

    if login_session =='':
        context['login_session']= False
    else :
        context['login_session']=True
    return render(request, "board/test-post-board-dong.html", context)


# 게시글 수정
@login_required
def board_update(request, board_id):
    login_session = request.session.get('login_session', '')


    user = User.objects.get(user_id=login_session)

    board = get_object_or_404(Board, pk=board_id)
    if board.author != user:
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
    context = {"form": form, "board": board, 'user':user}
    if login_session =='':
        context['login_session']= False
    else :
        context['login_session']=True
    return render(request, "board/update.html", context)


# 게시글 삭제

@login_required
def board_delete(request, board_id):
    login_session = request.session.get('login_session', '')


    user = User.objects.get(user_id=login_session)

    board = get_object_or_404(Board, pk=board_id)
    if board.author != user:
        messages.error(request, "삭제 권한이 없습니다.")
        return redirect("board:board_read", board_id=board.id)
    board.delete()
    messages.success(request, "글을 삭제하였습니다.")
    return redirect("board:board_list")


# 댓글 등록

@login_required
def reply_create(request, board_id):
    login_session = request.session.get('login_session', '')
    context = {'login_session': login_session}

    user = User.objects.get(user_id=login_session)

    board = get_object_or_404(Board, pk=board_id)
    reply_list = Reply.objects.filter(board=board.id).order_by("-created_date")
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = user
            reply.board = board
            reply.save()
            return redirect("board:board_read", board_id=board.id)
    else:
        form = ReplyForm()
    context = {"form": form, "board": board, "reply_list": reply_list, 'user':user}
    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True
    return render(request, "board/read.html", context)


# 댓글 수정
@login_required
def reply_update(request, board_id, reply_id):
    login_session = request.session.get('login_session', '')


    user = User.objects.get(user_id=login_session)

    board = get_object_or_404(Board, pk=board_id)
    reply = get_object_or_404(Reply, pk=reply_id)
    if reply.author != user:
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
    context = {"form": form, "board": board, "reply": reply, 'user':user}
    if login_session =='':
        context['login_session']= False
    else :
        context['login_session']=True
    return render(request, "board/read.html", context)


# 게시글 삭제
@login_required
def reply_delete(request, board_id, reply_id):
    login_session = request.session.get('login_session', '')
    context = {'login_session': login_session}
    if login_session =='':
        context['login_session']= False
    else :
        context['login_session']=True
    user = User.objects.get(user_id=login_session)

    board = get_object_or_404(Board, pk=board_id)
    reply = get_object_or_404(Reply, pk=reply_id)
    if reply.author != request.user:
        messages.error(request, "삭제 권한이 없습니다.")
        return redirect("board:board_read", board_id=board.id)
    reply.delete()
    messages.success(request, "댓글을 삭제하였습니다.")
    return redirect("board:board_read", board_id=board.id)

