# Generated by Django 2.1.10 on 2019-07-27 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StomachacheSurvey',
            fields=[
                ('survey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='stomach', serialize=False, to='survey.SurveyMeta')),
                ('symptom_start', models.CharField(choices=[('less_than_month', '한 달이 안됐습니다.'), ('more_than_month', '한 달이 넘었습니다.')], max_length=50)),
                ('symptom_start_less_than_month', models.DateField(default='2019-07-23')),
                ('fast_or_slow', models.CharField(choices=[('fast', '갑자기'), ('slow', '천천히')], max_length=20)),
                ('symtpon_situation', models.CharField(max_length=50)),
                ('symtpom_location', models.CharField(max_length=100)),
                ('location_move', models.BooleanField(default=False)),
                ('location_move_how', models.CharField(max_length=100)),
                ('pain_spread', models.BooleanField(default=False)),
                ('pain_spread_where', models.CharField(max_length=100)),
                ('pain_duration', models.CharField(choices=[('lest_than_10m', '10분 미만'), ('from_10m_to_1h', '10분 ~ 1시간'), ('more_than_1h', '1시간 이상'), ('all_day', '하루종일')], max_length=20)),
                ('pain_repeated', models.BooleanField(default=False)),
                ('pain_per_day', models.CharField(choices=[('0_to_1', '0~1회'), ('2_to_3', '2~3회'), ('4_to_5', '4회~5회'), ('more_than_6', '6회이상')], max_length=20)),
                ('pain_worse', models.BooleanField(default=False)),
                ('pain_experience', models.BooleanField(default=False)),
                ('pain_character', models.CharField(choices=[('squeeze', '쥐어짜듯'), ('burn', '타는듯'), ('cut', '베이듯')], max_length=20)),
                ('pain_score', models.CharField(choices=[('1', '1점'), ('2', '2점'), ('3', '3점'), ('4', '4점'), ('5', '5점'), ('6', '6점'), ('7', '7점'), ('8', '8점'), ('9', '9점'), ('10', '10점')], max_length=20)),
                ('associated_symptom_digestive', models.CharField(choices=[('식욕감소', '식욕감소'), ('구역질', '구역질'), ('구토', '구토'), ('토혈', '토혈'), ('복부팽만', '복부팽만'), ('복부종괴', '복부종괴'), ('변비', '변비'), ('설사', '설사'), ('혈변', '혈변'), ('흑색변', '흑색변'), ('지방변', '지방변'), ('황달', '황달')], max_length=20)),
                ('associated_symptom_circulatory', models.CharField(choices=[('가슴통증', '가슴통증'), ('호흡곤란', '호흡곤란'), ('기침', '기침')], max_length=20)),
                ('associated_symptom_gynecology', models.CharField(choices=[('질출혈', '질출혈'), ('질분비물', '질분비물'), ('생리주기변화', '생리주기변화'), ('임신가능성', '임신가능성')], max_length=20)),
                ('associated_symptom_whole_body', models.CharField(choices=[('발열', '발열'), ('오한', '오한'), ('피로', '피로'), ('체중변화', '체중변화'), ('식은땀', '식은땀')], max_length=20)),
                ('associated_symptom_urinary', models.CharField(choices=[('배뇨통', '배뇨통'), ('소변량변화', '소변량변화'), ('혈뇨', '혈뇨'), ('빈뇨', '빈뇨')], max_length=20)),
                ('associated_symptom_others', models.CharField(max_length=100)),
                ('factor', models.CharField(choices=[('after_meal', '식사후 심해짐'), ('no_meal', '공복에심해짐'), ('after_alchol', '음주후 심해짐'), ('posture', '자세에따라 통증변화'), ('defecation', '배뇨/배변에 의해 통증변화')], max_length=20)),
                ('other_factor', models.CharField(max_length=100)),
            ],
            bases=('survey.surveymeta',),
        ),
    ]
