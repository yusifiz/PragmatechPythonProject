# Generated by Django 3.2.8 on 2021-10-30 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Product Name', max_length=200)),
                ('color', models.SmallIntegerField(choices=[(1, 'black'), (3, 'red'), (2, 'yellow')], max_length=100)),
                ('price', models.SmallIntegerField(default=1)),
            ],
        ),
    ]