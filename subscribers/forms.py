from django import forms
from subscribers.models import Subscribe


class SubscribeForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Subscribe
        fields = ('email',)