# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
if settings.WAGTAIL_VERSION > 1:
    import wagtail.fields as wagtail_core_fields
else:
    import wagtail.fields as wagtail_core_fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='description',
            field=wagtail_core_fields.RichTextField(default='', blank=True),
            preserve_default=False,
        ),
    ]
