# Generated by Django 4.0.2 on 2022-02-15 18:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppSoftDesk', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='contributors',
            options={'verbose_name': 'Contributor', 'verbose_name_plural': 'Contributors'},
        ),
        migrations.AlterModelOptions(
            name='issues',
            options={'verbose_name': 'Issue', 'verbose_name_plural': 'Issues'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.RenameField(
            model_name='issues',
            old_name='projetct_id',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='comment_id',
        ),
        migrations.RemoveField(
            model_name='issues',
            name='tile',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='assignee_user_id',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='project_id',
        ),
        migrations.AddField(
            model_name='issues',
            name='assignee_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignee_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issues',
            name='author_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issues',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 15, 19, 2, 9, 176054)),
        ),
        migrations.AddField(
            model_name='issues',
            name='project_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppSoftDesk.projects'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='author_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 15, 19, 2, 9, 176054)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='issue_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppSoftDesk.issues'),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='permission',
            field=models.CharField(choices=[('restricted', 'Contributeur'), ('all', 'Auteur')], default='restricted', max_length=50),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='projet_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppSoftDesk.projects'),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='role',
            field=models.CharField(choices=[('author', 'Auteur'), ('responsable', 'Responsable'), ('Contributor', 'Contributeur')], default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='contributors',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issues',
            name='priority',
            field=models.CharField(choices=[('Low', 'Faible'), ('Middle', 'Moyenne'), ('High', 'Elevée')], default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='issues',
            name='status',
            field=models.CharField(choices=[('En cours', 'En cours'), ('Terminée', 'Terminée')], default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='issues',
            name='tag',
            field=models.CharField(choices=[('Bug', 'Bug'), ('Amelioration', 'Amelioration'), ('Tâche', 'Tâche')], default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='projects',
            name='author_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projects',
            name='type',
            field=models.CharField(choices=[('Web', 'Web'), ('iOS', 'iOS'), ('Android', 'Android')], default='Web', max_length=7),
        ),
    ]