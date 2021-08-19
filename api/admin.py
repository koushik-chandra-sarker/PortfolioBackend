from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from api.models import Profile, Profession, Service, Project, ProjectCategory, ProjectImage, About, Skill, Experience, \
    Education


class ServiceInline(admin.StackedInline):
    model = Service
    extra = 1


class ProjectImageInline(NestedStackedInline):
    model = ProjectImage
    extra = 1


class ProjectInline(NestedStackedInline):
    model = Project
    extra = 1
    inlines = [ProjectImageInline]


class SkillInline(NestedStackedInline):
    model = Skill
    extra = 1


class ExperienceInline(NestedStackedInline):
    model = Experience
    extra = 1


class EducationInline(NestedStackedInline):
    model = Education
    extra = 1


@admin.register(Profile)
class ProfileAdmin(NestedModelAdmin):
    inlines = [ServiceInline, ProjectInline]
    list_display = ['firstname', 'lastname', 'about', 'Professions', 'Service', 'Project', 'Testimonial',
                    'Contact', 'Message']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [SkillInline, ExperienceInline, EducationInline, ]
    list_display = ['aboutYourself', 'cv_link', 'facebook_link', 'linkdin_link', 'github_link']


@admin.register(Profession)
class ProfessionsAdmin(admin.ModelAdmin):
    list_display = ['profession']


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ['title', 'thumbnail', 'category', 'profile', 'Images']
