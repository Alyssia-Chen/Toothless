#!/bin/bash
# This script add an admin user to the Django admin app
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '1234')" | python manage.py shell