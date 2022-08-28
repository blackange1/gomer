# Generated by Django 4.1 on 2022-08-22 11:48

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='заголовок')),
                ('style', models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary'), ('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('info', 'info'), ('light', 'light'), ('dark', 'dark')], max_length=32, verbose_name='стиль')),
                ('body', tinymce.models.HTMLField(help_text='для більш вражаючого ефекту використовуйте тег hr', verbose_name='контент')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публікувати')),
            ],
            options={
                'verbose_name_plural': 'Оголошення',
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='заголовок')),
                ('class_name_icon', models.CharField(choices=[('flaticon-001-swing', '001-swing'), ('flaticon-002-bricks', '002-bricks'), ('flaticon-003-feeding-bottle', '003-feeding-bottle'), ('flaticon-004-balloons', '004-balloons'), ('flaticon-005-marker', '005-marker'), ('flaticon-006-spinning-top', '006-spinning-top'), ('flaticon-007-sandbox', '007-sandbox'), ('flaticon-008-tambourine', '008-tambourine'), ('flaticon-009-bib', '009-bib'), ('flaticon-010-slide', '010-slide'), ('flaticon-011-mat', '011-mat'), ('flaticon-012-kite', '012-kite'), ('flaticon-013-brush', '013-brush'), ('flaticon-014-blackboard', '014-blackboard'), ('flaticon-015-potty', '015-potty'), ('flaticon-016-apple', '016-apple'), ('flaticon-017-toy-car', '017-toy-car'), ('flaticon-018-ball', '018-ball'), ('flaticon-019-pencil', '019-pencil'), ('flaticon-020-rattle', '020-rattle'), ('flaticon-021-juice-box', '021-juice-box'), ('flaticon-022-drum', '022-drum'), ('flaticon-023-girl', '023-girl'), ('flaticon-024-shape-toy', '024-shape-toy'), ('flaticon-025-sandwich', '025-sandwich'), ('flaticon-026-paper-boat', '026-paper-boat'), ('flaticon-027-xylophone', '027-xylophone'), ('flaticon-028-kindergarten', '028-kindergarten'), ('flaticon-029-clock', '029-clock'), ('flaticon-030-crayons', '030-crayons'), ('flaticon-031-bell', '031-bell'), ('flaticon-032-book', '032-book'), ('flaticon-033-blocks', '033-blocks'), ('flaticon-034-popsicle', '034-popsicle'), ('flaticon-035-table', '035-table'), ('flaticon-036-boy', '036-boy'), ('flaticon-037-toys', '037-toys'), ('flaticon-038-locker', '038-locker'), ('flaticon-039-seesaw', '039-seesaw'), ('flaticon-040-puzzle', '040-puzzle'), ('flaticon-041-abacus', '041-abacus'), ('flaticon-042-synthesizer', '042-synthesizer'), ('flaticon-043-teddy-bear', '043-teddy-bear'), ('flaticon-044-scissors', '044-scissors'), ('flaticon-045-cookies', '045-cookies'), ('flaticon-046-bucket', '046-bucket'), ('flaticon-047-backpack', '047-backpack'), ('flaticon-048-paper-plane', '048-paper-plane'), ('flaticon-049-cutlery', '049-cutlery'), ('flaticon-050-fence', '050-fence')], help_text="вигляд та ім'я класу дивись нижче", max_length=64, verbose_name="ім'я класу іконки")),
                ('description', models.CharField(max_length=256, verbose_name='опис')),
                ('mass', models.SmallIntegerField(default=0, help_text='позиція має бути унікальним для кожногї зручності', unique=True, verbose_name='позиція')),
            ],
            options={
                'verbose_name_plural': 'Зручності',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="дотримуйтесь заздалегіть вибраного шаблону. Приклад: прізвище, ім'я або ім'я та по батькові", max_length=32, verbose_name="ім'я")),
                ('profession', models.CharField(blank=True, help_text='перше слово з маленької букви', max_length=32, null=True, verbose_name='професія')),
                ('photo', models.ImageField(help_text='фото має бути розміром 100x100 px', upload_to='testimonials', verbose_name='фото')),
                ('text', models.CharField(help_text='всі відгуки мають місти однакову кількість слів для кращого дизайну', max_length=256, verbose_name='відгук')),
            ],
            options={
                'verbose_name_plural': 'Відгуки',
            },
        ),
    ]