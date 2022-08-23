from rest_framework import serializers

from author.models import User
from author.serializers import AuthorSerializer
from portfolio.models import About, Skill, Experience, Education, Profession, Project, Service, Testimonial, Contact, \
    Message


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['profession']


class AboutSerializer(serializers.ModelSerializer):
    professions = ProfessionSerializer(read_only=True)

    class Meta:
        model = About
        fields = ['displayName', 'profilePic', 'professions', 'aboutYourself', 'cv', 'facebook_link', 'linkdin_link',
                  'github_link']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill', 'image']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['company_name', 'company_name', 'start_date', 'end_date', 'position', 'address', 'description']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['start_date', 'end_date', 'institution_name', 'institution_logo', 'education', 'group', 'CGPA',
                  'Out_Of']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'thumbnail', 'category']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_name', 'description', 'icon']


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['clientName', 'company', 'speech', 'image', 'video']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['phone', 'email', 'address']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message']


class AllData(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', "about", "skills", "experiences", "educations",
                  "projects", "services", "testimonials", "contact"]

    about = serializers.SerializerMethodField("get_about")
    skills = serializers.SerializerMethodField("get_skills")
    experiences = serializers.SerializerMethodField("get_experiences")
    educations = serializers.SerializerMethodField("get_educations")
    projects = serializers.SerializerMethodField("get_projects")
    services = serializers.SerializerMethodField("get_services")
    testimonials = serializers.SerializerMethodField("get_testimonials")
    contact = serializers.SerializerMethodField("get_contact")

    def get_about(self, arg):
        qs = About.objects.get(user=arg.id)
        serializer = AboutSerializer(instance=qs)
        return serializer.data

    def get_skills(self, arg):
        qs = Skill.objects.all()
        serializer = SkillSerializer(instance=qs, many=True)
        return serializer.data

    def get_experiences(self, arg):
        qs = Experience.objects.filter(user=arg.id)
        serializer = ExperienceSerializer(instance=qs, many=True)
        return serializer.data

    def get_educations(self, arg):
        qs = Education.objects.filter(user=arg.id)
        serializer = EducationSerializer(instance=qs, many=True)
        return serializer.data

    def get_projects(self, arg):
        qs = Project.objects.filter(user=arg.id)
        serializer = ProjectSerializer(instance=qs, many=True)
        return serializer.data

    def get_services(self, arg):
        qs = Service.objects.filter(user=arg.id)
        serializer = ServiceSerializer(instance=qs, many=True)
        return serializer.data

    def get_testimonials(self, arg):
        qs = Testimonial.objects.filter(user=arg.id)
        serializer = TestimonialSerializer(instance=qs, many=True)
        return serializer.data

    def get_contact(self, arg):
        qs = Contact.objects.filter(user=arg.id)
        serializer = ContactSerializer(instance=qs, many=True)
        return serializer.data
