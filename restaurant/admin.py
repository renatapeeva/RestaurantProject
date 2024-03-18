from django.contrib import admin
from .models import Restaurant, Employee, Table, Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("table", "name", "date_time",)
    list_filter = ("table__restaurant",)

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Employee)
admin.site.register(Table)
admin.site.register(Restaurant)

# Register your models here.
