# Generated by Django 2.2.3 on 2019-07-10 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
if settings.WAGTAIL_VERSION > 1:
    import wagtail.images.models as wagtail_image_models
    import wagtail.search.index as wagtail_search_index
else:
    import wagtail.images.models as wagtail_image_models
    import wagtail.search.index as wagtail_search_index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PortalImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('file', models.ImageField(height_field='height', upload_to=wagtail_image_models.get_upload_to, verbose_name='file', width_field='width')),
                ('width', models.IntegerField(editable=False, verbose_name='width')),
                ('height', models.IntegerField(editable=False, verbose_name='height')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('focal_point_x', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_y', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_width', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_height', models.PositiveIntegerField(blank=True, null=True)),
                ('file_size', models.PositiveIntegerField(editable=False, null=True)),
                # ('file_hash', models.CharField(blank=True, editable=False, max_length=40)),
                ('creator', models.CharField(blank=True, max_length=255)),
                ('creator_URL', models.URLField(blank=True)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text=None, through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags')),
                ('uploaded_by_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='uploaded by user')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_search_index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='PortalRendition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_spec', models.CharField(db_index=True, max_length=255)),
                # ('file', models.ImageField(height_field='height', upload_to=wagtail_image_models.get_rendition_upload_to, width_field='width')),
                ('file', models.ImageField(height_field=b'height', width_field=b'width', upload_to=b'images')),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('focal_point_key', models.CharField(blank=True, default='', editable=False, max_length=16)),
                # ('filter', models.ForeignKey(related_name='+', to='wagtailimages.Filter', on_delete=django.db.models.deletion.CASCADE)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='renditions', to='base.PortalImage')),
            ],
            options={
                'unique_together': {('image', 'filter_spec', 'focal_point_key')},
            },
        ),
    ]
