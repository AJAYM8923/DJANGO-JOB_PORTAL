from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from employers.models import JobPost
from .forms import JobApplicationForm
from .models import JobApplication
from .models import  contact as contact_data
from django.db.models import Q
# Create your views here.
def home(request):
    jobs = JobPost.objects.filter(is_verified=True).order_by('-posted_at')
    return render(request,"home.html",{"jobs":jobs})

def login(request):
    error=None
    if request.method == "POST":
        
        email=request.POST.get("email")
        password=request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user :
            auth_login(request,user)
            return redirect("home")
        else:
            error = "Invalid email or password"

    return render(request,"login.html",{'error':error})

def register(request):
    user=None
    error=None
    if request.method == "POST":
        name=request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        username=email
        


        try:
           user = User.objects.create_user( username=username, email=email, password=password)
           user.first_name = name
           user.save()
           return redirect("login")
        except Exception as e:
            error = str(e)

    return render(request,"register.html",{"error":error})

def logout(request):
    auth_logout(request)
    return redirect("home")
@login_required
def apply_to_job(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)

    # Check if already applied
    if JobApplication.objects.filter(user=request.user, job=job).exists():
        return render(request, 'already_applied.html')

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()
            return redirect('user_dashboard')
    else:
        form = JobApplicationForm()

    return render(request, 'apply_to_job.html', {'form': form, 'job': job})
@login_required
def user_dashboard(request):
    applications = JobApplication.objects.filter(user=request.user)
    return render(request, 'user_dashboard.html', {'applications': applications})

def all_jobs(request):
    jobs = JobPost.objects.filter(is_verified=True).order_by('-posted_at')
    

    return render(request, "all_jobs.html", { "jobs": jobs })


def job_search_results(request):
    query = request.GET.get('q')
    jobs = []

    if query:
        jobs = JobPost.objects.filter(
            Q(title__icontains=query) |
            Q(company__icontains=query) |
            Q(location__icontains=query) |
            Q(description__icontains=query),
            is_verified=True
        ).order_by('-posted_at')

    return render(request, 'job_search_results.html', {'jobs': jobs, 'query': query})

def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        contact_obj=contact_data(name=name,email=email,message=message)
        contact_obj.save()
        return redirect("home")

    return render(request,"contact.html")

