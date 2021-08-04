from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from django.core import serializers
from django.core.files.storage import FileSystemStorage


# def check_email(request):
#     if request.method == 'POST' and request.is_ajax:
#         email = request.POST.get('email')
#         user_obj = User.objects.get(email=email)
#         if user_obj.pk:
#             return JsonResponse(
#                 {"status": 1, "user_name": user_obj.first_name, "user_id": user_obj.pk, "user_type": user_obj.user_type,
#                  "email": user_obj.email})
#         else:
#             return JsonResponse({"status": 0})


# def loginPage(request):
#     if request.method == 'POST' and request.is_ajax:
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user = authenticate(request, username=email, password=password)

#         if user is not None:
#             if user.user_type == 2:
#                 login(request, user)
#                 return JsonResponse({"status": 'done', "user_pk": user.pk})
#             else:
#                 login(request, user)
#                 return JsonResponse({"status": 'done', "user_pk": user.pk})


#         else:
#             return JsonResponse({"status": 'Username OR password is incorrect'})

#     context = {}
#     return render(request, 'accounts/login.html', context)


# def logoutUser(request):
#     logout(request)
#     return redirect('login')


# def register_trainer(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         user = User.objects.create_trainer(email=email, first_name=first_name, last_name=last_name,
#                                            address=address, password=password, phone=phone)
#         if user is not None:
#             login(request, user)
#             return redirect('home-page')


#         else:
#             messages.add_message(request, messages.error, 'Please Review Your Data Failed To Register')
#     context = {}
#     return render(request, 'accounts/register-trainer.html', context)


# def register_trainee(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         user = User.objects.create_trainee(email=email, first_name=first_name, last_name=last_name,
#                                            address=address, password=password, phone=phone)
#         if user is not None:
#             login(request, user)
#             return redirect('home-page')


#         else:
#             messages.add_message(request, messages.error, 'Please Review Your Data Failed To Register')
#     context = {}
#     return render(request, 'accounts/register-trainee.html', context)


# def register_permier_emp(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         user = User.objects.create_permier_employeeuser(email=email, first_name=first_name, last_name=last_name,
#                                                         address=address, password=password, phone=phone)
#         if user is not None:
#             if user.user_type == 2:
#                 login(request, user)
#                 return redirect('home-employee', user.pk)
#             elif user.user_type == 3:
#                 login(request, user)
#                 return redirect('home-employee', user.pk)
#             elif user.user_type == 1:
#                 login(request, user)
#                 return redirect('home-employee', user.pk)
#             else:
#                 login(request, user)
#                 return redirect('home-page', user.pk)


#         else:
#             messages.add_message(request, messages.error, 'Please Review Your Data Failed To Register')
#     context = {}
#     return render(request, 'accounts/register.html', context)


# def register_secondary_empolyee(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         user = User.objects.create_secondary_empuser(email=email, first_name=first_name, last_name=last_name,
#                                                      address=address, password=password, phone=phone)
#         if user is not None:
#             login(request, user)
#             return redirect('home-page')
#         else:
#             messages.add_message(request, messages.error, 'Please Review Your Data Failed To Register')
#     context = {}
#     return render(request, 'accounts/register-employee.html', context)


# def register_helper_employee(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         user = User.objects.create_helper_empuser(email=email, first_name=first_name, last_name=last_name,
#                                                   address=address, password=password, phone=phone)
#         if user is not None:
#             login(request, user)
#             return redirect('home-page')
#         else:
#             messages.add_message(request, messages.error, 'Please Review Your Data Failed To Register')
#     context = {}
#     return render(request, 'accounts/register-helper-employee.html', context)


# def register_needy(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         user = User.objects.create_Needy_user(email=email, first_name=first_name, last_name=last_name,
#                                               address=address, password=password, phone=phone)
#         if user is not None:
#             login(request, user)
#             return redirect('home-page')
#         else:
#             messages.add_message(request, messages.error, 'Please Review Your Data Failed To Register')
#     context = {}
#     return render(request, 'accounts/register-needy.html', context)


# def register_volunteer(request):
#     if request.method == 'POST' and request.FILES['cv']:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         filed = request.POST.get('filed')
#         study = request.POST.get('study')
#         goals = request.POST.get('goals')
#         bithdate = request.POST.get('bithdate')
#         skills = request.POST.get('skills')
#         time = request.POST.get('time')
#         place = request.POST.get('place')
#         user = User.objects.create_volunteer(email=email, first_name=first_name, last_name=last_name,
#                                              address=address, password=password, phone=phone)
#         cv = request.FILES['cv']
#         gender = request.POST.get('gender')
#         fs = FileSystemStorage()
#         fs.save(cv.name, cv)
#         job = request.POST.get('job')
#         desc = request.POST.get('specific')
#         vol_profile = VolunteerProfile(job=job, desc=desc, volunteer=user, gender=gender, birthdate=bithdate,
#                                        time=time, place=place, cv=cv, skills=skills, study=study, goals=goals,
#                                        filed=filed)
#         vol_profile.save()
#         if user is not None:
#             login(request, user)
#             return redirect('home-page')
#         else:
#             messages.add_message(request, messages.error, 'Please Review Your Data Failed To Register')
#     context = {}
#     return render(request, 'accounts/register-volunteer.html', context)


# def register_donator(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         user = User.objects.create_Donator_user(email=email, first_name=first_name, last_name=last_name,
#                                                 address=address, password=password, phone=phone)
#         if user is not None:
#             login(request, user)
#             return redirect('home-page')
#         else:
#             messages.add_message(request, messages.error, 'Please Review Your Data Failed To Register')
#     context = {}
#     return render(request, 'accounts/register-donator.html', context)


# def user_profile(request):
#     user_obj = User.objects.get(pk=request.user.pk)
#     if user_obj.user_type == 7:
#         profile = VolunteerProfile.objects.get(volunteer=user_obj)
#         return render(request, 'accounts/user-profile.html', context={"profile": profile})
#     else:
#         return render(request, 'accounts/user-profile.html')


# def user_profile_dash(request):
#     return render(request, 'accounts/profile-dash.html')


# def get_notification(request):
#     if request.method == 'POST' and request.is_ajax:
#         pk = request.POST.get('user_id')
#         user_obj = User.objects.get(pk=pk)
#         users = User.objects.filter(pk=pk)
#         user_json = serializers.serialize('json', users)
#         if user_obj.user_type == 5:
#             national_id = request.POST.get('national_id')
#             neddy_obj = Needy.objects.get(national_id=national_id)
#             needy = Needy.objects.filter(national_id=national_id)
#             needy_json = serializers.serialize('json', needy)
#             if neddy_obj.enablity == 1:
#                 bags = CourseBag.objects.filter(paymentcoursebag__needy__national_id__in=national_id)
#                 coorse_obi = Courses.objects.filter(tamkeen__national_id__in=national_id)
#                 course_json = serializers.serialize('json', coorse_obi)
#                 return JsonResponse({"needy": needy_json, "courses": course_json, "bags": bags},
#                                     content_type='application/json')
#             else:
#                 bags = CourseBag.objects.filter(paymentcoursebag__needy__national_id__in=national_id)
#                 return JsonResponse({"needy": neddy_obj, "bags": bags}, content_type='application/json')
#         elif user_obj.user_type == 6:
#             payment = Payment.objects.filter(helper=user_obj)
#             payment_json = serializers.serialize('json', payment)
#             return JsonResponse({"payment": payment_json}, content_type='application/json')
#         elif user_obj.user_type == 7:
#             return JsonResponse({"user": user_json}, content_type='application/json')
#         else:
#             found = Foundation.objects.filter(employee=user_obj)
#             found_json = serializers.serialize('json', found)
#             return JsonResponse({"found": found_json}, content_type='application/json')

# def edit_user_info(request, pk):
#     user_obj = User.objects.get(pk=pk)
#     if request.method == "POST":
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         user_obj.email = email
#         user_obj.address = address
#         user_obj.first_name = first_name
#         user_obj.phone = phone
#         user_obj.last_name = last_name
#         user_obj.save()
#         return redirect('user-profile')
#     return render(request, 'accounts/user_edit.html', context={"user": user_obj})
