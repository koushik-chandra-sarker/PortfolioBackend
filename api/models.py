from django.db import models


class About(models.Model):
    aboutYourself = models.CharField(max_length=500, null=True, blank=True)
    cv_link = models.CharField(max_length=150, null=True, blank=True)
    facebook_link = models.CharField(max_length=150, null=True, blank=True)
    linkdin_link = models.CharField(max_length=150, null=True, blank=True)
    github_link = models.CharField(max_length=150, null=True, blank=True)


class Skill(models.Model):
    def directory_path(instance, filename):
        return 'images/user/user_{0}/skill/{1}'.format(instance.user.id, filename)

    skill = models.CharField(max_length=150)
    about = models.ForeignKey(About, default=None, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=directory_path, null=True, blank=True)


class Experience(models.Model):
    def directory_path(instance, filename):
        return 'images/user/user_{0}/experience/{1}'.format(instance.user.id, filename)

    company_name = models.CharField(max_length=80)
    company_logo = models.ImageField(upload_to=directory_path, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=50)
    address = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    about = models.ForeignKey(About, default=None, null=True, blank=True, on_delete=models.CASCADE)


class Education(models.Model):
    def directory_path(instance, filename):
        return 'images/user/user_{0}/education/{1}'.format(instance.user.id, filename)

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    institution_name = models.CharField(max_length=100)
    institution_logo = models.ImageField(upload_to=directory_path, null=True, blank=True)
    education = models.CharField(max_length=100)
    group = models.CharField(max_length=25)
    CGPA = models.FloatField()
    Out_Of = models.FloatField()
    about = models.ForeignKey(About, default=None, null=True, blank=True, on_delete=models.CASCADE)


class Profession(models.Model):
    profession = models.CharField(max_length=70)


class Profile(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    about = models.OneToOneField(About, on_delete=models.CASCADE)
    # CAT=models.OneToOneField(Contact, on_delete=models.CASCADE,parent_link=True)
    professions = models.ManyToManyField(Profession, blank=True)

    def Professions(self):
        return '  ,  '.join(str(f) for f in self.professions.all())

    def Service(self):
        return '  ,  '.join(str(f) for f in self.service_set.all())

    def Project(self):
        return '  ,  '.join(str(f) for f in self.project_set.all())

    def Testimonial(self):
        return '  ,  '.join(str(f) for f in self.testimonial_set.all())

    def Contact(self):
        return '  ,  '.join(str(f) for f in self.contact_set.all())

    def Message(self):
        return '  ,  '.join(str(f) for f in self.message_set.all())


class ProjectCategory(models.Model):
    name = models.CharField(max_length=45)


class Project(models.Model):
    def directory_path(instance, filename):
        return 'images/user/user_{0}/thumb/{1}'.format(instance.user.id, filename)

    title = models.CharField(max_length=45)
    thumbnail = models.ImageField(upload_to=directory_path)
    profile = models.ForeignKey(Profile, default=None, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(ProjectCategory, default=None, null=True, blank=True, on_delete=models.SET_NULL)

    def Images(self):
        return '  ,  '.join(str(f) for f in self.projectimage_set.all())


class ProjectImage(models.Model):
    def directory_path(instance, filename):
        return 'images/user/user_{0}/{1}'.format(instance.user.id, filename)

    project = models.ForeignKey(Project, default=None, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=directory_path)


class Service(models.Model):
    service_name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50,
                            help_text='Give a Fontawesome i tag. Ex: <i class="fas fa-chess-queen"/>, '
                                      'from https://fontawesome.com/')
    profile = models.ForeignKey(Profile, default=None, null=True, blank=True, on_delete=models.CASCADE)


class Testimonial(models.Model):
    def directory_path(instance, filename):
        return 'images/user/user_{0}/testimonial/{1}'.format(instance.user.id, filename)

    def video_directory_path(instance, filename):
        return 'videos/user/user_{0}/testimonial/{1}'.format(instance.user.id, filename)

    clientName = models.CharField(max_length=50)
    company = models.CharField(max_length=60)
    speech = models.CharField(max_length=500)
    image = models.ImageField(upload_to=directory_path)
    video = models.FileField(upload_to=video_directory_path)
    profile = models.ForeignKey(Profile, default=None, null=True, blank=True, on_delete=models.CASCADE)


class Contact(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, default=None, null=True, blank=True, on_delete=models.CASCADE)


class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    profile = models.ForeignKey(Profile, default=None, null=True, blank=True, on_delete=models.CASCADE)
