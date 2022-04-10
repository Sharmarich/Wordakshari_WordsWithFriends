from django.forms import ModelForm
from .models import UserInfo

class UserInfoForm(ModelForm):

	class Meta:
		model = UserInfo
		fields = '__all__'