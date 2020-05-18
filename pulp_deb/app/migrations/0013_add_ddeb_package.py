# Generated by Django 2.2.16 on 2020-09-29 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_fips_checksums'),
        ('deb', '0012_auto_20200803_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='installerpackage',
            name='package_type',
            field=models.CharField(default='udeb', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='package_type',
            field=models.CharField(default='deb', max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='DebugPackage',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='deb_debugpackage', serialize=False, to='core.Content')),
                ('package', models.TextField()),
                ('source', models.TextField(null=True)),
                ('version', models.TextField()),
                ('architecture', models.TextField()),
                ('section', models.TextField(null=True)),
                ('priority', models.TextField(null=True)),
                ('origin', models.TextField(null=True)),
                ('tag', models.TextField(null=True)),
                ('bugs', models.TextField(null=True)),
                ('essential', models.BooleanField(choices=[(True, 'yes'), (False, 'no')], null=True)),
                ('build_essential', models.BooleanField(choices=[(True, 'yes'), (False, 'no')], null=True)),
                ('installed_size', models.IntegerField(null=True)),
                ('maintainer', models.TextField()),
                ('original_maintainer', models.TextField(null=True)),
                ('description', models.TextField()),
                ('description_md5', models.TextField(null=True)),
                ('homepage', models.TextField(null=True)),
                ('built_using', models.TextField(null=True)),
                ('auto_built_package', models.TextField(null=True)),
                ('multi_arch', models.TextField(choices=[('no', 'no'), ('same', 'same'), ('foreign', 'foreign'), ('allowed', 'allowed')], null=True)),
                ('breaks', models.TextField(null=True)),
                ('conflicts', models.TextField(null=True)),
                ('depends', models.TextField(null=True)),
                ('recommends', models.TextField(null=True)),
                ('suggests', models.TextField(null=True)),
                ('enhances', models.TextField(null=True)),
                ('pre_depends', models.TextField(null=True)),
                ('provides', models.TextField(null=True)),
                ('replaces', models.TextField(null=True)),
                ('relative_path', models.TextField()),
                ('sha256', models.TextField()),
                ('package_type', models.CharField(default='ddeb', max_length=255, null=True)),
            ],
            options={
                'abstract': False,
                'default_related_name': '%(app_label)s_%(model_name)s',
                'unique_together': {('relative_path', 'sha256')},
            },
            bases=('core.content',),
        ),
        migrations.CreateModel(
            name='DebugPackageFileIndex',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='deb_debugpackagefileindex', serialize=False, to='core.Content')),
                ('component', models.CharField(max_length=255)),
                ('architecture', models.CharField(max_length=255)),
                ('relative_path', models.TextField()),
                ('sha256', models.CharField(max_length=255)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deb_debugpackagefileindex', to='deb.ReleaseFile')),
            ],
            options={
                'verbose_name_plural': 'DebugPackageFileIndices',
                'default_related_name': '%(app_label)s_%(model_name)s',
                'unique_together': {('relative_path', 'sha256')},
            },
            bases=('core.content',),
        ),
    ]
