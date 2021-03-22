from django.views.generic import TemplateView
from django.http import HttpResponse

def reccomendation_system(request):
    print("This is a simple function")
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

class IndexPageView(TemplateView):
    template_name = 'main/index.html'


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'

class MovieReccomdationView(TemplateView):
    template_name = 'main/recomend.html'
