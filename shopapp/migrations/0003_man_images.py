# Generated by Django 2.2.3 on 2019-08-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_auto_20190804_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='man_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='man_images')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
    ]
