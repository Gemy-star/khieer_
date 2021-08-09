from django.urls import path
from . import views

urlpatterns = [
    path('create/contact', views.create_contact, name='create-contact'),
    path('heba-kheer', views.heba_kheer, name='heba-kheer'),
    path('technical-support', views.add_technical, name='technical-support'),
    path('technical-list', views.technical_list, name='technical-list'),
    path('home-employee', views.home_employee, name='home-employee'),
    path('add-course', views.add_greenCourse, name='add-course'),
    path('vol/report', views.VolunteerAllReport.as_view(), name='vol-report'),
    path('courses/report', views.CourseAllReport.as_view(), name='course-report'),
    path('hebas/report', views.HebaAllReport.as_view(), name='heba-report'),
    path('course/list', views.courses_list, name='course-list'),
    path('volunteers/list', views.volunteer_list, name='volunteer-list'),
    path('trainers/list', views.trainers_list, name='trainers-list'),
    path('contact/list', views.contact_list, name='contact-list'),
    path('technical/list', views.technical_list, name='techs-list'),
    path('course/request/<int:pk>', views.course_request, name='course-request'),

]
