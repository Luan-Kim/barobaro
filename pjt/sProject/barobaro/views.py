from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import korean_food, chinese_food, japanese_food, User


def index(request):
    msg = 'My Message'
    return render(request, 'barobaro/index.html', {'message': msg})
    # template = loader.get_template('delivery/index.html')
    # context = {
    #         'latest_question_list': "test",
    # }
    # return HttpResponse(template.render(context, request))


def register(request):  # 회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'barobaro/register.html')

    elif request.method == "POST":
        username = request.POST.get('username', None)  # 딕셔너리형태
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        res_data = {}
        if not (username and password and re_password):
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User(username=username, password=make_password(password))
            user.save()
            return redirect('/')
        return render(request, 'barobaro/register.html', res_data)  # register를 요청받으면 register.html 로 응답.

    # if request.method == 'POST':
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         # user.set_password(form.cleaned_data['password'])
    #         user.password = make_password(form.cleaned_data['password'])
    #         user.status = 1
    #         user.save()
    #         # id = user.username
    #         return render(request, 'barobaro/index.html', {'form': form})
    # else:
    #     form = UserForm()
    # return render(request, 'barobaro/register.html', {'form': form})


def login(request):
    response_data = {}

    if request.method == "GET":
        return render(request, 'barobaro/login.html')

    elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('password', None)

        if not (login_username and login_password):
            response_data['error'] = "아이디와 비밀번호를 모두 입력해주세요!"
        else:
            try:
                user = User.objects.get(username=login_username)
            except User.DoesNotExist:
                return HttpResponse('존재하지 않는 사용자입니다.')
            if check_password(login_password, user.password):
                request.session['user'] = user.username
                return redirect('/')

            else:
                response_data['error'] = "비밀번호가 틀렸습니다."
        return render(request, 'barobaro/login.html', response_data)

    # if request.method == "POST":
    #     form = LoginForm(request.POST)
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = auth.authenticate(request, username=username, password=password)
    #     if user is not None:
    #         auth.login(request, user)
    #         return redirect('/')
    #     else:
    #         return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    # else:
    #     form = LoginForm()
    #     return render(request, 'barobaro/login.html', {'form': form})


def logout(request):
    # auth.logout(request)
    # return redirect('/')
    if request.session.get('user'):
        del (request.session['user'])
    return redirect('/')


def about(request):
    msg = 'My Message'
    return render(request, 'barobaro/about.html', {'message': msg})


def kor_food(request):
    Restaurant_name = korean_food.objects.all()
    context = {'Restaurant_name': Restaurant_name}
    return render(request, 'barobaro/korfood.html', context)


def cn_food(request):
    Restaurant_name = chinese_food.objects.all()
    context = {'Restaurant_name': Restaurant_name}
    return render(request, 'barobaro/cnfood.html', context)


def jp_food(request):
    Restaurant_name = japanese_food.objects.all()
    context = {'Restaurant_name': Restaurant_name}
    return render(request, 'barobaro/jpfood.html', context)


def order(request):
    msg = 'My Message'
    return render(request, 'barobaro/order.html', {'message': msg})


def menu(request):
    msg = 'My Message'
    return render(request, 'barobaro/menu.html', {'message': msg})
