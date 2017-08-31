# coding: utf-8
# from django_select2.forms import Select2TagWidget

# from django import forms

# from .models import Channel


# class BidTypeChoices(Select2TagWidget):
#     def value_from_datadict(self, data, files, name):
#         values = super(BidTypeChoices, self).value_from_datadict(data, files, name)
#         return ",".join(values)

#     def optgroups(self, name, value, attrs=None):
#         values = value[0].split(',') if value[0] else []
#         selected = set(values)
#         subgroup = [self.create_option(name, v, v, selected, i) for i, v in enumerate(values)]
#         return [(None, subgroup, 0)]


# class ChannelForm(forms.ModelForm):
#     class Meta:
#         model = Channel
#         fields = ('bid_types',)
#         widgets = {
#             "bid_types": BidTypeChoices()
#         }
