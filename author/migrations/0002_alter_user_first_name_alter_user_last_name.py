# Generated by Django 4.1 on 2022-08-21 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("author", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="First Name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Last Name"
            ),
        ),
    ]
