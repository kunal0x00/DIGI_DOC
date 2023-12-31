# Generated by Django 5.0 on 2023-12-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_encryptedfile_encrypted_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='encryptedfile',
            name='file_encrypted',
            field=models.FileField(blank=True, upload_to='uploads/encrypted/'),
        ),
        migrations.AddField(
            model_name='encryptedfile',
            name='key',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='encryptedfile',
            name='file',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
