# Generated by Django 3.0 on 2021-08-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khieer', '0002_remove_trainer_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('job', models.CharField(blank=True, max_length=255, null=True, verbose_name='المهنه')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='التخصص')),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('ذكر', 'ذكر'), ('أنثى', 'انثى')], max_length=255, null=True)),
                ('time', models.CharField(choices=[('متفرغ', 'متفرغ'), ('غير متفرغ', 'غير متفرغ')], max_length=255, null=True)),
                ('place', models.CharField(max_length=255, null=True)),
                ('study', models.CharField(max_length=255, null=True)),
                ('skills', models.TextField(null=True)),
                ('goals', models.TextField(null=True)),
                ('filed', models.CharField(max_length=255, null=True)),
                ('cv', models.FileField(null=True, upload_to='')),
                ('date_received', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
