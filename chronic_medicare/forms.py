from django import forms
from .models import MedicareFile, ChronicConditionLinearRegression
from .constants import CHRONIC_COLUMN_NAMES


class ChronicConditionAnalysisQueryForm(forms.Form):
    '''
    This form validates that valid query choices have been made
    '''
    parameters = forms.MultipleChoiceField(choices=CHRONIC_COLUMN_NAMES,
        widget=forms.CheckboxSelectMultiple())
    create_dummies = forms.BooleanField(required=False)
    input_file = forms.ModelChoiceField(queryset=MedicareFile.objects.all())

    def clean_input_file(self):
        return self.cleaned_data['input_file'].csv_file

class ChronicConditionLinearRegressionForm(forms.ModelForm):
    '''
    This model form is used to validate output from
    sklearn LinearRegression to ensure data saved is legitimate
    '''
    class Meta:
        model = ChronicConditionLinearRegression
        fields = ['parameters', 'coefficient', 'constant', 'r_squared']
