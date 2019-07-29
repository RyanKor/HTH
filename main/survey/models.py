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

    PAIN_POSITION = [
        ("whole abdomen", "복부 전체"),
        ("sternal", "명치"),
        ("umbilicus", "배꼽"),
        ("flank", "옆구리"),
        ("LUQ", "왼쪽 위"),
        ("LLQ", "왼쪽 아래"),
        ("RUQ", "오른쪽 위"),
        ("RLQ", "오른쪽 아래"),
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

    PAIN_CHARACTER = [ # 통증의 양상 다양한 표현이 있을 수 있다.
        ('crushing', '쥐어짜듯'),
        ('burning', '타는듯'),
        ('stabbing', '베이듯'),
        ('splitting', '찢어지듯'),
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
        ('change of appetite', '식욕감소'),
        ('nausea', '구역질'),
        ('vomiting', '구토'),
        ('vomiting blood', '토혈'),
        ('abdominal inflation', '복부팽만'),
        ('lump on abdomen', '복부종괴'),
        ('constipation', '변비'),
        ('diarrhea', '설사'),
        ('rectal_bleeding', '혈변'),
        ('melena', '흑색변'),
        ('steatorrhea', '지방변'),
        ('jaundice', '황달'),
        ('nothing', '해당사항 없음'),        
    ]

    ASSOCIATED_SYMPTOM_CIRCULATORY = [
        ('chest pain', '가슴통증'),
        ('shortness of breah', '호흡곤란'),
        ('cough', '기침'),
        ('runny nose', '콧물'),
        ('nothing', '해당사항 없음'),        
    ]

    ASSOCIATED_SYMPTOM_GYNECOLOGY = [
        ('colporrhagia', '질출혈'),
        ('leukorrhea', '질분비물'),
        ('menstrual cycle change', '생리주기변화'),
        ('pregnant possibility', '임신가능성'),
        ('nothing', '해당사항 없음'),            
    ]

    ASSOCIATED_SYMPTOM_WHOLE_BODY = [
        ('fever', '발열'),
        ('chilling', '오한'),
        ('fatigue', '피로'),
        ('weight change', '체중변화'),
        ('sweating', '식은땀'),
        ('sleep disturbance','수면곤란'), 
        ('headache', '두통'),
        ('nothing', '해당사항 없음'),        
    ]

    ASSOCIATED_SYMPTOM_URINARY = [
        ('painful urination', '배뇨통'),
        ('chnage the quantity of urine', '소변량변화'),
        ('red urine', '혈뇨'),
        ('foamy urine', '거품뇨'),
        ('frequency' ,'잦은 소변'),
        ('nothing', '해당사항 없음'),        
    ]

    FACTOR = [
        ('after meal', '식사후 심해짐'),
        ('no meal', '공복에심해짐'),
        ('after alchol', '음주후 심해짐'),
        ('posture', '자세에따라 통증변화'),
        ('urination', '배뇨시 통증변화'),
        ('defecation', '배변시 통증변화'),
        ('nothing', '해당사항 없음'),
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
    symtpom_location = models.CharField(max_length=20, choices=PAIN_POSITION, default="NULL")
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

    abdomen_relevant = models.CharField(max_length=30, choices=abdomen_history)
    # abdomen_relevant = models.CharField(max_length=100)

    def __str__(self):
        return (self.author.username + '/' + self.symptom + '/' + str(self.id))
        
