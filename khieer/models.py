from datetime import date
from django.utils.translation import gettext_lazy as _
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='الأسم')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='العنوان')
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='الهاتف')
    message = models.TextField(null=True, blank=True, verbose_name='الرساله')

    def __str__(self):
        return self.name


class HebaKheer(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='اسم ')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='العنوان')
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='الهاتف')
    ammount = models.IntegerField(null=True, blank=True, verbose_name='المبلغ')

    def __str__(self):
        return self.name


class TechnicalSupport(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='الأسم')
    message = models.TextField(blank=True, null=True, verbose_name='الرساله')

    def __str__(self):
        return self.name


class Trainer(models.Model):
    image = models.ImageField(verbose_name='لوجو الدوره', null=True)
    email = models.EmailField(
        verbose_name=_('email address'), max_length=255, unique=True
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    address = models.CharField(_('Address'), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم التصنيف')
    description = models.CharField(max_length=255, null=True, verbose_name='عن التصنيف')

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم الدوره')
    description = models.CharField(max_length=255, null=True, verbose_name='عن الدوره')
    logo = models.ImageField(verbose_name='لوجو الدوره', null=True)
    duration = models.SmallIntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name='التصنيف')
    link = models.URLField(
        verbose_name='المسار',
        max_length=128,
        db_index=True,
        unique=True,
        blank=True,
        null=True
    )
    start_date = models.DateField(verbose_name="تاريخ البدايه", null=True, auto_now=False, auto_now_add=False)
    end_date = models.DateField(verbose_name="تاريخ النهايه", null=True, auto_now=False, auto_now_add=False, )
    total_hours = models.IntegerField(null=True, blank=True, verbose_name='عدد الساعات')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, verbose_name='المدرب')

    @property
    def is_past_due(self):
        return date.today() > self.end_date

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    email = models.EmailField(
        verbose_name=_('email address'), max_length=255, unique=True
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    address = models.CharField(_('Address'), max_length=255, null=True, blank=True)
    job = models.CharField(max_length=255, null=True, blank=True, verbose_name='المهنه')
    desc = models.CharField(max_length=255, null=True, blank=True, verbose_name='التخصص')
    birthdate = models.DateField(null=True, blank=True)
    GENDER_CHOICES = (
        ('ذكر', 'ذكر'),
        ('أنثى', 'انثى'),
    )
    gender = models.CharField(max_length=255, null=True, choices=GENDER_CHOICES)
    TIME_CHOICES = (
        ('متفرغ', 'متفرغ'),
        ('غير متفرغ', 'غير متفرغ'),
    )
    time = models.CharField(max_length=255, null=True, choices=TIME_CHOICES)
    place = models.CharField(max_length=255, null=True)
    study = models.CharField(max_length=255, null=True)
    skills = models.TextField(null=True)
    goals = models.TextField(null=True)
    filed = models.CharField(max_length=255, null=True)
    cv = models.FileField(null=True)
    date_received = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class CourseRequest(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم الملتحق')
    email = models.EmailField(
        verbose_name=_('email address'), max_length=255
    )
    phone = models.CharField(max_length=255, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
