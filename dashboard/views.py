from django.http import JsonResponse
from django.shortcuts import render
from dashboard.models import Dataset
from django.core import serializers

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})


def pivot_data(request):
    dataset = Dataset.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
 