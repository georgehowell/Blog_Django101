from django.db import migrations
import sorl.thumbnail.fields

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name='image',
            field=sorl.thumbnail.fields.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
