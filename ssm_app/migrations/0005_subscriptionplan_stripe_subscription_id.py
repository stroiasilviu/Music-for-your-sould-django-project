# Generated by Django 4.0.5 on 2022-07-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssm_app', '0004_alter_playlist_user_alter_song_playlists'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionplan',
            name='stripe_subscription_id',
            field=models.CharField(default='price_1LL86DKyBoMgXtI9EN160apN', max_length=50),
            preserve_default=False,
        ),
    ]
