from django.forms import ModelForm
from autos.models import Make


# Create the form class.
class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'

        # i think it's not needed because all in views.py already exist
        # this code was for the MAKE only part without simple code