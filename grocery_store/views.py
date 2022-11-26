import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.renderers import JSONRenderer

from grocery_store.forms import EmployeeRegisterForm, FeedbackForm
from grocery_store.models import Supplier, Employee, Game, Feedback
from rest_framework import generics

from requests import get

from grocery_store.serializers import EmployeeSerializer, GameSerializer, TimeFromOpenweather, \
    TimeFromOpenweatherSerializer, FeedbackSerializer


def homepage(request):
    context = {'greeting': 'Welcome to homepage!!!'}
    return render(request, 'homepage.html', context)


def store_homepage(request):
    context = {'greeting': 'Welcome to store\'s homepage!!!'}
    return render(request, 'store_homepage.html', context)


def login_page(request):
    if request.method == 'GET':
        return render(request, 'store/login.html')
    elif request.method == 'POST':
        data = request.POST
        input_login = data.get('input_login')
        input_password = data.get('input_password')
        user = authenticate(username=input_login, password=input_password)
        context = None
        if user:
            login(request, user)
        else:
            context = {'error': 'Invalid username or password'}
        return render(request, 'store/login.html', context=context)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_page'))


@login_required(login_url=login_page)
def auth_page(request):
    return HttpResponse(
        '<h2>You can see this page cause you are authorized.</h2>'
    )


def employee_page(request):
    if request.method == "GET":
        context = {
            'form': EmployeeRegisterForm()
        }
        return render(request, 'store/employee_add.html', context=context)
    elif request.method == 'POST':
        data = request.POST
        employee_obj = EmployeeRegisterForm(data)
        employee_obj.save()
        context = {
            'form': EmployeeRegisterForm(),
            'success_msg': 'Employee added'
        }
        return render(request, 'store/employee_add.html', context=context)


@login_required(login_url=login_page)
def feedback_page(request):
    if request.method == "GET":
        context = {
            'form': FeedbackForm()
        }
        return render(request, 'store/feedback_page.html', context=context)
    elif request.method == 'POST':
        data = request.POST
        files = request.FILES
        feedback_obj = FeedbackForm(data, files)
        feedback_obj.save()
        context = {
            'form': FeedbackForm(),
            'success_msg': 'Feedback added'
        }
        return render(request, 'store/feedback_page.html', context=context)


def supplier_info(request):
    if request.method == 'GET':
        return render(request, 'store/supplier_info.html')
    elif request.method == 'POST':
        data = request.POST
        input_id = data.get('input_supplier_id')
        if list(Supplier.objects.values())[int(input_id) - 1]:
            context = {
                'supplier_info': list(Supplier.objects.values())[int(input_id)]
            }
        else:
            context = {'error': 'Invalid supplier\'s id'}
        return render(request, 'store/supplier_info.html', context=context)


# Views for HomeWork 7


def time_encode(request, *args):
    city = request.GET.get('city')
    key = "fcc97445e7b8129db774b580d9e6958d"
    weather_api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}&units=metric'
    response: dict = get(weather_api).json()
    if response.get('cod') == '404':
        return HttpResponse(f'<script>alert("City {city} does not exist!");</script>')
    api_time = response.get('dt')
    time_response = datetime.datetime.utcfromtimestamp(api_time).strftime('%H:%M:%S')
    model_ = TimeFromOpenweather(time_response)
    model_sr = TimeFromOpenweatherSerializer(model_)
    json_response = JSONRenderer().render(model_sr.data)
    return HttpResponse(json_response)


class EmployeeInfoView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class FeedbackListView(generics.ListAPIView):
    queryset = Feedback.objects.all().order_by('-created')
    serializer_class = FeedbackSerializer


class FeedbackGetView(generics.RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackCreateView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated,)


class FeedbackDeletingView(generics.RetrieveDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAdminUser,)


class GameView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = 'user'
