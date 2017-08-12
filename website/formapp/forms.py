#coding=utf-8
from django import forms
from myapp.models import*

TOPIC_CHOICES = (
    ('leave1','好评'),
    ('leave2','中评'),
    ('leave3','差评'),
)

class RemarkForm(forms.Form):
    subject = forms.CharField(max_length = 100,label = '标题')
    mail = forms.EmailField(label = '邮件')
    topic = forms.ChoiceField(choices = TOPIC_CHOICES,label = '评价')
    message = forms.CharField(label = '内容',widget = forms.Textarea)
    cc_myself = forms.BooleanField(required = False,label = '订阅')

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'first_name':'姓氏',
            'last_name':'名字',
            'age':'年龄',
            'email':'邮箱',
        }
