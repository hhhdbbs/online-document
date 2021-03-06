# Generated by Django 3.1 on 2020-08-11 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('creator', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'file',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('number_num', models.IntegerField(default=1)),
                ('describe', models.TextField()),
                ('icon', models.ImageField(upload_to='team_icons/%Y/%m/%d/')),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('content', models.TextField()),
                ('score', models.DecimalField(decimal_places=1, max_digits=3)),
                ('accept_num', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'templete',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_username', models.CharField(max_length=32, unique=True)),
                ('u_password', models.CharField(max_length=64)),
                ('u_email', models.EmailField(max_length=254, unique=True)),
                ('u_icon', models.ImageField(upload_to='icons/%Y/%m/%d/')),
                ('is_active', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=False)),
                ('is_manager', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Team_relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('check', models.BooleanField(default=False)),
                ('change', models.BooleanField(default=False)),
                ('delete', models.BooleanField(default=False)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.user')),
            ],
            options={
                'db_table': 'team_relation',
            },
        ),
        migrations.CreateModel(
            name='Team_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.file')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.team')),
            ],
            options={
                'db_table': 'team_record',
            },
        ),
        migrations.CreateModel(
            name='Team_collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.file')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.team')),
            ],
            options={
                'db_table': 'team_collection',
            },
        ),
        migrations.CreateModel(
            name='Personal_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.file')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.user')),
            ],
            options={
                'db_table': 'personal_record',
            },
        ),
        migrations.CreateModel(
            name='Personal_collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.file')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.user')),
            ],
            options={
                'db_table': 'personal_collection',
            },
        ),
        migrations.CreateModel(
            name='file_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateTimeField(auto_now=True)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.file')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.user')),
            ],
            options={
                'db_table': 'file_log',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.file')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.user')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
