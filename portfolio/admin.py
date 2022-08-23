from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from portfolio.models import Profession, Service, Project, ProjectCategory, ProjectImage, About, Skill, Experience, \
    Education, Testimonial, Contact, Message


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


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    # inlines = []
    # list_display = ['aboutYourself', 'cv', 'facebook_link', 'linkdin_link', 'github_link']
    pass

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill', 'image', 'user']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'company_name', 'start_date', 'end_date', 'position', 'address', 'description',
                    'user']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['start_date', 'end_date', 'institution_name', 'institution_logo', 'education', 'group', 'CGPA',
                    'Out_Of', 'user']


@admin.register(Profession)
class ProfessionsAdmin(admin.ModelAdmin):
    list_display = ['profession']


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ['title', 'thumbnail', 'category', 'Images']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'description', 'icon', 'user']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['clientName', 'company', 'speech', 'image', 'video', 'user']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', 'address', 'user']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'user']
