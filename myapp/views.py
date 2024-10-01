###import point###
from django.shortcuts import render
from django.http import HttpResponse

def homework2(request, username):
    print(username)
    # return HttpResponse ("test~")
    return render(request,"show.html",locals())
###import point###
import random
def lotto1(request):
    #return HttpResponse("wait a moment")
    num_listg = random.sample(range(1,43),5)
    print(num_listg)
    return render(request,"lotto1.html",locals())

def lotto2(request):
    
    random_num_lists=[] # 創建一個空的列表，用來存放每組樂透號碼
    for n in range(1,6):
        num_listg = random.sample(range(1,43),5) # 隨機生成一組5個號碼，使用random.sample來確保號碼不重複
        random_num_lists.append(num_listg)
    print(random_num_lists)
    return render(request,"lotto2.html",locals())

def index(request):
    print("首頁index")
    #return HttpResponse("wait a moment")
    return render(request,"index.html",locals())

def index2(request):
    print("首頁index2")
    #return HttpResponse("wait a moment")
    return render(request,"index2.html",locals())

def appointment_view(request):
    # 處理邏輯
    return render(request, 'appointment.html')
def select_department_view(request):
    # 處理邏輯
    return render(request, 'select_department.html')


###import point###
from django.http import JsonResponse
import json
###import point###
from django.shortcuts import render, redirect
###import point###
from django.views.decorators.csrf import csrf_exempt  # 导入 csrf_exempt
###import point###
from django.test import TestCase
from django.urls import reverse


number = 0 #主線
current_number = 0 #協助主線更新用

def current_number(request):
    # 該返回畫面只在重整頁面時更新，但不影響後台即時刷新
    return JsonResponse({'current_number': number})

def lcd_control(request):
    # 渲染顯示數字的頁面
    return render(request, 'lcd_control.html')

def increase_button(request):
    #進入此頁面後global number+1
    global current_number
    global number
    # number上限為5
    if number < 5:
        current_number = number + 1
        number = current_number
    else:
        current_number = 0
        number = 0
    return render(request, 'increase_button.html')#按鍵後導回原本的畫面

def increase_forESP8266(request):
    #進入此頁面後global number+1
    global current_number
    global number
    # 如果 current_number 或 number 小于 特定數字，则加 1；否则重置为 0
    if number < 5:
        current_number = number + 1
        number = current_number
    else:
        current_number = 0
        number = 0
    return JsonResponse({'current_number': number})#按鍵後只顯示當前number

def clear_number(request):
    #進入此頁面後號碼歸0
    global current_number 
    global number
    current_number=0
    number = 0
    return HttpResponse("號碼已歸0")

