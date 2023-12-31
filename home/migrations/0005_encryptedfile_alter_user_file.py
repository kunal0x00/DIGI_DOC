# Generated by Django 5.0 on 2023-12-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_user_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='EncryptedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encrypted_file', models.FileField(upload_to='encrypted_files/')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
