from django.contrib.admin.apps import AdminConfig


class BlogAdminConfig(AdminConfig):
    default_site = 'myblog.admin.BlogAdminSite'