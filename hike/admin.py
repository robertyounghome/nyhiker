from django import forms
from django.contrib import admin
from .models import Range, Mountain, Hike, HikeDetail, Challenge, Condition, Grade

class HikeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['range'].required = True
        self.fields['rating'].required = False
        self.fields['duration'].required = False

    class Meta:
        model = Hike
        fields = '__all__'

@admin.register(Hike)
class HikeAdmin(admin.ModelAdmin):
    form = HikeForm
    list_display = ('name', 'name_small')

class MountainForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['range'].required = True
        self.fields['rating'].required = False

    class Meta:
        model = Mountain
        fields = '__all__'

@admin.register(Mountain)
class MountainAdmin(admin.ModelAdmin):
    form = MountainForm
    list_display = ('name', 'range', 'rating')
    list_editable = ('range', 'rating')

admin.site.register(Range)
admin.site.register(HikeDetail)
admin.site.register(Challenge)
admin.site.register(Condition)
admin.site.register(Grade)