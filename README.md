Django Drip
====================

[![CI](https://github.com/SweetProcess/django-drip/actions/workflows/ci.yml/badge.svg)](https://github.com/SweetProcess/django-drip/actions/workflows/ci.yml)

Drip campaigns are pre-written sets of emails sent to customers or prospects over time. Django Drips lets you use the admin to manage drip campaign emails using querysets on Django's User model.

Originally created by [Zapier](https://zapier.com/), this fork is maintained for use by SweetProcess.

[Read the docs](docs/index.rst).

### Supported versions

Python 3.12, 3.13, and 3.14; Django 5.1, 5.2, 6.0, and 6.1.
CI tests these combinations except Python 3.14 with Django 5.1, which Django does not support.
Each Django series is tested at its latest patch release, including Python 3.13 / Django 5.1.

Django 5.1 remains a compatibility target for existing installations but is past
upstream support. Django 5.2 LTS is the recommended next upgrade for those installations.

### Installing

Install the SweetProcess fork from Git using SSH access to the repository. Add a
pinned commit to your application's requirements file, replacing `<commit-sha>`
with the full commit SHA you have validated:

```text
git+ssh://git@github.com/SweetProcess/django-drip.git@<commit-sha>#egg=django-drip
```

```bash
python -m pip install -r requirements.txt
```

Next, you'll want to add `drip` to your `INSTALLED_APPS` in settings.py.

```python
INSTALLED_APPS = [
    # Your existing apps, including Django's admin and its dependencies.
    "drip",
]
```

Set `DRIP_FROM_EMAIL` in settings.py; when it is absent, the library falls back to
`DEFAULT_FROM_EMAIL`.

Apply the database migrations, then schedule `send_drips` at the desired interval:

```bash
python manage.py migrate drip
python manage.py send_drips
```

### Development

Using Python 3.12 or newer:

```bash
git clone git@github.com:SweetProcess/django-drip.git
cd django-drip
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -Wa manage.py test --noinput
```

To match SweetProcess's Python 3.13 / Django 5.1 deployment, create the virtual
environment with Python 3.13 and install with
`python -m pip install -r requirements.txt "Django~=5.1.0"`.

Build the wheel and source distribution with:

```bash
python -m pip install build
python -m build
```

CI also installs both artifacts and the checked-out Git commit into separate
environments, then checks their metadata, package resources, and migrations from
outside the checkout. Before updating SweetProcess's pinned commit, validate it
in the application, including any changes since the previously pinned commit.

![what the admin looks like](docs/images/drip-example.png)
![what the admin looks like for the timeline](docs/images/view-timeline.png)
