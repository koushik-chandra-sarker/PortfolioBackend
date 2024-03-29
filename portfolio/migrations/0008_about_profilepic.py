# Generated by Django 4.1 on 2022-08-22 16:40

from django.db import migrations, models
import portfolio.models
import storages.backends.ftp


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0007_alter_about_aboutyourself"),
    ]

    operations = [
        migrations.AddField(
            model_name="about",
            name="profilePic",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=storages.backends.ftp.FTPStorage(),
                upload_to=portfolio.models.About.profile_directory_path,
            ),
        ),
    ]
