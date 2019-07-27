from django.db import models
from users.models import CustomUser
from profiles.models import Profile
# Create your models here.

class SurveyMeta(models.Model):

    symptom = models.CharField(max_length=20)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # default=date.today로 해도 될 듯?

    def __str__(self):
        return (self.author.username + '/' + self.symptom + '/' + str(self.id))

class StomachacheSurvey(SurveyMeta):
    survey = models.OneToOneField(
        SurveyMeta, on_delete=models.CASCADE, related_name='stomach', parent_link=True)

    SYMTPOM_START = [
        ('less_than_month', '한 달이 안됐습니다.'),
        ('more_than_month', '한 달이 넘었습니다.'),
    ]

    FAST_OR_SLOW = [
        ('fast', '갑자기'),
        ('slow', '천천히'),
    ]

    PAIN_DURATION = [
        ('lest_than_10m', '10분 미만'),
        ('from_10m_to_1h', '10분 ~ 1시간'),
        ('more_than_1h', '1시간 이상'),
        ('all_day', '하루종일'),
    ]

    PAIN_REPEATED = [
        ('repeat', '반복됩니다'),
        ('no_repeat', '단발성입니다'),
    ]
    PAIN_PER_DAY = [
        ('0_to_1', '0~1회'),
        ('2_to_3', '2~3회'),
        ('4_to_5', '4회~5회'),
        ('more_than_6', '6회이상'),
    ]

    PAIN_CHARACTER = [
        ('squeeze', '쥐어짜듯'),
        ('burn', '타는듯'),
        ('cut', '베이듯'),
    ]

    PAIN_SCORE = [
        ('1', '1점'),
        ('2', '2점'),
        ('3', '3점'),
        ('4', '4점'),
        ('5', '5점'),
        ('6', '6점'),
        ('7', '7점'),
        ('8', '8점'),
        ('9', '9점'),
        ('10', '10점'),
    ]

    ASSOCIATED_SYMPTOM_DIGESTIVE = [
        ('식욕감소', '식욕감소'),
        ('구역질', '구역질'),
        ('구토', '구토'),
        ('토혈', '토혈'),
        ('복부팽만', '복부팽만'),
        ('복부종괴', '복부종괴'),
        ('변비', '변비'),
        ('설사', '설사'),
        ('혈변', '혈변'),
        ('흑색변', '흑색변'),
        ('지방변', '지방변'),
        ('황달', '황달'),
    ]

    ASSOCIATED_SYMPTOM_CIRCULATORY = [
        ('가슴통증', '가슴통증'),
        ('호흡곤란', '호흡곤란'),
        ('기침', '기침'),
    ]

    ASSOCIATED_SYMPTOM_GYNECOLOGY = [
        ('질출혈', '질출혈'),
        ('질분비물', '질분비물'),
        ('생리주기변화', '생리주기변화'),
        ('임신가능성', '임신가능성'),

    ]

    ASSOCIATED_SYMPTOM_WHOLE_BODY = [
        ('발열', '발열'),
        ('오한', '오한'),
        ('피로', '피로'),
        ('체중변화', '체중변화'),
        ('식은땀', '식은땀'),
    ]

    ASSOCIATED_SYMPTOM_URINARY = [
        ('배뇨통', '배뇨통'),
        ('소변량변화', '소변량변화'),
        ('혈뇨', '혈뇨'),
        ('빈뇨', '빈뇨'),
    ]

    FACTOR = [
        ('after_meal', '식사후 심해짐'),
        ('no_meal', '공복에심해짐'),
        ('after_alchol', '음주후 심해짐'),
        ('posture', '자세에따라 통증변화'),
        ('defecation', '배뇨/배변에 의해 통증변화'),
    ]

    abdomen_hurted = "복부를 다친 적이 있음"
    abdomen_surgery = "복부 수술을 받은 적이 있음"
    abdomen_nothing = "해당없음"
    abdomen_history = (
        (abdomen_hurted, "복부를 다친 적이 있음"), (abdomen_surgery,
                                           "복부 수술을 받은 적이 있음"), (abdomen_nothing, "해당없음")
    )

    # Onset
    symptom_start = models.CharField(choices=SYMTPOM_START, max_length=50)
    symptom_start_less_than_month = models.DateField(default='2019-07-23')
    fast_or_slow = models.CharField(choices=FAST_OR_SLOW, max_length=20)
    symtpon_situation = models.CharField(max_length=50)

    # location
    symtpom_location = models.CharField(max_length=100)
    location_move = models.BooleanField(default=False)
    location_move_how = models.CharField(max_length=100)
    pain_spread = models.BooleanField(default=False)
    pain_spread_where = models.CharField(max_length=100)

    # Duration
    pain_duration = models.CharField(choices=PAIN_DURATION, max_length=20)
    pain_repeated = models.BooleanField(default=False)
    pain_per_day = models.CharField(choices=PAIN_PER_DAY, max_length=20)

    # Course
    pain_worse = models.BooleanField(default=False)

    # Experience
    pain_experience = models.BooleanField(default=False)

    # character
    pain_character = models.CharField(choices=PAIN_CHARACTER, max_length=20)
    pain_score = models.CharField(choices=PAIN_SCORE, max_length=20)

    # associated symptom
    associated_symptom_digestive = models.CharField(
        choices=ASSOCIATED_SYMPTOM_DIGESTIVE, max_length=20)

    associated_symptom_circulatory = models.CharField(
        choices=ASSOCIATED_SYMPTOM_CIRCULATORY, max_length=20)

    associated_symptom_gynecology = models.CharField(
        choices=ASSOCIATED_SYMPTOM_GYNECOLOGY, max_length=20)

    associated_symptom_whole_body = models.CharField(
        choices=ASSOCIATED_SYMPTOM_WHOLE_BODY, max_length=20)

    associated_symptom_urinary = models.CharField(
        choices=ASSOCIATED_SYMPTOM_URINARY, max_length=20)

    associated_symptom_others = models.CharField(max_length=100)

    # factor
    factor = models.CharField(choices=FACTOR, max_length=20)
    other_factor = models.CharField(max_length=100)

    # 다음 중 해당 사항에 모두 체크해주세요

    abdomen_relevant = models.CharField(max_length=15, choices=abdomen_history)

    def __str__(self):
        return (self.author.username + '/' + self.symptom + '/' + str(self.id))
        
