"""
URL configuration for job_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from users import views as user_views
from employers import views as employer_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.contrib.auth import views as auth_views

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('login/', user_views.login, name='login'),
    path('register/', user_views.register, name='register'),
    path('logout/', user_views.logout, name='logout'),
    path('post_job/', employer_views.post_job, name='post_job'),
    path('job/<int:job_id>/', employer_views.job_detail, name='job_detail'),
    path('apply/<int:job_id>/', user_views.apply_to_job, name='apply_to_job'),
    path('employer_dashboard/', employer_views.employer_dashboard, name='employer_dashboard'),
    path('user_dashboard/', user_views.user_dashboard, name='user_dashboard'),
    path("all_jobs/", user_views.all_jobs, name='all_jobs'),
    path("job_search_results/", user_views.job_search_results, name="job_search_results"),
    path('contact/',user_views.contact,name="contact"),
   
   # Password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)