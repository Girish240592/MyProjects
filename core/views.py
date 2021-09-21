from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.contrib import messages
from django.http import HttpResponse, response

# Create your views here.
# Middeleware view (Function Based) start
def home1(request):
    print('This is my home view function')
    return HttpResponse('This is my home page and views')
# Middeleware view function based end


# Middeleware view (Class Based) start
def home2(request):
    print('This is my home view function for class based middleware')
    return HttpResponse('This is my home page and views for class based middleware')
# Middeleware view Class based end
# Cookie Start
def set_cookie(request):
    response = render(request, 'core/setcookies.html')
    response.set_cookie('f_name','Girish')
    response.set_cookie('l_name','Rode')
    response.set_cookie('address','Nagpur',max_age=60*60*24*2)
    return response

def get_cookie(request):
    # This Method Will give you an error
    # nm=request.COOKIES['f_name']
    # ln=request.COOKIES['l_name']
    # ad=request.COOKIES['address']
    
    # This Method Will give you "None""
    nm=request.COOKIES.get('f_name')
    ln=request.COOKIES.get('l_name')
    ad=request.COOKIES.get('address')
    return render(request, 'core/getcookies.html',{'nm':nm,'ln':ln,'ad':ad})

def delete_cookie(request):
    response = render(request, 'core/delcookies.html')
    response.delete_cookie('f_name')
    response.delete_cookie('l_name')
    response.delete_cookie('address')
    return response

#Cookie End

# Session Start
def set_session(request):
    request.session['firstname']='Girish'
    request.session['lastname']='Rode'
    request.session['address']='A1 302 Garden Court Nagpur'
    return render (request, 'core/setsession.html')

def get_session(request):
    # This Method Will give you an error
    # fn=request.session['firstname']
    # ln=request.session['lastname']
    # addr=request.session['address']
    
    # This Method Will give you "None""
    fn=request.session.get('firstname')
    ln=request.session.get('lastname')
    addr=request.session.get('address')
    return render (request, 'core/getsession.html',{'name':fn,'surname':ln,'address':addr})

# First Method (To Delete perticular sessions)
def del_session(request):
    # if 'dd' is request.session:
    del request.session['firstname']
    # if 'lastname' is request.session:
    del request.session['lastname']
    # if 'address' is request.session:
    del request.session['address']
    response=render(request,'core/delsession.html')

    return response
# Second Method (To Delete all sessions At a Time) 

# def del_session(request):
#     response=request.session.flush()
#     return render(request, 'core/delsession.html', {'res':response})

# Session End
def home1(request):
    #stu=Student.objects.all()
    #stu=Student.objects.get(id=1)
    #stu=Student.objects.filter(roll=221)
    #stu=Student.objects.exclude(roll=221)
    #stu=Student.objects.order_by('roll') # ASC Order
    stu=Student.objects.order_by('-id')  # DSC Order
    #stu=Student.objects.order_by('name') # Order by name alphabatical order
    return render(request, 'core/home1.html', {'form':stu})

def home(request,vnit,check,errors):    
    print(check)
    print(errors)
    value = vnit
    err = errors
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            rol=fm.cleaned_data['roll']
            adds=fm.cleaned_data['address']
            stu=Student(name=nm, roll=rol, address=adds)
            stu.save()
            messages.success(request, "Your form has been submitted successfully...!!")
            # stu=Student(id=6,name=nm, roll=rol, address=adds)
            # stu.delete()
            fm=StudentForm()
    else:
        fm=StudentForm()
    return render(request, 'core/home.html', {'form':fm},)