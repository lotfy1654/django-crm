from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):

    email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', "placeholder": "Email"}))
    first_name = forms.CharField(label="First Name", max_length=30, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', "placeholder": "First Name"}))
    last_name = forms.CharField(label="Last Name", max_length=30, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', "placeholder": "Last Name"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    # Overriding the init method to add bootstrap classes to the default fields
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # Adding bootstrap classes
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        # Adding placeholders
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password2'].widget.attrs['placeholder'] = "Confirm Password"

        # Adding labels
        self.fields['username'].label = "Username"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

        # Addding help texts
        self.fields['username'].help_text = "<small class='form-text text-muted'>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>"
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


# Record Form
# class RecordForm(forms.ModelForm):
#     class Meta:
#         model = Record
#         fields = '__all__'

#         def __init__(self ,*args, **kwargs):
#             super(RecordForm, self).__init__(*args, **kwargs)
#             for field in self.fields:
#                 self.fields[field].widget.attrs['class'] = 'form-control'


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label="First Name", widget=forms.TextInput(
        attrs={"placeholder": "First Name", "class": "form-control"}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={"placeholder": "Last Name", "class": "form-control"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={"placeholder": "Email", "class": "form-control"}))
    phone = forms.CharField(required=True, widget=forms.TextInput(
        attrs={"placeholder": "Phone", "class": "form-control"}))
    address = forms.CharField(required=True, widget=forms.TextInput(
        attrs={"placeholder": "Address", "class": "form-control"}))
    city = forms.CharField(required=True, widget=forms.TextInput(
        attrs={"placeholder": "City", "class": "form-control"}))
    state = forms.CharField(required=True, widget=forms.TextInput(
        attrs={"placeholder": "State", "class": "form-control"}))
    zipcode = forms.CharField(required=True, widget=forms.TextInput(
        attrs={"placeholder": "Zipcode", "class": "form-control"}))

    class Meta:
        model = Record
        exclude = ("user",)
        fields = ('first_name', 'last_name', 'email', 'phone',
                  'address', 'city', 'state', 'zipcode')

    # def __init__(self, *args, **kwargs):
    #     super(AddRecordForm, self).__init__(*args, **kwargs)
