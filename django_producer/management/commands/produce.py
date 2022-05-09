from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Produce all files for new apps."

    def add_arguments(self, parser) -> None:
        parser.add_argument("-c", "--config", type=str)

    def handle(self, *args, **options):
        config = options.get("config")
        print(config)
        self.stdout.write("Done\n")
