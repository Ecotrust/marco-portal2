# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def create_homepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    Page = apps.get_model('wagtailcore.Page')
    Site = apps.get_model('wagtailcore.Site')
    HomePage = apps.get_model('home.HomePage')

    # Delete the default homepage
    Page.objects.get(id=2).delete()

    # Create content type for homepage model
    homepage_content_type, created = ContentType.objects.get_or_create(
        model='homepage', app_label='home', defaults={'app_label': 'Homepage'})

    # Create a new homepage
    homepage = HomePage.objects.create(
        title="Homepage",
        slug='home',
        content_type=homepage_content_type,
        path='00010001',
        depth=2,
        numchild=0,
        url_path='/home/',
    )

    # Create a site with the new homepage set as the root
    Site.objects.create(
        hostname='localhost', root_page=homepage, is_default_site=True)


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    run_before = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'), # Required for Wagtail 2.11+ migration without locale.
    ]

    operations = [
        migrations.RunPython(create_homepage),
    ]
