from django.forms import ModelForm
from .models import Reservation

class ReservationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Reservation
        fields = ["table", "date_time", "desc", "name"]
