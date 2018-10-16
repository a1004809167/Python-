from  django  import forms

class Bookform(forms.Form):
    book_name = forms.CharField(max_length=150)
    book_rate = forms.CharField(max_length=50)
    # book_date = forms.DateTimeField(null=True, blank=True)
class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128)
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)
#     password2 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)
class UsersForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128)
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)
    password2 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)