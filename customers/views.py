from django.shortcuts import render, get_object_or_404
from .models import Customer, DeliveryOrder, OrderTracking
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from .forms import AccountOpeningForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


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
        uid = force_str(urlsafe_base64_decode(uidb64))
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

# def order_list(request):
#     orders = DeliveryOrder.objects.all()
#     return render(request, 'customers/order_list.html', {'orders': orders})

class OrderListView(ListView, LoginRequiredMixin):
    models = DeliveryOrder
    context_object_name = 'orders'
    template_name = 'customers/order_list.html'

    def get_queryset(self):
        return DeliveryOrder.objects.all()
  

def order_detail(request, order_id):
    order = get_object_or_404(DeliveryOrder, id=order_id)
    tracking_info = OrderTracking.objects.filter(order=order)
    return render(request, 'customers/order_detail.html', {'order': order, 'tracking_info': tracking_info})

def track_order(request, tracking_number):
    order = get_object_or_404(DeliveryOrder, tracking_number=tracking_number)
    tracking_info = OrderTracking.objects.filter(order=order)
    tracking_data = [{'status': t.status, 'location': t.location, 'timestamp': t.timestamp} for t in tracking_info]
    return JsonResponse({'order': order.id, 'tracking_number': order.tracking_number, 'status': order.status, 'tracking_info': tracking_data})


# class OrderListView(ListView, LoginRequiredMixin):
#     models = DeliveryOrder
#     context_object_name = 'orders'
#     template_name = 'customers/order_list.html'

#     def get_queryset(self):
#         return DeliveryOrder.objects.filter(customer=self.request.user)
    
# def track_order(request, tracking_number):
#     order = get_object_or_404(DeliveryOrder, tracking_number=tracking_number)
#     tracking_info = OrderTracking.objects.filter(order=order)
#     tracking_data = [{'status': t.status, 'location': t.location, 'timestamp': t.timestamp} for t in tracking_info]
#     return JsonResponse({'order': order.id, 'tracking_number': order.tracking_number, 'status': order.status, 'tracking_info': tracking_data})
