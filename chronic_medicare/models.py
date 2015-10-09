from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import numpy as np


class MedicareFile(models.Model):
    csv_file = models.FileField(upload_to='medicare-files/')

    def __str__(self):
        return self.csv_file.name.split('/')[-1]


@python_2_unicode_compatible
class ChronicConditionLinearRegression(models.Model):
    # source_file = models.ForeignKey(MedicareFile, related_name="linear_regressions")
    parameters = models.CharField(max_length=512)
    coefficient = models.FloatField(max_length=64)
    constant = models.FloatField(max_length=64, default=0)
    r_squared = models.FloatField(max_length=64)

    def __str__(self):
        return str(self.id)

    def chart_x_values(self, min_value=0, max_value=100, intervals=10):
        initial_range = np.arange(min_value, max_value, max_value/intervals)
        x_values = initial_range.tolist()
        x_values.append(max_value)
        x_values = [int(value) for value in x_values]
        return x_values

    def chart_y_values(self):
        chart_y_values = []
        for x in self.chart_x_values()[1:]:
            y_value = self.coefficient * x + self.constant
            chart_y_values.append(y_value)
        return chart_y_values
