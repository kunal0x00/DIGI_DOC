# Generated by Django 5.0 on 2023-12-11 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_user_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='file_encrypted',
            field=models.FileField(blank=True, upload_to='uploads/encrypted/'),
        ),
        migrations.AddField(
            model_name='user',
            name='key',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='file',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
