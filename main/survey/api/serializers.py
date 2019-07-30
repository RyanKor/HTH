from rest_framework import serializers
from survey.models import SurveyMeta, StomachacheSurvey

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

PAIN_CHARACTER = [  # 통증의 양상 다양한 표현이 있을 수 있다.
    ('crushing', '쥐어짜듯'),
    ('burning', '타는듯'),
    ('stabbing', '베이듯'),
    ('splitting', '찢어지듯'),
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
    ('sleep disturbance', '수면곤란'),
    ('headache', '두통'),
    ('nothing', '해당사항 없음'),

]

ASSOCIATED_SYMPTOM_URINARY = [
    ('painful urination', '배뇨통'),
    ('chnage the quantity of urine', '소변량변화'),
    ('red urine', '혈뇨'),
    ('foamy urine', '거품뇨'),
    ('frequency', '잦은 소변'),
    ('nothing', '해당사항 없음'),

]

abdomen_hurted = "복부를 다친 적이 있음"
abdomen_surgery = "복부 수술을 받은 적이 있음"
abdomen_nothing = "해당없음"
abdomen_history = (
    (abdomen_hurted, "복부를 다친 적이 있음"), (abdomen_surgery,
                                       "복부 수술을 받은 적이 있음"), (abdomen_nothing, "해당없음")
)


class StomachacheSurveyCreateSerializer(serializers.ModelSerializer):
    symtpom_location = serializers.MultipleChoiceField(PAIN_POSITION)
    pain_character = serializers.MultipleChoiceField(PAIN_CHARACTER)
    associated_symptom_digestive = serializers.MultipleChoiceField(
        ASSOCIATED_SYMPTOM_DIGESTIVE)
    associated_symptom_circulatory = serializers.MultipleChoiceField(
        ASSOCIATED_SYMPTOM_CIRCULATORY)
    associated_symptom_gynecology = serializers.MultipleChoiceField(
        ASSOCIATED_SYMPTOM_GYNECOLOGY)
    associated_symptom_whole_body = serializers.MultipleChoiceField(
        ASSOCIATED_SYMPTOM_WHOLE_BODY)
    associated_symptom_urinary = serializers.MultipleChoiceField(
        ASSOCIATED_SYMPTOM_URINARY)
    factor = serializers.MultipleChoiceField(FACTOR)
    abdomen_relevant = serializers.MultipleChoiceField(abdomen_history)

    class Meta:
        model = StomachacheSurvey
        exclude = ["symptom", "created_at", "author", "had_checkup", 
                   "had_checkup_true", "diagnosed_disease", "taking_medicine", 
                   "what_medicine", "family_history", "drinking", 
                   "drinking_per_week", "smoking", "how_long_smoking", 
                   "how_much_smoking", "job", "relevant_data"]


class StomachacheSurveySerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField(read_only=True)
    author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = StomachacheSurvey
        fields = "__all__"

    def get_created_at(self, instance):
        return instance.created_at.strftime("%Y %B %d")

    def get_author(self, instance):
        return str(instance.author)


class SurveyMetaSerializer(serializers.ModelSerializer):

    stomach = StomachacheSurveySerializer(read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SurveyMeta
        exclude = ["had_checkup", 
                   "had_checkup_true", "diagnosed_disease", "taking_medicine", 
                   "what_medicine", "family_history", "drinking", 
                   "drinking_per_week", "smoking", "how_long_smoking", 
                   "how_much_smoking", "job", "relevant_data"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%Y %B %d")
