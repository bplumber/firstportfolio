from django.forms import ModelForm
from .models import projects

class ProjectForm(ModelForm):
    class Meta:
        model = projects
        fields = '__all__'


class GeeksForm(ModelForm):
    class Meta:
        model = projects
        fields = '__all__'