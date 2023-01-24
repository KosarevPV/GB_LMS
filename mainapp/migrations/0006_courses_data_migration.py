import json

from django.db import migrations


def forwards_func(apps, schema_editor):
    # Get model
    Courses = apps.get_model("mainapp", "Courses")
    # Create model's objects

    with open("mainapp/fixtures/002_courses.json", encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        Courses.objects.create(
            name=item["fields"]["name"],
            description=item["fields"]["description"],
            description_as_markdown=item["fields"]["description_as_markdown"],
            cost=item["fields"]["cost"],
            cover=item["fields"]["cover"],
            created=item["fields"]["created"],
            updated=item["fields"]["updated"],
        )


def reverse_func(apps, schema_editor):
    # Get model
    Courses = apps.get_model("mainapp", "Courses")
    # Delete objects
    Courses.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0005_news_data_migration"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
