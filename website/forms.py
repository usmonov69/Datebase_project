from django  import forms
from .models import Member
from django.contrib.auth.forms import  UserCreationForm , UserChangeForm
class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ['fname','lname','email','age','passwd' , 'phone_num', ]

class MemberCreateForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = Member
		fields = ('fname','lname','email','age','passwd')


class MemberChangeForm(UserChangeForm):
	class Meta:
		model = Member
		fields =('fname', 'lname', 'email', 'age',)

