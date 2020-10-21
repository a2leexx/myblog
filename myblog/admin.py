from django.contrib import admin


class BlogAdminSite(admin.AdminSite):
    site_header = 'Администрирование блога'
    site_title = 'Администрирование блога'