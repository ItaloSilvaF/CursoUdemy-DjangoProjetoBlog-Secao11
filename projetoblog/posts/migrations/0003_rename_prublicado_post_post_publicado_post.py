# Generated by Django 4.0.6 on 2022-07-27 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_autor_post_alter_post_categoria_post_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='prublicado_post',
            new_name='publicado_post',
        ),
    ]
