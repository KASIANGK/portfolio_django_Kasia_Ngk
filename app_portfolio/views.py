from django.shortcuts import render, redirect
from .forms import PortfolioForm
from .models import PortfolioItem

def add_portfolio_item(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = PortfolioForm()
    
    return render(request, 'portfolio.html', {'form': form})

def home(request):
    portfolio_item = PortfolioItem.objects.all()
    return render(request, 'home.html', {'portfolio_item': portfolio_item})