# Generated by Django 3.0 on 2021-08-06 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='اسم التصنيف')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='عن التصنيف')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='الأسم')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='العنوان')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='الهاتف')),
                ('message', models.TextField(blank=True, null=True, verbose_name='الرساله')),
            ],
        ),
        migrations.CreateModel(
            name='HebaKheer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم ')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='العنوان')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='الهاتف')),
                ('ammount', models.IntegerField(blank=True, null=True, verbose_name='المبلغ')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='الأسم')),
                ('message', models.TextField(blank=True, null=True, verbose_name='الرساله')),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='اسم المدرب')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='لوجو الدوره')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='اسم الدوره')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='عن الدوره')),
                ('logo', models.ImageField(null=True, upload_to='', verbose_name='لوجو الدوره')),
                ('duration', models.SmallIntegerField(blank=True, null=True)),
                ('link', models.URLField(blank=True, db_index=True, max_length=128, null=True, unique=True, verbose_name='المسار')),
                ('start_date', models.DateField(null=True, verbose_name='تاريخ البدايه')),
                ('end_date', models.DateField(null=True, verbose_name='تاريخ النهايه')),
                ('total_hours', models.IntegerField(blank=True, null=True, verbose_name='عدد الساعات')),
                ('price', models.IntegerField(blank=True, default=1500, null=True, verbose_name='السعر')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='khieer.Category', verbose_name='التصنيف')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khieer.Trainer', verbose_name='المدرب')),
            ],
        ),
    ]
