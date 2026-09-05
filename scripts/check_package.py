"""Check an installed distribution from outside the source checkout."""

from importlib.metadata import distribution
from importlib.resources import files
from importlib.util import find_spec

import django
from django.conf import settings
from django.core.management import call_command, get_commands, load_command_class

import drip

package = distribution("django-drip")
assert package.version == drip.__version__
assert package.metadata["Requires-Python"] == ">=3.12"
assert package.requires == ["Django>=5.1"]
assert package.metadata["License-Expression"] == "MIT"
assert any(str(path).endswith("/licenses/LICENSE") for path in package.files)
assert find_spec("credits") is None, "The test app must not be packaged"

resources = files("drip")
for path in (
    "templates/admin/drip/change_form.html",
    "templates/admin/drip/SentDrip/change_form.html",
    "templates/drip/timeline.html",
    "migrations/0001_initial.py",
    "migrations/0002_auto_20151230_0553.py",
    "south_migrations/0001_initial.py",
    "south_migrations/0002_auto__add_field_drip_from_email__add_field_drip_from_email_name__add_f.py",
    "south_migrations/0003_auto__add_field_drip_message_class.py",
):
    assert resources.joinpath(path).is_file(), f"Missing package resource: {path}"

settings.configure(
    SECRET_KEY="package-installation-check",
    INSTALLED_APPS=["django.contrib.auth", "django.contrib.contenttypes", "drip"],
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
    DEFAULT_AUTO_FIELD="django.db.models.AutoField",
    USE_TZ=True,
)
django.setup()

assert get_commands()["send_drips"] == "drip"
load_command_class("drip", "send_drips")
call_command("migrate", interactive=False, verbosity=0)

from drip.models import Drip, QuerySetRule, SentDrip

for model in (Drip, QuerySetRule, SentDrip):
    assert model.objects.count() == 0

print(f"Validated django-drip {package.version} on Django {django.get_version()}")
