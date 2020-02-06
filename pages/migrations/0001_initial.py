# Generated by Django 3.0.3 on 2020-02-06 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(db_index=True, max_length=50, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('keywords', models.CharField(max_length=255)),
                ('content', models.TextField(null=True)),
            ],
            options={
                'db_table': 'pages',
                'ordering': ['id'],
            },
        ),
    ]
