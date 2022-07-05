from datetime import datetime
import email
from multiprocessing import context
from re import template
from django.shortcuts import render
from weatherapp.models import AppUser

#package for sending mail
from django.core.mail import send_mail

#form
from weatherapp.forms import RegistrationForm

from weatherapp.forms import LoginForm

# Create your views here.

def landing(request):
    return render(request, 'index.html')

def user_login(request):
    #creating LoginForm form object
    lf = LoginForm()
    template = 'users/login.html'
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        #checking and selecting user object from database with email

        #user = AppUser.objects.get(email = request.POST.get('email'))
        user = AppUser.objects.get(email = email)

        #if request.POST.get('password') == user.password:
        if password == user.password:

            #storing user data in session
            request.session.setdefault("user_email",user.email)

            #method two
            #request.session.update({'user_email' : user.email})

            #method three
            #request.session['user_email'] = user.email

            #Checking session value and redirecting into index page
            if request.session.has_key('user_email'):
                
                template = 'users/index.html'
                context = {
                
                    'msg_success': 'Login Success',
                    'wc_msg' : 'Welcome to weather app',
                    'page_content_title': 'This is a user dashboard.',
                    'page_content_body' : 'Hello! Welcome to our User Dashboard.'
                }
                return render(request, template, context)

        else:
            context = {
                'form': lf,
                'msg_error': 'Login Failed'
            }
            return render(request, template, context)
            
    else:
        context = {'form':lf}
        return render(request, template, context)

def user_register(request):
    template = 'users/create.html'
    rf = RegistrationForm()
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        address = request.POST.get('address')

        #creating Appuser model object
        #parameterized constructor
        #user = AppUser(first_name = first_name, middle_name =middle_name,\
            #last_name = last_name, contact = contact, email = email,\
                #dob = dob, password = password, address = address,\
                #created_at = datetime.now())
        
        #non parameterized constructor
        user = AppUser()
        # storing data to Model Attribute via object
        user.first_name = first_name
        user.middle_name = middle_name
        user.last_name = last_name
        user.contact = contact
        user.email = email
        user.dob = dob
        user.password = password
        user.address = address
        user.created_at = datetime.now()

        #to store data
        user.save() 
        send_mail(
            'weather App - Verification Code',
            'Your email verification code is 2243567',
            'sthasan19@gmail.com',
            [user.email],
            fail_silently=False,
        )
        context = {
            'form':rf,
            'success' : 'Registered Succesfully'
        }
        
        return render(request, template, context)

    else:
        context = {'form':rf}
        return render(request, template, context)    

def user_logout(request):
    if request.session.has_key('user_email'):
        del request.session['user_email']
        lf = LoginForm()
        template = "users/login.html"
        context = {
            'form':lf
            }
        return render(request, template, context)


def user_index(request):

    # render()- this function is used to render pages in django
    #takes three parameter
    #1. request
    #2. template
    #3. data(which can be null)- must be a dict- context - is optional

    #Add session
    if request.session.has_key('user_email'):
        template = 'users/index.html'
        context = {
            'page_content_title': 'This is a user dashboard.',
            'page_content_body' : 'Hello! Welcome to our User Dashboard.'
        }
        return render (request, template, context)

    else:
        lf = LoginForm()
        template = "users/login.html"
        context = {
            'form':lf
            }
        return render(request, template, context)
