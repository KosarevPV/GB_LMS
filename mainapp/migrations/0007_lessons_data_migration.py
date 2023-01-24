import json

from django.db import migrations


def forwards_func(apps, schema_editor):
    # Get model
    Lesson = apps.get_model("mainapp", "Lesson")
    # Create model's objects
    Courses = apps.get_model("mainapp", "Courses")

    with open("mainapp/fixtures/003_lessons.json", encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        Lesson.objects.create(
            course=Courses.objects.get(pk=int(item["fields"]["course"])),
            num=item["fields"]["num"],
            title=item["fields"]["title"],
            description=item["fields"]["description"],
            description_as_markdown=item["fields"]["description_as_markdown"],
            created=item["fields"]["created"],
            updated=item["fields"]["updated"],
        )


def reverse_func(apps, schema_editor):
    # Get model
    Lesson = apps.get_model("mainapp", "Lesson")
    # Delete objects
    Lesson.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0006_courses_data_migration"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
