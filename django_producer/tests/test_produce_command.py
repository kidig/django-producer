from io import StringIO

from django.core.management import call_command
from django.test import TestCase


class ProduceCommandTestCase(TestCase):
    def call_command(self, *args, **kwargs):
        out = StringIO()
        call_command(
            "produce",
            *args,
            stdout=out,
            stderr=StringIO(),
            **kwargs,
        )
        return out.getvalue()

    def test_done(self):
        out = self.call_command()
        self.assertEqual(out, "Done\n")
