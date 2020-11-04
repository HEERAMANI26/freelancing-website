from django import forms
from.models import *

class student_form(forms.Form):
    name=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    emailid=forms.EmailField()
    contact=forms.CharField(widget=forms.TextInput(),required=True,max_length=11)




    class meta():
        model=student2
        fields=['name','emailid','contact']


class userRegistration(forms.Form):
    username = forms.CharField(widget=forms.TextInput(),required=True, max_length=50)
    email = forms.EmailField()
    firstname = forms.CharField(widget=forms.TextInput(),required=True, max_length=50)
    lastname = forms.CharField(widget=forms.TextInput(),required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(),required=True, max_length=20)
    conpassword = forms.CharField(widget=forms.PasswordInput(),required=True, max_length=20)
    mobno = forms.CharField(widget=forms.TextInput(),required=True, max_length=11)



    class meta():
        model=UserRegistration
        fields=['username','email','firstname','lastname','password','conpassword','mobno']


class medicalmarket(forms.Form):
    medicine_name = forms.CharField(widget=forms.TextInput(), required=True, max_length=50)
    medicine_shop_name = forms.CharField(widget=forms.TextInput(), required=True, max_length=50)
    address = forms.CharField(widget=forms.TextInput(), required=True, max_length=50)
    contact = forms.CharField(widget=forms.TextInput(), required=True, max_length=11)
    email = forms.EmailField()



    class meta():
        model=medicalstore
        fields=['medicine_name','medicine_shop_name','address','contact','email']




class MEDICALSTORAGE(forms.Form):
    medicine_name = forms.CharField(widget=forms.TextInput(), required=True, max_length=50)
    medicine_shop_name = forms.CharField(widget=forms.TextInput(), required=True, max_length=50)
    address = forms.CharField(widget=forms.TextInput(), required=True, max_length=50)
    contact = forms.CharField(widget=forms.TextInput(), required=True, max_length=11)
    email = forms.EmailField()
    postalcode = forms.CharField(widget=forms.TextInput(), required=True, max_length=11)

    storage = forms.CharField(widget=forms.TextInput(), required=True, max_length=11)
    details=forms.CharField(widget=forms.Textarea(), required=True,max_length=100)


    class meta():
        model=mediacldetails
        fields=['medicine_name','medicine_shop_name','address','contact','email','postalcode','storage','details']