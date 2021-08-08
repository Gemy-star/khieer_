from django.http import JsonResponse
from accounts.models import User
from django.shortcuts import render
from khieer.models import Contact, HebaKheer, TechnicalSupport


def create_contact(request):
    if request.method == 'POST' and request.is_ajax:
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(
            name=name, address=address, phone=phone, message=message)
        contact.save()
        if contact.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def home_employee(request):
    user_obj = User.objects.get(pk=request.user.pk)
    request.session['user_id'] = user_obj.user_type
    return render(request, 'khieer/home-employee.html', {"user": user_obj})


def heba_kheer(request):
    if request.method == 'GET':
        return render(request, 'khieer/heba-kheer.html')
    elif request.method == 'POST' and request.is_ajax:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        national_id = request.POST.get('national_id')
        ammount = request.POST.get('ammount')
        heba_obj = HebaKheer(
            address=address, phone=phone, national_id=national_id, name=name, ammount=ammount)
        heba_obj.save()
        if heba_obj.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def add_technical(request):
    if request.method == 'GET':
        return render(request, 'main/technical-support.html')
    if request.method == 'POST' and request.is_ajax:
        name = request.POST.get('name')
        message = request.POST.get('message')
        tech_support = TechnicalSupport(name=name, message=message)
        tech_support.save()
        if tech_support.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def technical_list(request):
    problems = TechnicalSupport.objects.all()
    return render(request, 'main/technical_list.html', context={"problems": problems})
