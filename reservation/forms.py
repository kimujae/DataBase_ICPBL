from django import forms

class SeatForm(forms.Form):
    class Meta:

        fields = ["seat"]
        labels = {
            "seat": "좌석",
        }

