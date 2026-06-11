from jobs.models import Job

def create_job(title, description):
    return Job.objects.create(
        title=title,
        description=description
    )