# Generated by Django 2.1.10 on 2019-07-22 18:30

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('gender', models.CharField(choices=[('남성', '남성'), ('여성', '여성')], max_length=6)),
                ('birth_date', models.DateField(default=datetime.date.today)),
                ('height', models.PositiveSmallIntegerField(default=160, validators=[django.core.validators.MaxValueValidator(250)])),
                ('weight', models.PositiveSmallIntegerField(default=60, validators=[django.core.validators.MaxValueValidator(200)])),
                ('name', models.CharField(max_length=10)),
                ('had_checkup', models.BooleanField(default=False)),
                ('had_checkup_true', models.CharField(blank=True, choices=[('1년 이내', '1년 이내'), ('1-3년', '1-3년'), ('3-5년', '3-5년'), ('5-10년', '5-10년'), ('10년 이상', '10년 이상')], max_length=6, null=True)),
                ('diagnosed_disease', models.CharField(choices=[('고혈압', '고혈압'), ('간염', '간염'), ('결핵', '결핵'), ('없음', '없음'), ('기타', '기타')], max_length=3)),
                ('taking_medicine', models.BooleanField(default=False)),
                ('what_medicine', models.CharField(blank=True, max_length=20, null=True)),
                ('family_history', models.CharField(choices=[('고혈압', '고혈압'), ('간염', '간염'), ('결핵', '결핵'), ('없음', '없음'), ('기타', '기타')], max_length=3)),
                ('drinking', models.BooleanField(default=False)),
                ('drinking_per_week', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('smoking', models.CharField(choices=[('예', '예'), ('아니오', '아니오'), ('끊었음', '끊었음')], max_length=3)),
                ('how_long_smoking', models.PositiveSmallIntegerField(default=0)),
                ('how_much_smoking', models.PositiveSmallIntegerField(default=0)),
                ('job', models.CharField(blank=True, max_length=20, null=True)),
                ('relevant_data', models.CharField(blank=True, choices=[('스트레스를 많이 받는 편', '스트레스를 많이 받는 편'), ('식사 불규칙', '식사 불규칙'), ('기름진 음식을 많이 먹음', '기름진 음식을 많이 먹음'), ('수면시간 불규칙', '수면시간 불규칙')], max_length=13, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
