from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm
from .models import AboutInfo
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import AboutInfo
from app_testimonials.models import Testimonial 
from app_testimonials.forms import TestimonialForm
from app_skills.models import Skill 
from app_services.models import Service 
from .forms import AboutInfoForm
from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm
from django.forms import modelformset_factory



def portfolio_details(request):
    return render(request, 'portfolio_details.html')

def about(request):
    about_info = AboutInfo.objects.first()
    return render(request, 'info_about.html', {'about_info': about_info})


# def home(request):
#     about_info = AboutInfo.objects.first()  
#     testimonials = Testimonial.objects.all() 
#     skills = Skill.objects.all() 
#     services = Service.objects.all() 
#     context = locals()

#     return render(request, 'home.html', context)


def home(request):
    about_info = AboutInfo.objects.first()  
    testimonials = Testimonial.objects.all() 
    skills = Skill.objects.all() 
    services = Service.objects.all() 
    context = {
        'about_info': about_info,
        'testimonials': testimonials,
        'skills': skills,
        'services': services,
    }
    return render(request, 'home.html', context)




def homeback(request):
    data_saved = False
    x = 'lol'
    
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data_saved = True 
            return redirect('backhome') 
    else:
        form = TestimonialForm()
    
    context = {
        'form': form,
        'data_saved': data_saved,
        'x': x,
        'isLoggedIn': request.user.is_authenticated
    }
    return render(request, 'back_home.html', context)





def modify_services(request):
    data_saved = False
    serviceform = Service.objects.all()
    
    if request.method == 'POST':
        form = ServiceForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('backhome')  
    else:
        form = ServiceForm()

    context = {
        'form': form,
    }
    
    return render(request, 'back_services.html', {'form': form, 'data_saved': data_saved, 'serviceform':serviceform})






def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

  
        user = authenticate(username=username, password=password)

        if user is not None:
            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')




def update_about(request):
    about_instance = AboutInfo.objects.first()
    data_saved = False
    
    if request.method == 'POST':
        form = AboutInfoForm(request.POST, request.FILES, instance=about_instance)  
        if form.is_valid():
            form.save()
            data_saved = True
            return redirect('backhome')  
    else:
        form = AboutInfoForm(instance=about_instance)
    
    return render(request, 'back_info_about.html', {'form': form, 'data_saved': data_saved})




@login_required
def profile(request):
    user = request.user

    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)











def service(request):
    services = Service.objects.first()
    return render(request, 'services.html', {'services': services})



