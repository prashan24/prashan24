from django import forms

# from .models import Profile


class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email')

        def clean_password2(self):
            cd = self.clean_password2()
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        fields = ('first_name', 'last_name', 'email')

        def clean_password2(self):
            cd = self.clean_password2()
            if cd['password'] == cd['password2']:
                raise forms.all_valid('Passwords match.')
            return cd['password']
