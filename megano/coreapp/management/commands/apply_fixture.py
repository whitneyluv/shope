from django.core.management import BaseCommand
from django.db.utils import IntegrityError
import os


class Command(BaseCommand):
    """
    Applies all fixtures to the database
    """
    def handle(self, *args, **options):
        self.stdout.write("=" * 40 +
                          "\nApply all fixtures to the database\n\n")
        total_error = list()
        paths = [
            # сначала юзер нужен и так далее
            #loaddata - загрузить
            #dumpdata выгрузить - python -Xutf8 manage.py  dumpdata coreapp.banner --output data.json
            #приминять фикстуры  python manage.py apply_fixture

            "coreapp/fixtures/groups.json",
            "coreapp/fixtures/banners.json",
        ]
        for path in paths:
            is_error = os.system(f"python -Xutf8 manage.py loaddata {path}")
            if is_error != 0:
                self.stdout.write(self.style.ERROR(
                    f"ERROR! Fixture {path} is not loaded\n"
                ))
                total_error.append(path)
            else:
                self.stdout.write(self.style.SUCCESS(
                    f"Fixture {path} applied successfully\n\n"
                ))
        if not len(total_error):
            self.stdout.write(self.style.SUCCESS(
                "Fixtures applied successfully\n" + "=" * 40))
        else:
            self.stdout.write(self.style.ERROR(
                "When loading fixtures, the following fell off:\n{errors}\n".format(
                    errors='\n'.join(total_error)
                ) + "=" * 40))