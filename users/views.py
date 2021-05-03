from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm
from django.core.mail import send_mail
from ecommerce.settings import EMAIL_HOST_USER

#**************************User Registration**************************************
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created !!!')

            if request.method == 'POST':
                subject = 'Successfully Registered'
                message = 'Your account is Successfully Registered'
                recepient = str(form['email'].value())
                send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
