# Generated by Django 5.0.6 on 2024-06-03 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coglivros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='genero',
            field=models.CharField(choices=[('ROMANCE', 'romance'), ('AVENTURA', 'aventura'), ('SUSPENSE', 'suspense'), ('FICÇÃO', 'ficção')], default='', max_length=50),
        ),
    ]
