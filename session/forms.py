from django.forms import ModelForm

import shekho.session.models

class SessionForm(ModelForm):
    class Meta:
        model = shekho.session.models.Session
