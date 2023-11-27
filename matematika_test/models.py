from django.db import models

# Create your models here.
class Addition(models.Model):
    number1 = models.IntegerField(null=True, blank=True)
    number2 =  models.IntegerField(null=True, blank=True)
    
    @property
    def javob(self):
        return self.number1 + self.number2

class Subtraction(models.Model):
    number1 = models.IntegerField(null=True, blank=True)
    number2 =  models.IntegerField(null=True, blank=True)

    @property
    def javob(self):
        return self.number1 - self.number2

class Multiplication(models.Model):
    number1 = models.IntegerField(null=True, blank=True)
    number2 =  models.IntegerField(null=True, blank=True)

    @property
    def javob(self):
        return self.number1 * self.number2
    
class Division(models.Model):
    number1 = models.IntegerField(null=True, blank=True)
    number2 =  models.IntegerField(null=True, blank=True)

    @property
    def javob(self):
        return self.number1 / self.number2