from django.shortcuts import render

# Create your views here.

def history_order(request):
    return render(request, 'order_app/historyorder.html')

def one_order(request):
    return render(request, 'order_app/oneorder.html')

def order(request):
    return render(request, 'order_app/order.html')