from django.contrib import admin
from .models import Addition, Subtraction, Multiplication, Division

# Register your models here.
admin.site.register(Addition)
admin.site.register(Subtraction)
admin.site.register(Multiplication)
admin.site.register(Division)