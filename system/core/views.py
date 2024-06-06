# drivers/views.py
from django.views import generic
from django.urls import reverse_lazy
from .models import *
from django.shortcuts import render
from django.db.models import Sum
from datetime import date, timedelta

class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'driver_count': Driver.objects.count(),
            'vehicle_count': Vehicle.objects.count(),
            'farmer_count': Farmer.objects.count(),
            'job_count': Job.objects.count(),
            'total_revenue': Revenue.objects.aggregate(Sum('amount'))['amount__sum'],
            'recent_jobs': Job.objects.order_by('-scheduled_date')[:5],
            'recent_revenues': Revenue.objects.order_by('-date')[:5],
        }

        context['jobs_per_day'] = self.get_jobs_per_day()
        context['revenues_per_day'] = self.get_revenues_per_day()

        return render(request, self.template_name, context)

    def get_jobs_per_day(self):
        today = date.today()
        dates = [today - timedelta(days=i) for i in range(7)]
        jobs_per_day = [Job.objects.filter(scheduled_date=d).count() for d in dates]
        return {'dates': dates[::-1], 'counts': jobs_per_day[::-1]}

    def get_revenues_per_day(self):
        today = date.today()
        dates = [today - timedelta(days=i) for i in range(7)]
        revenues_per_day = [Revenue.objects.filter(date=d).aggregate(Sum('amount'))['amount__sum'] or 0 for d in dates]
        return {'dates': dates[::-1], 'amounts': revenues_per_day[::-1]}

class DriverListView(generic.ListView):
    model = Driver
    template_name = 'drivers/driver_list.html'
    context_object_name = 'drivers'

class DriverCreateView(generic.CreateView):
    model = Driver
    fields = ['name', 'email', 'phone_number', 'license_number', 'assigned_vehicle']
    template_name = 'drivers/driver_form.html'
    success_url = reverse_lazy('driver-list')

class DriverUpdateView(generic.UpdateView):
    model = Driver
    fields = ['name', 'email', 'phone_number', 'license_number', 'assigned_vehicle']
    template_name = 'drivers/driver_form.html'
    success_url = reverse_lazy('driver-list')

class DriverDeleteView(generic.DeleteView):
    model = Driver
    template_name = 'drivers/driver_confirm_delete.html'
    success_url = reverse_lazy('driver-list')


class VehicleListView(generic.ListView):
    model = Vehicle
    template_name = 'vehicles/vehicle_list.html'
    context_object_name = 'vehicles'

class VehicleCreateView(generic.CreateView):
    model = Vehicle
    fields = ['vehicle_number', 'vehicle_type', 'license_plate', 'capacity']
    template_name = 'vehicles/vehicle_form.html'
    success_url = reverse_lazy('vehicle-list')

class VehicleUpdateView(generic.UpdateView):
    model = Vehicle
    fields = ['vehicle_number', 'vehicle_type', 'license_plate', 'capacity']
    template_name = 'vehicles/vehicle_form.html'
    success_url = reverse_lazy('vehicle-list')

class VehicleDeleteView(generic.DeleteView):
    model = Vehicle
    template_name = 'vehicles/vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle-list')

class FarmerListView(generic.ListView):
    model = Farmer
    template_name = 'farmers/farmer_list.html'
    context_object_name = 'farmers'

class FarmerCreateView(generic.CreateView):
    model = Farmer
    fields = ['name', 'email', 'phone_number', 'address']
    template_name = 'farmers/farmer_form.html'
    success_url = reverse_lazy('farmer-list')

class FarmerUpdateView(generic.UpdateView):
    model = Farmer
    fields = ['name', 'email', 'phone_number', 'address']
    template_name = 'farmers/farmer_form.html'
    success_url = reverse_lazy('farmer-list')

class FarmerDeleteView(generic.DeleteView):
    model = Farmer
    template_name = 'farmers/farmer_confirm_delete.html'
    success_url = reverse_lazy('farmer-list')


class JobListView(generic.ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'

class JobCreateView(generic.CreateView):
    model = Job
    fields = ['driver', 'vehicle', 'farmer', 'pickup_location', 'destination', 'cargo', 'scheduled_date', 'scheduled_time']
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job-list')

class JobUpdateView(generic.UpdateView):
    model = Job
    fields = ['driver', 'vehicle', 'farmer', 'pickup_location', 'destination', 'cargo', 'scheduled_date', 'scheduled_time']
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job-list')

class JobDeleteView(generic.DeleteView):
    model = Job
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('job-list')

class RevenueListView(generic.ListView):
    model = Revenue
    template_name = 'revenues/revenue_list.html'
    context_object_name = 'revenues'

class RevenueCreateView(generic.CreateView):
    model = Revenue
    fields = ['job', 'amount']
    template_name = 'revenues/revenue_form.html'
    success_url = reverse_lazy('revenue-list')

class RevenueUpdateView(generic.UpdateView):
    model = Revenue
    fields = ['job', 'amount']
    template_name = 'revenues/revenue_form.html'
    success_url = reverse_lazy('revenue-list')

class RevenueDeleteView(generic.DeleteView):
    model = Revenue
    template_name = 'revenues/revenue_confirm_delete.html'
    success_url = reverse_lazy('revenue-list')