from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView, ListView
from django.contrib.auth import get_user_model
from Repair.models import Repair, Status
from django.views import View
from Repair.forms import CustomerForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Repair.mixins import RepairMixin

# Create your views here.

User = get_user_model()


@method_decorator(login_required, name='dispatch')
class GetViewUserRepair(RepairMixin, ListView):
    template_name = "get_repairs.html"
    model = Repair

    def get_queryset(self):
        """Возвращаем заявки пользователя"""

        _repair = self._get_repair_filter(self.request.user)
        print(_repair)
        return Repair.objects.filter(**_repair)


class DetailRepair(View):
    template_name = "detail.html"

    def get(self, request, pk):
        repair = get_object_or_404(Repair, pk=pk)
        context = {
            'repair': repair
        }
        return render(request, self.template_name, context)


class ListViewRepair(ListView):
    template_name = "home.html"
    model = Repair

    def get_queryset(self):
        """Возвращаем заявки для пользователей по статусу заявки"""
        return Repair.objects.filter(status=Status.CREATED)
    #refactor


@method_decorator(login_required, name='dispatch')
class CreateRepair(FormView):
    template_name = 'create_repair.html'
    form_class = CustomerForm
    success_url = '/'

    def form_valid(self, form):
        repair = form.save()
        repair.user.add(self.request.user)
        return super().form_valid(form)