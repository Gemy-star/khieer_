from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from django.views import View
from accounts.models import User
from django.shortcuts import render, redirect
from khieer.models import Contact, HebaKheer, TechnicalSupport, Trainer, Course, Category, Volunteer, CourseRequest
from khieer_.utils import render_to_pdf


def add_greenCourse(request):
    trainer = Trainer.objects.all()
    category = Category.objects.all()
    if request.method == 'POST' and request.FILES['logo']:
        name = request.POST.get('name')
        description = request.POST.get('description')
        start = request.POST.get('start')
        end = request.POST.get('end')
        trainer = request.POST.get('trainer')
        total = request.POST.get('total_hour')
        category = request.POST.get('cat')
        link = request.POST.get('link')
        logo = request.FILES['logo']
        fs = FileSystemStorage()
        fs.save(logo.name, logo)
        course = Course(name=name, description=description, logo=logo, link=link, duration=total, category_id=category,
                        trainer_id=trainer, start_date=start, end_date=end)
        course.save()
        if course.pk:
            return redirect('user-profile-dash')
    return render(request, 'khieer/add-course_bag.html', context={"cats": category, "trainers": trainer})


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
    elif request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        ammount = request.POST.get('ammount')
        heba_obj = HebaKheer(
            address=address, phone=phone, name=name, ammount=ammount)
        heba_obj.save()
        return redirect('heba-pay')


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


def course_request(request, pk):
    course = Course.objects.get(pk=pk)
    context = {"course": course}
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        course = CourseRequest(name=name, phone=phone, email=email, course=course)
        course.save()
        if course.pk:
            return redirect('course-list')
    return render(request, 'khieer/request_course.html', context)


def heba_payment(request):
    return render(request, 'khieer/payment-heba.html')


def courses_list(request, pk):
    context = {"courses": Course.objects.filter(category_id=pk)}
    return render(request, 'khieer/bag-list.html', context)


def technical_list(request):
    context = {"techs": TechnicalSupport.objects.all()}
    return render(request, 'khieer/technical-list.html', context)


def contact_list(request):
    context = {"contacts": Contact.objects.all()}
    return render(request, 'khieer/contact-list.html', context)


def trainers_list(request):
    context = {"trainers": Trainer.objects.all()}
    return render(request, 'khieer/trainers_list.html', context)


def volunteer_list(request):
    context = {"volunteers": Volunteer.objects.all()}
    return render(request, 'khieer/volunteer-list.html', context)


def cat_list(request):
    context = {"cats": Category.objects.all()}
    return render(request, 'khieer/all_cats.html', context)


class VolunteerAllReport(View):
    def get(self, request, *args, **kwargs):
        template = get_template('volunteer-all-pdf.html')
        needyinshow = Volunteer.objects.all()
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "خير السعوديه",
            "user": user_obj,
            "vols": needyinshow,
            "topic": "المتقدمين للتطوع ",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('volunteer-all-pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class HebaAllReport(View):
    def get(self, request, *args, **kwargs):
        template = get_template('heba-all-pdf.html')
        needyinshow = HebaKheer.objects.all()
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "خير السعوديه",
            "user": user_obj,
            "hebas": needyinshow,
            "topic": "هبات الخير ",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('heba-all-pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class CourseAllReport(View):
    def get(self, request, *args, **kwargs):
        template = get_template('course-all-pdf.html')
        needyinshow = Course.objects.all()
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "خير السعوديه",
            "user": user_obj,
            "courses": needyinshow,
            "topic": "الحقائب الخضراء ",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('course-all-pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
