from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'amadonStore/index.html')

def buy(request):
    product_id = request.POST['product_id']
    product_count = request.POST['quantity']
    if (product_id == '1001'):
        price = 19.99
    elif (product_id == '1002'):
        price = 29.99
    elif (product_id == '1003'):
        price = 4.99
    elif (product_id == '1004'):
        price = 49.99
    else:
        price = 0
    transaction_amount = int(product_count) * price
    try:
        request.session['num_items'] += int(product_count)
        request.session['last_charge_amount'] = transaction_amount
        request.session['total_spend'] += transaction_amount
    except:
        request.session['num_items'] = int(product_count)
        request.session['last_charge_amount'] = transaction_amount
        request.session['total_spend'] = transaction_amount
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'amadonStore/checkout.html')
