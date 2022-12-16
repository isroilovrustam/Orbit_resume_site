from django.contrib import admin
from .models import Home, About, Degree, Category, Portfolio, Service, Work, Education, Happy_Client, Medium
# Register your models here.

class DegreeAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage', 'created_at']


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['created_at']


admin.site.register(Home)
admin.site.register(About)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Category)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Service)
admin.site.register(Work)
admin.site.register(Education)
admin.site.register(Happy_Client)
admin.site.register(Medium)