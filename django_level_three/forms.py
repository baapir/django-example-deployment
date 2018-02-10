from django import forms
from django.core import validators
from django_level_three.models import newuser

##create new validator!!
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('name should start with z')

class testform(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='email again')
    text = forms.CharField(widget=forms.Textarea)
    ##max_lenght should be 0 for validator
    botcatcer = forms.CharField(required=False, widget=forms.HiddenInput)
    second_botcatcher = forms.CharField(required=False,
                                        validators=[validators.MaxLengthValidator(0)],
                                        widget=forms.HiddenInput)


    ##clean a specific field
    def clean_botcatcer(self):
        botcacher = self.cleaned_data['botcatcer']
        if len(botcacher):
            raise forms.ValidationError('gotcha bot _|_ !!')
        return botcacher


    ##clean whole form you chek everything here!!! like verify email
    def clean(self):
        cleaned_all = super().clean()
        email = cleaned_all['email']
        vmail = cleaned_all['verify_email']
        if email != vmail:
            raise forms.ValidationError('email dosent match!!')

class signupssform(forms.ModelForm):
      #form fields go here with validators
      class Meta:
          model = newuser
          fields = ['FirstName', 'LastName', 'Email']
          ##exclude = []





