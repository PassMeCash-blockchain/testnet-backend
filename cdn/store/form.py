from django import forms
class AssetForm(forms.Form):
    choices=(
        ('CSS','css'),
         ('JS','javascript'),
          ('IMAGE','image'),
           ('PDF','pdf'),

    )
    Description = forms.CharField(label="Description",max_length=500)
    FileType  = forms.ChoiceField(label="File Type",choices=choices)
    file      = forms.FileField(label='Upload File') # for creating file input
