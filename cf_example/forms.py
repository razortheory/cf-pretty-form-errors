from crispy_forms.layout import ButtonHolder, Submit
from django import forms
from django.core.validators import RegexValidator

from cf_pretty_form_errors.form_mixins import PrettyFormPlaceholdersMixin


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Incorrect phone format.")


class ExampleForm(PrettyFormPlaceholdersMixin, forms.Form):
    name = forms.CharField()
    phone = forms.CharField(required=False, validators=[phone_regex],
                            help_text='Phone in format \'+999999999\'. Up to 15 digits allowed')
    email = forms.EmailField()
    link = forms.URLField()
    gender = forms.CharField(
        widget=forms.Select(choices=(
            ('m', 'Male'),
            ('f', 'Female'),
            (None, 'Other (raises error)'),
        )),
        error_messages={'required': "You have to select gender."},
        help_text='Gender'
    )
    age = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper.layout.append(
            ButtonHolder(Submit('submit', value='Submit'))
        )
