# Generated by Django 3.2.9 on 2021-11-12 17:07

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=False, help_text='To display this menu, check this box. ')),
                ('is_user_menu', models.BooleanField(default=False, help_text='If this menu is the User Menu, check this box.')),
                ('footer', models.BooleanField(default=False, help_text='Select to display this menu in the footer rather than in the nav bar. The footer has enough room for four menus.')),
                ('order', models.PositiveSmallIntegerField(default=1, help_text='The order that this menu appears. Lower numbers appear first.')),
            ],
            options={
                'ordering': ('footer', 'order'),
            },
        ),
        migrations.CreateModel(
            name='MenuEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, help_text='Note: URLs starting with http:// will open in a new window.', max_length=4096, null=True)),
                ('show_divider_underneath', models.BooleanField(default=False)),
                ('display_options', models.CharField(choices=[('A', 'Always display'), ('I', 'Display only to logged-in users'), ('O', 'Display only to anonymous users'), ('S', 'Display only to staff and administrators')], default='A', max_length=1)),
                ('menu', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='menu.menu')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
