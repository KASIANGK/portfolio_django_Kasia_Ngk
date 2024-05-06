from django.contrib import admin
from django.urls import path
from app_about import views as about_views 
from app_skills import views as skills_views 
from app_portfolio import views as portfolio_views
from app_testimonials import views as add_testimonial_views 
from app_services import views as modify_service_views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', about_views.home, name="home"),  
    path('portfolio_details/', about_views.portfolio_details, name='portfolio_details'),
    path('update_about/', about_views.update_about, name='update_about'),
    path('about/', about_views.about, name='about'),
    path('logout/', about_views.logout_view, name='logout'),  
    path('profile/', about_views.profile, name='profile'),
    path('login/', about_views.login, name='login'),  
    path('homeback/', about_views.homeback, name="homeback"),
    path('update_skills/', skills_views.update_skills, name='update_skills'), 
    path('add_portfolio_item/', portfolio_views.add_portfolio_item, name='add_portfolio_item'),
    path('homeback/testi/', add_testimonial_views.add_testimonial, name='add_testimonial'),
    path('modify/', modify_service_views.modify_services, name='modify_services'),  
    path('service/', modify_service_views.service, name='service'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path
from app_about import views as about_views 
from app_skills import views as skills_views 
from app_portfolio import views as portfolio_views
from app_testimonials import views as add_testimonial_views 
from app_services import views as modify_service_views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', about_views.home, name="home"),  
    path('portfolio_details/', about_views.portfolio_details, name='portfolio_details'),
    path('update_about/', about_views.update_about, name='update_about'),
    path('about/', about_views.about, name='about'),
    path('logout/', about_views.logout_view, name='logout'),  
    path('profile/', about_views.profile, name='profile'),
    path('login/', about_views.login, name='login'),  
    path('homeback/', about_views.homeback, name="homeback"),
    path('update_skills/', skills_views.update_skills, name='update_skills'), 
    path('add_portfolio_item/', portfolio_views.add_portfolio_item, name='add_portfolio_item'),
    path('homeback/testi/', add_testimonial_views.add_testimonial, name='add_testimonial'),
    path('modify/', modify_service_views.modify_services, name='modify_services'),  
    path('service/', modify_service_views.service, name='service'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
