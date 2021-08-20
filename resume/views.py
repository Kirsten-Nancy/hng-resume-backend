from resume.forms import ContactForm
from django.shortcuts import redirect, render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print('form', form.data)
        if form.is_valid():
            form.save()
            send_mail(form.data['subject'], form.data['message'], form.data['email'] , ['chingskorjep@gmail.com'])
            return redirect('resume:success')
    form = ContactForm()
    return render(request, 'resume/index.html',{'form': form})

def success(request):
    return render(request, 'resume/success.html')