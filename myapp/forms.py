from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Snipper
from django.core.validators import RegexValidator

class NameWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        super().__init__([
            forms.TextInput(),
            forms.TextInput()
        ], attrs)

    def decompress(self, value):
        # 'firstvalue secondvalue'
        if value:
            return value.split('')
        return['','']

class NameField(forms.MultiValueField):

    widget = NameWidget

    def __init__(self, *args, **kwargs):

        fields = {
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+', 'Enter a valid First name (Only Letters)')
            ]),
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+', 'Enter a valid Second name (Only Letters)')
            ]),
        }

        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        #data_list = {'firstvalue', 'secondvalue'}
        return f'{data_list[0]} {data_list[1]}'

class ContactForm(forms.Form):
    name = NameField()
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(choices={('question', 'Question'), ('other', 'Other')})
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'email',
            'category',
            'body',
            Submit('submit', 'Submit', css_class='btn_success')
        )

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snipper
        fields = ('name', 'body')