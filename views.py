from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect




# Create your views here.
def home(request):
    obj = student2.objects.all()



    return render(request,'index.html',{'obj':obj})




def student2(request):
    if request.method == 'POST':
        form=student_form(request.POST)
        if form.is_valid():
            nm=form.cleaned_data['name']
            em=form.cleaned_data['emailid']
            cm=form.cleaned_data['contact']
            reg=student2(name=nm,emailid=em,contact=cm)
            reg.save()
            messages.info(request,"Data Successfully Added to Database")
            return HttpResponseRedirect('/studentform/')
    else:
         form=student_form()
    return render(request,'student.html',{'form':form})


def studentregistration(request):
    form1 = UserRegistration.objects.all()
    return render(request,'registration_display.html',{'form1':form1})

def registration(request):
    if request.method == 'POST':
        form1=userRegistration(request.POST)
        if form1.is_valid():
            username=form1.cleaned_data['username']
            email=form1.cleaned_data['email']
            firstname=form1.cleaned_data['firstname']
            lastname = form1.cleaned_data['lastname']
            password = form1.cleaned_data['password']
            conpassword=form1.cleaned_data['conpassword']
            mobno=form1.cleaned_data['mobno']

            reg=UserRegistration(username=username,email=email,firstname=firstname,lastname=lastname,password=password,conpassword=conpassword,mobno=mobno)
            reg.save()
            messages.info(request,"Data Successfully Added to Database")
            return HttpResponseRedirect('/registration/')
    else:
         form1=userRegistration()
    return render(request,'Registration.html',{'form1':form1})



def search(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = medicalstore.objects.filter(Q(medicine_name__icontains=srch))
            if match:
                return render(request, 'medicine_name.html', {'sr': match})
            else:
                messages.error(request, "no result found")
        else:
            return HttpResponseRedirect('/search/')

    return render(request,'medicine_name.html')

def medicine_name(request):
    obj = mediacldetails.objects.all()
    return render(request,'search2.html',{'obj':obj})

