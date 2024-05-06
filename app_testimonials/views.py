from django.shortcuts import render, redirect
from .forms import TestimonialForm
from .models import Testimonial

def add_testimonial(request):
    data_saved = False
    x = 'lol'
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data_saved = True 
            return redirect('home')  
    else:
        form = TestimonialForm()
    
    return render(request, 'homeback.html', {'form': form, 'data_saved': data_saved, 'x':x})


def home(request):
    testimonials = Testimonial.objects.all()
    print("Testimonials:", testimonials)  
    return render(request, 'home.html', {'testimonials': testimonials})