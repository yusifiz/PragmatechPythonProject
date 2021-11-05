# Generated by Django 3.2.8 on 2021-10-30 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('created_at',), 'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, max_length=63, null=True, verbose_name='Muellif'),
        ),
    ]