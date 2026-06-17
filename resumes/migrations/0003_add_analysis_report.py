from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0002_add_skill_keywords'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_score', models.FloatField()),
                ('match_percent', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('job_description', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='analysis_reports', to='jobs.jobdescription')),
                ('resume', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='analysis_reports', to='resumes.resume')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
