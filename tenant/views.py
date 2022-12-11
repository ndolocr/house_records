from django.shortcuts import render
from tenant.models import Tenant

# Create your views here.

def view_all_tenants(request):
    all_tenants = Tenant.objects.all()

    context = {
        "all_tenants": all_tenants,
    }

    return render(request, 'tenant/index.html', context)