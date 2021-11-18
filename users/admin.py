from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Vacations, LogList

admin.site.site_header = 'Панель администратора'


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'phone', 'email']

    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительные данные', {'fields': ('third_name', 'phone', 'full_name', 'id_num', 'status', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительные данные', {'fields': ('third_name', 'phone', 'full_name', 'id_num', 'status', )}),
    )

    search_fields = ('first_name', 'last_name', 'email', 'phone', 'full_name', 'username', 'id_num',)
    list_filter = ('status',)


class VacationsAdmin(admin.ModelAdmin):
    list_display = ['doc_name', 'first_name', 'last_name', 'full_name', 'start_vacation', 'end_vacation', 'doc_date',
                    'vacation_status']
    ordering = ('doc_date',)


class LogListAdmin(admin.ModelAdmin):
    list_display = ['doc_name', 'first_name', 'last_name', 'full_name', 'doc_date', 'doc_status']
    ordering = ('doc_date',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Vacations, VacationsAdmin)
admin.site.register(LogList, LogListAdmin)
