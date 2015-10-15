from django.shortcuts import render, redirect, get_object_or_404
from .models import ChronicConditionLinearRegression
from .forms import ChronicConditionAnalysisQueryForm
from .regression import run_linear_regression, save_linear_regression


def home(request):
    return render(request, 'index.html')

def query_view(request):
    if request.method == 'POST':
        form = ChronicConditionAnalysisQueryForm(request.POST)
        if form.is_valid():
            regression_results = run_linear_regression(form.cleaned_data)
            saved_regression = save_linear_regression(regression_results)
            return redirect('chronic:results_detail', pk=saved_regression.pk)
    else:
        form = ChronicConditionAnalysisQueryForm()
    return render(request, 'chronic_medicare/query.html', {'form': form})


def results_list(request):
    results = ChronicConditionLinearRegression.objects.all()
    return render(request, 'chronic_medicare/results_list.html', {'results': results})


def results_detail(request, pk):
    result = get_object_or_404(ChronicConditionLinearRegression, pk=pk)
    return render(request, 'chronic_medicare/results_detail.html', {'result': result})
