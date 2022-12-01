from django import forms
from .models import data, rawdata

#ADD INFO TO DATA
class FileForm(forms.ModelForm):
    class Meta:
        model = data
        fields = ('clip','forclosuredate','boughtdate','mortgageamount','recordingdate','mortgagedate', )

#ADD INFO TO RAWDATA
class AddFile(forms.ModelForm):
    class Meta:
        model = rawdata
        fields = ('RawData',)