from django.shortcuts import render,redirect
from banking_system.urls import *
from banking.models import customer as cform
from banking.models import transfer as tform
from datetime import datetime
from django.db.models import F
from django.http import JsonResponse
# Create your views here.
def About(request):
    return render(request, 'about.html')
def customerForm(request):
    print(request.POST)
    cust=request.POST.get('cust')
    acc=request.POST.get('acc')
    email=request.POST.get('email')
    balance=request.POST.get('balance')
    cform.objects.create(name=cust,email=email,account_no=acc,balance=balance)



    return render(request,'customerForm.html')
def transferForm(request):
    print(request.POST)
    payer=request.POST.get('payer')
    payee=request.POST.get('payee')
    amount=request.POST.get('amount')
    tform.objects.create(payer=payer,payee=payee,amount=amount)


    return render(request,'transferForm.html')
def history(request):
    return render(request,'history.html')
def view(request):
    return render(request,'view.html',)
def transaction(request):
    if request.method =="POST":
        receiver= request.POST.get('payee')
        money = request.POST.get('amount')
        sender = request.POST.get('payer')
        print(receiver,money,sender)
        query2 = cform.objects.get(account_no = sender)
        print(query2)
        query2.balance= F('balance')- money
        query2.save()
        query1 = cform.objects.get(account_no= receiver)
        print(query1)

        query1.balance= F('balance')+ money
        query1.save()
        result = cform.objects.get(account_no = sender)
        transact = tform()
        transact.payer = sender
        transact.amount = money
        transact.payee = receiver
        transact.save()
        return render(request, 'about.html')
    all_entries = tform.objects.all()
    context = {
            "history" : all_entries
        }
    return render(request, 'transaction.html', context)

def details(request):
    details=cform.objects.all().values()
    context= {
        "details":list(details)
    }
    print(context)
    # return render(request, 'view.html', context)
    return JsonResponse(context)
def transfer(request):
    transaction=tform.objects.all().values()
    context= {
        "transaction":list(transaction)
    }
    print(context)
    # return render(request, 'history.html', context)
    return JsonResponse(context)


