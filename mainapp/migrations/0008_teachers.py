import json

from django.db import migrations


def forwards_func(apps, schema_editor):
    # Get model
    CourseTeachers = apps.get_model("mainapp", "CourseTeachers")
    Courses = apps.get_model("mainapp", "Courses")
    # Create model's objects

    with open("mainapp/fixtures/004_teachers.json", encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        CourseTeachers.objects.create(
            name_first=item["fields"]["name_first"],
            name_second=item["fields"]["name_second"],
            day_birth=item["fields"]["day_birth"],
        )

        teacher = CourseTeachers.objects.get(pk=item["pk"])
        teacher.course.set(list(map(lambda x: Courses.objects.get(pk=x), item["fields"]["course"])))


def reverse_func(apps, schema_editor):
    # Get model
    CourseTeachers = apps.get_model("mainapp", "CourseTeachers")
    # Delete objects
    CourseTeachers.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0007_lessons_data_migration"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
