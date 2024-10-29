from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

from django.shortcuts import render

# Create your views here.

def func_templates_view(request):
    return render(request, 'second_task/func_template.html')

def main_page(request):
    return render(request, 'second_task/main_page.html')

class class_templates_view(TemplateView):
    template_name = 'second_task/class_template.html'