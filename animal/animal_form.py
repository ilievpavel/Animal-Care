from django import forms

from animal.models import Animal


class AnimalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'input-group'

    class Meta:
        model = Animal
        fields = '__all__'
