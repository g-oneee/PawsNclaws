from django import forms
from app.models import Adopt


class AdoptForm(forms.ModelForm):
    class Meta:
        model = Adopt
        # fields = '__all__'
        # fields = []
        fields = ['petCategory', 'Breed', 'name' ,'image', 'gender' , 'location' ,'age', 'vacinated' , 'vaccineinfo' ,'neutered_or_spayed', 'contact_info' , 'good_with_dogs' ,'good_with_kids', 'shots_upto_date' , 'needs_loving_adopter' ] 