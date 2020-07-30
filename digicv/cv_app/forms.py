from django import forms
from cv_app.models import User

class FormName(forms.ModelForm):

    class Meta():
        fields = ["name","email","company"]
        model = User
        # name = forms.CharField()
        # email = forms.EmailField()
        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'})
        }

    def get_queryset(self):
        pass