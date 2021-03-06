# Generated by Django 3.0.5 on 2020-04-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default=1, upload_to='Project', verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
    ]
