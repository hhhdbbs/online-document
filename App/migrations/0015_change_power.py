# Generated by Django 3.1 on 2020-08-17 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_comment_reminder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Change_power',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.file')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.user')),
            ],
            options={
                'db_table': 'change_power',
            },
        ),
    ]
