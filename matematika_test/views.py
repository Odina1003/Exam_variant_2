from django.shortcuts import render
from .models import Multiplication, Addition, Subtraction, Division
from django.db.models import F

# Create your views here.
def main(request):
    return render(request=request, template_name='main.html')

def math(request):
    add = Addition.objects.all()
    minus = Subtraction.objects.all()
    multi = Multiplication.objects.all()
    division = Division.objects.all()
    return render(request=request, template_name='math_test.html', context={'add':add, 'minus':minus, 'multi':multi, 'division':division})
