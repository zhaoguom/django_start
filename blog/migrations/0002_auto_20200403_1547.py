# Generated by Django 2.2.9 on 2020-04-03 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('article_title', models.TextField()),
                ('article_content', models.TextField()),
                ('article_detail', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ArticleModel',
        ),
    ]