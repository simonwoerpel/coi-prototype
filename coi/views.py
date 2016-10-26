from django.db.models import Q
from django.shortcuts import render

from .models import Record


def search(request):
    q = request.GET.get('q')
    if q:
        qs = Record.objects.filter(
            Q(author_name__icontains=q) | Q(conflict__icontains=q)
        ).distinct()
        return render(request, 'coi/base.html', {'q': q, 'results': qs})
    return render(request, 'coi/base.html')
