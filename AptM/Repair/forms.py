from django import forms

from Repair.models import Repair, TypeRepair


class CustomerForm(forms.ModelForm):

    description = forms.CharField(
        label="Описание поломки",
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    type_repair = forms.ModelChoiceField(
        label="Выберите тип задачи",
        widget=forms.Select(attrs={"class": "form-control"}),
        queryset=TypeRepair.objects.all()
    )

    class Meta:
        model = Repair
        fields = ('description', 'type_repair')