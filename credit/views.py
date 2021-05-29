from django.db.models.fields import DateField
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.http import HttpResponse

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse

from credit.forms import OrderForm
from credit.models import Order, OrderPayment

User=get_user_model()

def get_current_credit(request):
    if request.method!='GET':
        return JsonResponse({
            "is_successful":False,
            "message":"[ERROR] POST ONLY"
        })

    key = request.META.get('HTTP_AUTH')
    if User.objects.filter(key=key).exists()==False:
        return JsonResponse({
            "is_successful":False,
            "message":"Expired key. Please Login again."
        })
    user=User.objects.get(key=key)

    return JsonResponse({
        "id":user.username,
        "credit":user.credit
    })

    
    pass

def get_credit_log(request):
    if request.method!='GET':
        return JsonResponse({
            "is_successful":False,
            "message":"[ERROR] GET ONLY"
        })

    key = request.META.get("HTTP_AUTH")
    user=User.objects.get(key=key)

    if user==None:
        return JsonResponse({
            "is_successful":False,
            "message":"Expired key. Please Login again."
        })

    if CreditLog.objects.filter(user=user).exists()==False:
        return JsonResponse({
            "is_successful":False,
            "message":"CreditLog does not exist."
        })

    log=CreditLog.objects.get(user=user)

    return JsonResponse({
            "action":log.action,
            "details":log.details,
            "amount":log.amount,
            "date":log.date
    })

def home(request):
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            payment = OrderPayment.from_order(order)
            print("POST USER KEY: ")
            print(payment.order.userKey)
            return HttpResponseRedirect(reverse('payment:pay', args=[payment.pk]))
    else:
        key = request.META.get("HTTP_AUTH")

        if key==None:
            return JsonResponse({
            "is_successful":False,
            "message":"Expired key. Please Login again."
        })

        user = User.objects.get(key=key)
        
        if user==None:
            return JsonResponse({
            "is_successful":False,
            "message":"Expired key. Please Login again."
        })

        form = OrderForm(initial={
            'userKey': key,

            'name': '크레딧 충전',
            'amount': 1000,
            'buyer': user.username,
            #'addr': '주소',
            #'subaddr': '상세 주소',
            #'postcode': '우편번호',
            'email': 'DAIG@ajou.ac.kr',
            #'tel': '010-1234-5678'
        })

        return render(request, 'home.html', {'form': form})


def retry_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    payment = OrderPayment.from_order(order)

    return HttpResponseRedirect(reverse('payment:pay', args=[payment.pk]))
