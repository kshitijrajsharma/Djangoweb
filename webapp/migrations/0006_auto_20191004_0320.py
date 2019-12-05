# Generated by Django 2.2.5 on 2019-10-04 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_profile_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='Type',
            field=models.CharField(blank=True, choices=[('Government', 'Government'), ('Private', 'Private')], max_length=40),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]