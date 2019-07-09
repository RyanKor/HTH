from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


#유저가 로그인 정보를 입력한 이후, 어떤 템플릿으로 연결되어야 하는가?
#우리는 index.html로 연결해서 유저의 메인페이지를 관리한다.
class IndexTemplateView(LoginRequiredMixin, TemplateView):
    
    def get_template_names(self):
        template_name = "index.html"
        return template_name
