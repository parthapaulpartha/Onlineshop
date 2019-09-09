# Generated by Django 2.2.3 on 2019-08-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0006_kids_boy_image_kids_girl_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='electronics_desktop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='e_desktop')),
                ('title', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Electronics Desktop',
            },
        ),
        migrations.CreateModel(
            name='electronics_head_phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='e_h_phone')),
                ('title', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Electronics Head Phone',
            },
        ),
        migrations.CreateModel(
            name='electronics_laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='e_laptop')),
                ('title', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Electronics Laptop',
            },
        ),
        migrations.CreateModel(
            name='electronics_phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='e_phone')),
                ('title', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Electronics Phone',
            },
        ),
        migrations.CreateModel(
            name='gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='gift')),
                ('title', models.CharField(max_length=30)),
                ('price', models.CharField(default='', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Gift',
            },
        ),
        migrations.CreateModel(
            name='watch_kids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='w_kids')),
                ('title', models.CharField(max_length=30)),
                ('price', models.CharField(default='', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Watch Kids',
            },
        ),
        migrations.CreateModel(
            name='watch_man',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='w_man')),
                ('title', models.CharField(max_length=30)),
                ('price', models.CharField(default='', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Watch Man',
            },
        ),
        migrations.CreateModel(
            name='watch_woman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='w_woman')),
                ('title', models.CharField(max_length=30)),
                ('price', models.CharField(default='', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Watch Woman',
            },
        ),
        migrations.AlterModelOptions(
            name='kids_boy_image',
            options={'verbose_name_plural': 'Kids Boy Image'},
        ),
        migrations.AlterModelOptions(
            name='kids_girl_image',
            options={'verbose_name_plural': 'Kids Girl Image'},
        ),
        migrations.AlterModelOptions(
            name='man_images',
            options={'verbose_name_plural': 'Man Images'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'Profile'},
        ),
        migrations.AlterModelOptions(
            name='slider_images',
            options={'verbose_name_plural': 'Slider Image'},
        ),
        migrations.AlterModelOptions(
            name='woman_images',
            options={'verbose_name_plural': 'Woman Images'},
        ),
    ]
