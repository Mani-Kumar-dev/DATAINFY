from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from innerpages.forms import ContactForm
from innerpages.models import ContactSubmission


# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            company_name = form.cleaned_data['company_name']
            work_email = form.cleaned_data['work_email']
            phone_type = form.cleaned_data['phone_type']
            phone_number = form.cleaned_data['phone_number']
            job_title = form.cleaned_data['job_title']
            department = form.cleaned_data['department']
            job_role = form.cleaned_data['job_role']
            country = form.cleaned_data['country']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            zip_code = form.cleaned_data['zip_code']
            address = form.cleaned_data['address']
            message = form.cleaned_data['message']
            
            # Save to the database
            ContactSubmission.objects.create(
                first_name=first_name,
                last_name=last_name,
                company_name=company_name,
                work_email=work_email,
                phone_type=phone_type,
                phone_number=phone_number,
                job_title=job_title,
                department=department,
                job_role=job_role,
                country=country,
                state=state,
                city=city,
                zip_code=zip_code,
                address=address,
                message=message
            )
            
            # Send email to admin
            send_mail(
                f'Contact Us message from {first_name} {last_name}',
                message,
                work_email,
                ['maqsood.a.ansari@gmail.com'],  # replace with your admin email
                fail_silently=False,
            )
            
            # Display success message
            messages.success(request, 'Your enquiry/request is submitted successfully and we will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request,"contact.html")
def Virtualization(request):
    return render(request,"Virtualization.html")
def migrations_page(request):
    return render(request,"migrations_page.html")
def security(request):
    return render(request,"security.html")
def mobility(request):
    return render(request,"mobility.html")
def backup(request):
    return render(request,"backup.html")
def storage(request):
    return render(request,"storage.html")