from unittest.util import _MAX_LENGTH
from django.db import models

#HARDCODED NEEDS TO BE GENERIC LATER
class data (models.Model):
    clip = models.IntegerField('clip')
    forclosuredate = models.DateField('Forclosure Date',max_length=255)
    boughtdate = models.DateField('Bought Date',max_length=255)
    mortgageamount = models.IntegerField('Mortagage Amount')
    recordingdate = models.DateField('Recording Date',max_length=255)
    mortgagedate = models.DateField('Mortgage date',max_length=255)

    def __str__(self):
        return self.title

##RAWDATA PATHFILES
class rawdata (models.Model):
    RawData = models.FileField(upload_to= 'rawdata/')

    def __str__(self):
        return self.title
