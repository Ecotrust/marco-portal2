# Generated by Django 2.2.3 on 2019-11-07 01:32

from django.db import migrations
from django.conf import settings
if settings.WAGTAIL_VERSION > 1:
    import wagtail.core.blocks as wagtail_core_blocks
    import wagtail.core.fields as wagtail_core_fields
else:
    import wagtail.core.blocks as wagtail_core_blocks
    import wagtail.core.fields as wagtail_core_fields


class Migration(migrations.Migration):

    dependencies = [
        ('ocean_stories', '0014_oceanstorysection_stream_body'),
    ]

    operations = [
        # migrations.AlterField(
        #     model_name='oceanstorysection',
        #     name='body',
        #     field=wagtail_core_fields.StreamField([('rich_text', wagtail_core_blocks.RichTextBlock()), ('raw_html', wagtail_core_blocks.RawHTMLBlock())], blank=True, null=True),
        # ),
    ]
