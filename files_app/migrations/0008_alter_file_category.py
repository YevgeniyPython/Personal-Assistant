# Generated by Django 5.1.1 on 2024-10-10 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files_app', '0007_file_resource_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='category',
            field=models.CharField(choices=[('image', 'Image'), ('document', 'Document'), ('video', 'Video'), ('audio', 'Audio'), ('other', 'Other')], max_length=20),
        ),
    ]
