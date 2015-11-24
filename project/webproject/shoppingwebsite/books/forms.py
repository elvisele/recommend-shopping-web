from django import forms
from books.models import Person

'''

用户注册表单

'''

class PersonForm(forms.ModelForm):
	userid = forms.CharField(widget=forms.TextInput(attrs={'style': 'background-color:#123453'}))
	location = forms.CharField(widget=forms.TextInput(attrs={'style': 'background-color:#123453'}))
	age = forms.CharField(widget=forms.TextInput(attrs={'style': 'background-color:#123453'}))
	class Meta:
		model = Person
		fields = ('userid','location','age')

