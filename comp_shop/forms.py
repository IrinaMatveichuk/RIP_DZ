from django import forms
from comp_shop.models import *
from django.contrib.auth.hashers import make_password


class CreateComputerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateComputerForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Computer
        fields = ('serial_num', 'brand', 'comp_pic', 'type', 'screen_size',
                  'installed_OS', 'processor_type', 'RAM', 'price')

    def save(self, commit=False):
        computer = super(CreateComputerForm, self).save(commit=False)
        if commit:
            computer.save()


class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'username'}),
        min_length=5, label='Логин:')
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'name'}),
        max_length=30, label='Имя:')
    surname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'surname'}),
        max_length=30, label='Фамилия:')
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'email'}), label='Email')
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'phone'}), label='Телефон')
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'address'}), label='Адрес')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password'}),
        min_length=8, label='Пароль:')
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password2'}),
        min_length=8, label='Повторите пароль:')

    def clean_password2(self):
        if self.cleaned_data.get('password') != \
                self.cleaned_data.get('password2'):
            raise forms.ValidationError('Passwords does not match')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            u = User.objects.get(username=username)
            raise forms.ValidationError('This login already uses')
        except User.DoesNotExist:
            return username

    def save(self):
        u = User()
        u.username = self.cleaned_data.get('username')
        u.password = make_password(self.cleaned_data.get('password'))
        u.first_name = self.cleaned_data.get('name')
        u.last_name = self.cleaned_data.get('surname')
        u.email = self.cleaned_data.get('email')
        u.address = self.cleaned_data.get('address')
        u.phone = self.cleaned_data.get('phone')
        u.is_staff = False
        u.is_active = True
        u.is_superuser = False
        u.save()
