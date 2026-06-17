from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='skill_keywords',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
