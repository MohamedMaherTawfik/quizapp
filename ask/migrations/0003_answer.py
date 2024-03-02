# Generated by Django 4.2 on 2024-03-02 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ask', '0002_remove_questions_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User_Answer', to=settings.AUTH_USER_MODEL)),
                ('question', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ask.questions')),
            ],
        ),
    ]
