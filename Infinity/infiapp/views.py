from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from .models import ContactSubmission

# Create your views here.
# def home(request):
#     return render(request,'base.html')

def index(request):
    return render(request,'index.html')





def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Save to the database
            ContactSubmission.objects.create(
                full_name=full_name,
                email=email,
                message=message
            )
            
            # Send email to admin
            send_mail(
                f'Contact Us message from {full_name}',
                message,
                email,
                ['maqsood.a.ansari@gmail.com'],  # replace with your admin email
                fail_silently=False,
            )
            
            # Display success message
            messages.success(request, 'Your enquiry/request is submitted successfully and we will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact_us.html', {'form': form})

