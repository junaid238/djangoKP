from django import forms
from .models import Article , Student_obj
STATUS_CHOICES = (
    (1, ("employed")),
    (2, ("not employed")),
    (3, ("student")),
    (4, ("None")),
    (5, ("others"))
)

EMP_STATUS = (
    ( 1,("Programmer")),
    ( 2, ("Lead")),
    ( 3, ("Manager")),
    ( 4, ("BA")),
    ( 5, ("others"))
)
class NameForm(forms.ModelForm):
	class Meta:
		model = Student_obj
		fields = ('name', )
	your_name = forms.CharField(label='Your name', max_length=100)
	status = forms.ChoiceField(choices = STATUS_CHOICES, label="", initial='', widget=forms.Select(), required=True)
	date = forms.DateTimeField()
	roll_no = forms.DecimalField()
	resume = forms.FileField()

class DemoForm(forms.Form):
	employee = forms.CharField(label='Your name', max_length=100)
	status = forms.ChoiceField(choices = EMP_STATUS, label="", initial='', widget=forms.Select(), required=True)
	DOJ = forms.DateTimeField()



class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ('title', 'text')
		