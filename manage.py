#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


from django.shortcuts import render


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


def post_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'home_app/post-details.html', {'todo': todo})
