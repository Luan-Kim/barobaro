from django import forms
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

        # 항상 해당 필드의 값을 리턴한다.
        return cd['password2']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

# class LoginForm(forms.Form):
#     username = forms.CharField(error_messages={"required" : "아이디를 입력해주세요"}, max_length=32, label = "사용자 이름")
#     password = forms.CharField(error_messages={"required" : "비밀번호를 입력해주세요."},
#     			max_length= 64, label = "비밀번호", widget=forms.PasswordInput)
#
#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data.get('username')
#         password = cleaned_data.get('password')
#
#         if password and username :
#             try:
#                 user = User.objects.get(username = username)
#             except User.DoesNotExist:
#                 self.add_error("username", "아이디가 존재하지 않습니다.")
#                 return
#
#             if not check_password(password, user.password):
#                 self.add_error("password", "비밀번호가 일치하지 않습니다.")
#             else:
#                 self.user_id = user.id