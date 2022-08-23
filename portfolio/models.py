from django.conf import settings
from django.db import models

from author.models.user_model import User
from storages.backends.ftp import FTPStorage

fs = FTPStorage()


class Profession(models.Model):
    profession = models.CharField(max_length=70)

    def __str__(self):
        return self.profession


class About(models.Model):
    def directory_path(instance, filename):
        return 'doc/cv/user_{0}/{1}'.format(instance.user.id, filename)

    def profile_directory_path(instance, filename):
        return 'images/profilePic/user_{0}/{1}'.format(instance.user.id, filename)

    displayName = models.CharField(max_length=70)
    profilePic = models.ImageField(upload_to=profile_directory_path, storage=fs, null=True, blank=True)
    professions = models.ForeignKey(Profession, on_delete=models.CASCADE)
    aboutYourself = models.TextField(max_length=500, null=True, blank=True)
    cv = models.FileField(storage=fs, upload_to=directory_path, null=True, blank=True)
    facebook_link = models.CharField(max_length=150, null=True, blank=True)
    linkdin_link = models.CharField(max_length=150, null=True, blank=True)
    github_link = models.CharField(max_length=150, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Skill(models.Model):
    def directory_path(instance, filename):
        return 'images/skill/user_{0}/{1}'.format(instance.user.id, filename)

    skill = models.CharField(max_length=150)
    image = models.ImageField(upload_to=directory_path, storage=fs, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Experience(models.Model):
    def directory_path(instance, filename):
        return 'images/experience/user_{0}/{1}'.format(instance.user.id, filename)

    company_name = models.CharField(max_length=80)
    company_logo = models.ImageField(upload_to=directory_path, storage=fs, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=50)
    address = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)


class Education(models.Model):
    def directory_path(instance, filename):
        return 'images/education/user_{0}/{1}'.format(instance.user.id, filename)

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    institution_name = models.CharField(max_length=100)
    institution_logo = models.ImageField(upload_to=directory_path, storage=fs, null=True, blank=True)
    education = models.CharField(max_length=100)
    group = models.CharField(max_length=25)
    CGPA = models.FloatField()
    Out_Of = models.FloatField()
    user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)


class ProjectCategory(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Project(models.Model):
    def directory_path(instance, filename):
        return 'images/thumb/user_{0}/{1}'.format(instance.user.id, filename)

    title = models.CharField(max_length=45)
    thumbnail = models.ImageField(upload_to=directory_path, storage=fs, null=True, blank=True)
    user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(ProjectCategory, default=None, null=True, blank=True, on_delete=models.SET_NULL)

    def Images(self):
        return '  ,  '.join(str(f) for f in self.projectimage_set.all())


class ProjectImage(models.Model):
    def directory_path(instance, filename):
        return 'images/project/project_{0}/{1}'.format(instance.project.id, filename)

    project = models.ForeignKey(Project, default=None, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=directory_path, storage=fs, null=True, blank=True)


class Service(models.Model):
    service_name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50,
                            help_text='Give a Fontawesome i tag. Ex: <i class="fas fa-chess-queen"/>, '
                                      'from https://fontawesome.com/')
    user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)


class Testimonial(models.Model):
    def directory_path(instance, filename):
        return 'images/testimonial/user_{0}/{1}'.format(instance.user.id, filename)

    def video_directory_path(instance, filename):
        return 'videos/testimonial/user_{0}/{1}'.format(instance.user.id, filename)

    clientName = models.CharField(max_length=50)
    company = models.CharField(max_length=60)
    speech = models.CharField(max_length=500)
    image = models.ImageField(upload_to=directory_path, storage=fs, null=True, blank=True)
    video = models.FileField(upload_to=video_directory_path, storage=fs, null=True, blank=True)
    user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)


class Contact(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)


class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)
