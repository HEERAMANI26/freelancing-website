from django.db import models

class student2(models.Model):
    name=models.CharField(max_length=50)
    emailid=models.EmailField(max_length=50)
    contact=models.CharField(max_length=10)


# Create your models here.
def __str__(self):
    return self.name

class UserRegistration(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    conpassword=models.CharField(max_length=20)
    mobno=models.CharField(max_length=11)



def __str__(self):
    return self.name



class medicalstore(models.Model):
    medicine_name=models.CharField(max_length=50)
    medicine_shop_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    contact=models.CharField(max_length=11)
    email=models.EmailField(max_length=50)



# Create your models here.
def __str__(self):
    return self.name




class mediacldetails(models.Model):
    medicine_name=models.CharField(max_length=50)
    medicine_shop_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    contact=models.CharField(max_length=11)
    email=models.EmailField(max_length=50)
    postalcode=models.CharField(max_length=6)
    storage=models.CharField(max_length=50)
    details=models.TextField(max_length=50)



# Create your models here.
def __str__(self):
    return self.name



