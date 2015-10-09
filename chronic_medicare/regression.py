import pandas as pd
from sklearn.linear_model import LinearRegression

from .models import ChronicConditionLinearRegression
from .forms import ChronicConditionLinearRegressionForm
from .constants import DEPENDENT_VARIABLE


def run_linear_regression(input_data):
    # df is standard short form for DataFrame object
    df = pd.read_csv(input_data['input_file'])

    independent = input_data['parameters'][0]
    try:
        dependent = input_data['dependent']
    except KeyError:
        dependent = DEPENDENT_VARIABLE

    # FIXME: Implement dummy variable logic
    X = df[[independent]].fillna(df[independent].mean())
    Y = df[[dependent]].fillna(df[dependent].mean())

    reg = LinearRegression()
    reg.fit(X, Y)
    results = {
        'parameters': independent,
        'coefficient': reg.coef_,
        'constant': reg.intercept_,
        'r_squared': reg.score(X, Y),
        }
    return results


def save_linear_regression(results):
    form = ChronicConditionLinearRegressionForm(results)
    if form.is_valid():
        regression_results, created = ChronicConditionLinearRegression.objects.get_or_create(**form.cleaned_data)
        return regression_results
    else:
        raise Exception("Invalid regression results!")
