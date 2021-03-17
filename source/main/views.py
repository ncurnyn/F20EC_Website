from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'main/index.html'


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'

class MovieReccomdationView(TemplateView):
    template_name = 'main/recomend.html'
