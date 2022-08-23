# Generated by Django 4.1 on 2022-08-22 17:25

from django.db import migrations, models
import portfolio.models
import storages.backends.ftp


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0008_about_profilepic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="about",
            name="cv",
            field=models.FileField(
                blank=True,
                null=True,
                storage=storages.backends.ftp.FTPStorage(
                    base_url="ftp://portfolio@files.iamkoushik.com:KoushiK30&30@iamkoushik.com:21"
                ),
                upload_to=portfolio.models.About.directory_path,
            ),
        ),
        migrations.AlterField(
            model_name="about",
            name="profilePic",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=storages.backends.ftp.FTPStorage(
                    base_url="ftp://portfolio@files.iamkoushik.com:KoushiK30&30@iamkoushik.com:21"
                ),
                upload_to=portfolio.models.About.profile_directory_path,
            ),
        ),
        migrations.AlterField(
            model_name="education",
            name="institution_logo",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=storages.backends.ftp.FTPStorage(
                    base_url="ftp://portfolio@files.iamkoushik.com:KoushiK30&30@iamkoushik.com:21"
                ),
                upload_to=portfolio.models.Education.directory_path,
            ),
        ),
        migrations.AlterField(
            model_name="experience",
            name="company_logo",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=storages.backends.ftp.FTPStorage(
                    base_url="ftp://portfolio@files.iamkoushik.com:KoushiK30&30@iamkoushik.com:21"
                ),
                upload_to=portfolio.models.Experience.directory_path,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="thumbnail",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=storages.backends.ftp.FTPStorage(
                    base_url="ftp://portfolio@files.iamkoushik.com:KoushiK30&30@iamkoushik.com:21"
                ),
                upload_to=portfolio.models.Project.directory_path,
            ),
        ),
        migrations.AlterField(
            model_name="projectimage",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=storages.backends.ftp.FTPStorage(
                    base_url="ftp://portfolio@files.iamkoushik.com:KoushiK30&30@iamkoushik.com:21"
                ),
                upload_to=portfolio.models.ProjectImage.directory_path,
            ),
        ),
        migrations.AlterField(
            model_name="skill",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=storages.backends.ftp.FTPStorage(
                    base_url="ftp://portfolio@files.iamkoushik.com:KoushiK30&30@iamkoushik.com:21"
                ),
                upload_to=portfolio.models.Skill.directory_path,
            ),
        ),
        migrations.AlterField(
            model_name="testimonial",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=storages.backends.ftp.FTPStorage(
                    base_url="ftp://portfolio@files.iamkoushik.com:KoushiK30&30@iamkoushik.com:21"
                ),
                upload_to=portfolio.models.Testimonial.directory_path,
            ),
        ),
        migrations.AlterField(
            model_name="testimonial",
            name="video",
            field=models.FileField(
                blank=True,
                null=True,
                storage=storages.backends.ftp.FTPStorage(
                    base_url="ftp://portfolio@files.iamkoushik.com:KoushiK30&30@iamkoushik.com:21"
                ),
                upload_to=portfolio.models.Testimonial.video_directory_path,
            ),
        ),
    ]
