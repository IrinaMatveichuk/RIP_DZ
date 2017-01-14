from django.shortcuts import render, redirect
from comp_shop.forms import *
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.views.decorators.csrf import ensure_csrf_cookie


class ComputerList(View):
    def get(self, request):
        try:
            order = Order.objects.get(user_id=request.user.id)
        except:
            order = []
        computers = Computer.objects.all()
        paginator = Paginator(computers, 3)  # Show 3 computers per page
        page = request.GET.get('page')
        try:
            computers = paginator.page(page)
        except PageNotAnInteger:
            computers = paginator.page(1)
        except EmptyPage:
            computers = paginator.page(paginator.num_pages)
        return render(request, 'computer_list.html',
                      {'computers':  computers, 'order': order})


def create_computer(request):
    if request.method == 'POST':
        form = CreateComputerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(True)
            serial_num = request.POST.get('serial_num')
            comp = Computer.objects.get(serial_num=serial_num)
            return render(request, 'computer.html', {'comp': comp})
    else:
        form = CreateComputerForm()

    return render(request, 'create_computer.html', {'form': form})


def contacts(request):
    return render(request, 'contacts.html')


def signin(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponse('true')
        else:
            return HttpResponse('false')


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


def signup_success(request):
    return render(request, 'signup_success.html')


def user_page(request):
    return render(request, 'user.html')


def logout_view(request):
    redirect = request.GET.get('main_page', '/')
    auth.logout(request)
    return HttpResponseRedirect(redirect)


class ComputerView(View):
    def get(self, request, id):
        users = []
        computer = Computer.objects.get(id=id)
        orders = computer.order_set.all()
        try:
            ord = Order.objects.get(user_id=request.user.id)
        except:
            ord = []
        for order in orders:
            users.append(User.objects.get(id=order.user_id_id))
        return render(request, 'computer.html',
                      {'comp': computer, 'users': users, 'order': ord})


@ensure_csrf_cookie
def order_add(request):
    if request.is_ajax():
        comp_id = request.POST.get('comp_id')
        user_id = request.user.id
        date_ord = datetime.now()
        comp = Computer.objects.get(id=comp_id)  # комп
        try:
            order = Order.objects.get(user_id_id=user_id)  # заказ
        except:
            o = Order(order_date=date_ord, user_id_id=user_id)
            o.save()
            order = Order.objects.get(user_id_id=user_id)
        order.computers.add(comp)
        return HttpResponse('ok')
    else:
        return HttpResponse('bad')


@ensure_csrf_cookie
def order_delete(request):
    if request.is_ajax():
        comp_id = request.POST.get('comp_id')
        user_id = request.user.id
        comp = Computer.objects.get(id=comp_id)  # комп
        order = Order.objects.get(user_id_id=user_id)  # заказ
        order.computers.remove(comp)
        return HttpResponse('ok')
    else:
        return HttpResponse('bad')


def delete_computer(request):
    if request.is_ajax():
        comp_id = request.POST.get('comp_id')
        comp = Computer.objects.get(id=comp_id)
        comp.delete()
        return HttpResponse('ok')
    else:
        return HttpResponse('bad')
