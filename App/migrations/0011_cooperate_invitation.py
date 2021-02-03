# Generated by Django 3.1 on 2020-08-15 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_auto_20200814_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperate_invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('reason', models.TextField(default='我想邀请你成为协作者')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.file')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.user')),
            ],
            options={
                'db_table': 'cooperate_invitation',
            },
        ),
    ]
