from django.shortcuts import render
from .models import Customer
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from .forms import AccountOpeningForm
from django.contrib.auth.decorators import login_required


def account_activation_sent(request):
    return render(request, 'customers/account_activation_sent.html')

def account_activation_successful(request):
    return render(request, 'customers/account_activation_successful.html')

def register(request):
    if request.method == 'POST':
        form = AccountOpeningForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # User is not active until email is confirmed
            user.save()
            # Send email confirmation
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message = render_to_string('customers/activate_account_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('account_activation_sent')
    else:
        form = AccountOpeningForm()
    return render(request, 'customers/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Customer.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Customer.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('account_activation_successful')
    else:
        return render(request, 'customers/activation_invalid.html')

@login_required
def profile(request):
    return render(request, 'customers/profile.html') 

@login_required
def confirm_logout(request):
    return render(request, 'customers/confirm_logout.html')