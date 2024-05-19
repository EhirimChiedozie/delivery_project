from django.forms import ModelForm
from .models import Reviews

class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'email', 'subject', 'message']