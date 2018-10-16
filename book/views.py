from django.shortcuts import render,redirect
from.forms import Bookform
from.forms import UserForm
from.forms import UsersForm
# Create your views here..
from django.http import HttpResponse, HttpResponseRedirect
from.models import Book
from django.contrib.auth.hashers import make_password,check_password
from datetime import datetime
from.models import User

from django.contrib import auth

def insert(request):
    #insert
    Book.objects.create(
        bookName='',
        bookRate='',
        bookDate= datetime.now()
    )

    return HttpResponse("添加成功 ")


def update(request):
    # aa = Book.objects.filter(bookRate='9.2')[0]
    # aa.bookRate = '9.4'
    # aa.save()
    Book.objects.filter(bookName='').update(bookDate= '')
    # Book.objects.all().update(bookDate= '2018-08-13')
    return HttpResponse("修改成功 ")


def search(request):
    book = Book.objects.all( )
    for i in book:
        print(i.bookName)
        print(i.bookRate)
        print(i.bookDate)

    return render(request,'book/dinx.html',{'book444':book})

def delete(request):
    Book.objects.filter(bookName= '').delete()
    return HttpResponse("删除成功 ")

def delete_post(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/book/search')
    # elif request.method == 'POST':
    #     book_id = int(request.POST['book_id'])
    #     Book.objects.filter(id=book_id).delete()
    elif request.method =='POST':
        book_Name = request.POST['book_Name']
        Book.objects.filter(bookName=book_Name).delete()

        return HttpResponseRedirect('/book/search')

def create_post(request):
    if request.method == 'GET':
        return ('这是GET方法')

    elif request.method == 'POST':
        aa = Bookform(request.POST) #aa 包含提交的数据
        if aa.is_valid():
            Book.objects.create(
                bookName = aa.cleaned_data['book_name'],
                bookRate = aa.cleaned_data['book_rate'],
                # bookDate = aa.cleaned_data['book_date']
            )
            # return HttpResponse('POST方法创建成功')
            return HttpResponseRedirect('/book/search')

        else:
            return HttpResponse('创建失败1')


# def create(request):
#     print(request.method)
#     try:
#         return render(request, 'book/create.html')
#     except:
#         return HttpResponse('创建失败')


def create(request):
    # username = request.session.get('name', None)
    # if username is None:
    #     request.session['name'] = 'zhang3'
        username = request.session.get('username', None)
        if username is None:
            return HttpResponseRedirect('/book/login')
        # resp = render(request, 'book/create.html', {'username': username})
        # return resp

        else:
            resp = render(request, 'book/create.html', {'name':username})
            return resp


# def login(request):
#     try:
#         return render(request,'book/denglu.html')
#     except:
#         return HttpResponse('登录界面打开失败')

def login(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id',None)
        if user_id is None:
            return render(request,'book/denglu.html')
        else:
            return HttpResponseRedirect('/book/create')
    elif request.method == 'POST':
        print('post..',request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            users = User.objects.filter(username=username)
            print('123')
            if users:
                users = users[0]
                ps = check_password(
                    form.cleaned_data['password'],
                    users.password
                )
                if ps:
                    request.session['user_id'] = users.id
                    request.session['username'] = username
                    return HttpResponseRedirect('/book/create')
            else:
                    return render(request,'book/denglu.html',{'mes':'账号或密码错误'})
        else:
           return render(request, 'book/denglu.html')






def register(request):
    if request.method == 'GET':
        return render(request, 'book/zhuce.html')
    elif request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
                if User.objects.filter(username=form.cleaned_data['username']):
                    return render(request, 'book/zhuce.html', {'mes': '该用户已存在'})
                a = form.cleaned_data['password']
                b = form.cleaned_data['password2']
                if a == b:
                    User.objects.create(
                    username = form.cleaned_data['username'] , # cleaned_data类型是字典，里面是提交成功后的信息
                    password = make_password(form.cleaned_data['password'])
                    )
                    return HttpResponseRedirect('/book/register_in')
                else:
                    return render(request, 'book/zhuce.html', {'mes': '两次密码不一致，请重新输入'})
        else:
            return render(request, 'book/zhuce.html')

    return render(request, 'book/zhuce.html')



def register_in(request):
    return render(request, 'book/chenggong.html')

def logout(request):
    response = HttpResponseRedirect('/book/login')
    response.delete_cookie('sessionid')
    return response

