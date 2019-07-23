# 2.인우 : 프로필에 들어갈 간단한 정보를 포함해서 user모델을 커스텀했습니다.

from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    avatar = models.ImageField(null=True, blank=True)
    # 3.인우 : 장고에서 ImageField를 쓰기 위해서는 pillow 패키지가 필수라고 합니다.
    # requirements.txt에 freeze시켜뒀습니다.
    # requriements.txt에 있는 모든 항목을 다운받으려면
    # pip install -r requirements.txt
    # 를 실행하면 됩니다.

    male = "남성"
    female = "여성"
    gender_choices = (
        (male, '남성'), (female, "여성")
    )
    gender = models.CharField(
        max_length=6, choices=gender_choices)
    # 4.인우 : 디폴트값 없으면 migration이 안 먹혀서 임의로 넣었습니다.

    birth_date = models.DateField(default=date.today)

    height = models.PositiveSmallIntegerField(default=160,
                                              validators=[MaxValueValidator(250)])
    # 5.인우 : validator는 나중에 좀 더 손봐야 할 것 같습니다. 장난으로 키 막 300 이렇게 적을까봐 일단
    # 넣어봤어요.
    # 디폴트값 없으면 migration이 안 먹혀서 임의로 넣었습니다.

    weight = models.PositiveSmallIntegerField(default=60,
                                              validators=[MaxValueValidator(200)])
    # 6.인우 : validator는 나중에 좀 더 손봐야 할 것 같습니다. 장난으로 몸무게 막 300 이렇게 적을까봐 일단
    # 넣어봤어요.
    # 디폴트값 없으면 migration이 안 먹혀서 임의로 넣었습니다.

    name = models.CharField(max_length=10)
    # 7.인우 : default값으로 이름 말고 더 좋은 의견 있으신가요?
    # 디폴트값 없으면 migration이 안 먹혀서 임의로 넣었습니다.
    # ->main/setting.py AUTH_USER_MODEL로 ㄱㄱ

    # 과거력

    # 이전에 건강검진을 받은 적이 있나요?
    had_checkup = models.BooleanField(default=False)
    # 얘도 디폴트값 설정 안하면 createsuperuser오류나여...

    # 몇 년 전에 받았나요?
    under_one = "1년 이내"
    one_to_three = "1-3년"
    three_to_five = "3-5년"
    five_to_ten = "5-10년"
    over_ten = "10년 이상"
    how_long_before = (
        (under_one, '1년 이내'), (one_to_three, "1-3년"), (three_to_five,
                                                       "3-5년"), (five_to_ten, "5-10년"), (over_ten, "10년 이상")
    )
    had_checkup_true = models.CharField(
        max_length=6, choices=how_long_before, blank=True, null=True)

    # 이전에 진단받은 병이 있나요?
    high_blood_pressure = "고혈압"
    hepatitis = "간염"
    tuberculosis = "결핵"
    none = "없음"
    etc = "기타"
    disease_list = (
        (high_blood_pressure, '고혈압'), (hepatitis,
                                       '간염'), (tuberculosis, '결핵'), (none, '없음'), (etc, '기타')
    )
    diagnosed_disease = models.CharField(max_length=3, choices=disease_list)

    # 드시고 계시는 약이 있나요?
    taking_medicine = models.BooleanField(default=False)
    # 얘도 디폴트값 설정 안하면 createsuperuser오류나여...

    # 드시고 계신 약물을 알려주세요
    what_medicine = models.CharField(max_length=20, blank=True, null=True)
    # 복용하고 있는 약물이 복수라면...? 필드를 조정하거나 max_length를 조정해야 하나..?

    # 가족분들이 진단 받은 병이 있나요?
    family_history = models.CharField(max_length=3, choices=disease_list)

    # 사회력

    # 술을 드시나요?
    drinking = models.BooleanField(default=False)
    # 얘도 디폴트값 설정 안하면 createsuperuser오류나여...

    # 매주 몇 병 드시나요?
    drinking_per_week = models.PositiveSmallIntegerField(blank=True, null=True)

    # 흡연하시나요?
    smoking_true = "예"
    smoking_false = "아니오"
    smoking_quit = "끊었음"
    do_you_smoke = (
        (smoking_true, "예"), (smoking_false, "아니오"), (smoking_quit, "끊었음")
    )
    smoking = models.CharField(max_length=3, choices=do_you_smoke)

    # 몇년째 피고 계신가요?
    how_long_smoking = models.PositiveSmallIntegerField(default=0)
    # 얘도 디폴트값 설정 안하면 createsuperuser오류나여...

    # 몇 갑씩 피시나요
    how_much_smoking = models.PositiveSmallIntegerField(default=0)
    # 얘도 디폴트값 설정 안하면 createsuperuser오류나여...

    # 직업이 무엇인가요?
    job = models.CharField(max_length=20, blank=True, null=True)
    # 직업을 꼭 말하고 싶지 않을 수도 있죠

    # 다음 중 해당사항에 체크해주세요
    stress="스트레스를 많이 받는 편"
    irregular_meals="식사 불규칙"
    greasy_meals="기름진 음식을 많이 먹음"
    irregular_sleep="수면시간 불규칙"
    bad_habits=(
        (stress, "스트레스를 많이 받는 편"), (irregular_meals, "식사 불규칙"), (greasy_meals, "기름진 음식을 많이 먹음"), (irregular_sleep, "수면시간 불규칙")
    )
    relevant_data = models.CharField(max_length=13, choices=bad_habits, blank=True, null=True)

    # 다음 중 해당 사항에 모두 체크해주세요
    # abdomen_hurted = "복부를 다친 적이 있음"
    # abdomen_surgery = "복부 수술을 받은 적이 있음"
    # abdomen_nothing = "해당없음"
    # abdomen_history = (
    #     (abdomen_hurted, "복부를 다친 적이 있음"), (abdomen_surgery, "복부 수술을 받은 적이 있음"), (abdomen_nothing, "해당없음")
    # )
    # abdomen_relevant = models.CharField(max_length=15, choices=abdomen_history)

    def __str__(self):
        return self.username
