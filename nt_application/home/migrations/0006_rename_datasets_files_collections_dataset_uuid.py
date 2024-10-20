# Generated by Django 4.1.13 on 2024-08-28 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_remove_collections_dataset_uuid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Datasets',
            new_name='Files',
        ),
        migrations.AddField(
            model_name='collections',
            name='Dataset_UUID',
            field=models.ForeignKey(default=45, editable=False, on_delete=django.db.models.deletion.PROTECT, to='home.files'),
            preserve_default=False,
        ),
    ]
