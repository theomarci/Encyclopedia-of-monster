from .models import monsters
import django_filters


class UserFilter(django_filters.FilterSet):
    class Meta:
        # reach the data base
        model = monsters
        # select the right fields to filter objects of the table
        fields = ['Type']




