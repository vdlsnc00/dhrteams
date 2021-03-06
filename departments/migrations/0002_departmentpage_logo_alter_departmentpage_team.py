# Generated by Django 4.0.3 on 2022-03-10 21:20

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departmentpage',
            name='logo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='departmentpage',
            name='team',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('members', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('full_name', wagtail.core.blocks.CharBlock()), ('title', wagtail.core.blocks.CharBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock())])))]))]),
        ),
    ]
