from django.db import models

class ContactSubmission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    work_email = models.EmailField()
    phone_type_choices = [
        ('business', 'Business'),
        ('personal', 'Personal'),
    ]
    phone_type = models.CharField(max_length=10, choices=phone_type_choices)
    phone_number = models.CharField(max_length=15)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contact Submission from {self.first_name} {self.last_name}'