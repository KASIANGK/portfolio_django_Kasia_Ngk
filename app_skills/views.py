from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Skill
from .forms import AddSkillForm

def update_skills(request):
    skills = Skill.objects.all()
    data_saved = False
    
    if request.method == 'POST':
        form = AddSkillForm(request.POST)
        if form.is_valid():
            new_skill = form.save()
            data_saved = True
            return redirect('update_skills')
    else:
        form = AddSkillForm()

    return render(request, 'skills_editable.html', {'form': form, 'skills': skills, 'data_saved': data_saved,})




def home(request):
    skills = Skill.objects.all()
    return render(request, 'home.html', {'skills': skills})