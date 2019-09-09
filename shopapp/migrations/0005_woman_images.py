# Generated by Django 2.2.3 on 2019-08-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_man_images_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='woman_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='woman_images')),
                ('title', models.CharField(max_length=30)),
                ('price', models.CharField(default='', max_length=20)),
            ],
        ),
    ]