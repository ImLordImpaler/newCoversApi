from django.db import models

class Vehicle_type(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Policy_type(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Fuel_type(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Owner_type(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Cover(models.Model):
    Value_type = (
        ('null' , 'null'),
        ('dropdown' , 'dropdown'),
        ('radio','radio'),
        ('text','text')
    )
    Cover_type = (
        ('Motor' , 'Motor'),
        ('Life','Life'),
        ('Health' , 'Health')
    )
    plan_type = (
        ('Own_Damage','Own_Damage'),
        ('Liability' , 'Liability'),
        ('Addon' , 'Addon'),
        ('Discounts','Discounts')
    )
    cover_type = models.CharField(max_length=100 , choices=Cover_type , null=True , blank=True )
    description = models.CharField(max_length=100 , null=True , blank=True)
    name = models.CharField(max_length=100 )
    code = models.CharField(max_length=50 )
    value = models.CharField(max_length=100 , blank=True , null=True )
    value_type = models.CharField(choices=Value_type , max_length=100 , blank=True , null=True , default='null')
    plan_type = models.CharField(max_length=100 , choices=plan_type , null=True , blank=True)
    policy_type = models.ManyToManyField(Policy_type , blank=True)
    owner_type = models.ManyToManyField(Owner_type , blank=True )
    fuel_type = models.ManyToManyField(Fuel_type , blank=True)
    vehicle_type = models.ManyToManyField(Vehicle_type , blank=True)
    # vehicle_type = models.CharField(max_length=100,choices=Vehicle_type , blank=True , null=True , default='all')
    def __str__(self):
        # #Owner_type , Fuel , policy_type , vehicle
        # l1 = []
        # if self.owner !='all':
        #     l1.append(self.owner)
        # s = ''
        # for i in l1:
        #     s += i +" "
        # return s
        return str(self.name + " "+ self.code)


class Question(models.Model):
    name = models.CharField(max_length=100)
    sub_question = models.ManyToManyField('SubQuestion' , blank=True)

    def __str__(self):
        return self.name


class SubQuestion(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name