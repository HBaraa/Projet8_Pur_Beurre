from django.core.management.base import BaseCommand, CommandError
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("first", type=int, help="a number")
        parser.add_argument("--option1", default="default", help="option1 value")

    def handle(self, *args, **options):
        # name = get_random_string(length=12)
        # self.stdout.write(name)
        # print(f'First:{options["first"]}')
        if options["first"] < 100:
            self.stdout.write(self.style.SUCCESS("Good Job"))
        else:
            raise CommandError("the numbre is not accepted")
        self.stdout.write(f'the value of --option1 is {options["option1"]}')
