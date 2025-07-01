from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from employers.models import JobPost
from users.models import JobApplication
# Create your views here.
@login_required
def post_job(request):
    if request.method == "POST":
        # Handle the form submission for posting a job
        title = request.POST.get("title")
        company = request.POST.get("company")
        location = request.POST.get("location")
        job_type = request.POST.get("type")
        salary = request.POST.get("salary")
        category = request.POST.get("category")
        experience = request.POST.get("experience")
        qualifications = request.POST.get("qualifications")
        description = request.POST.get("description")
        responsibilities = request.POST.get("responsibilities")
        skills = request.POST.get("skills")
        deadline = request.POST.get("deadline")

        # Create a new JobPost instance
        job_post = JobPost(
            employer=request.user,
            title=title,
            company=company,
            location=location,
            type=job_type,
            salary=salary,
            category=category,
            experience=experience,
            qualifications=qualifications,
            description=description,
            responsibilities=responsibilities,
            skills=skills,
            deadline=timezone.datetime.strptime(deadline, "%Y-%m-%d").date(),
        )
        
        # Save the job post to the database
        job_post.save()
        return redirect('home')
    return render(request, "post_job.html")  # Render the post job page

def job_detail(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    return render(request, 'job_detail.html', {'job': job})
@login_required
def employer_dashboard(request):
    jobs = JobPost.objects.filter(employer=request.user)
    # Create a dict: job -> list of applications
    applications_by_job = {}
    for job in jobs:
        applications = JobApplication.objects.filter(job=job)
        applications_by_job[job] = applications
    return render(request, 'employer_dashboard.html', {'applications_by_job': applications_by_job})
