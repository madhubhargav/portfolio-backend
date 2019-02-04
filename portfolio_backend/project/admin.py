from django.contrib import admin

from project.models import Project, ProjectDescription


admin.site.register(Project)
admin.site.register(ProjectDescription)
