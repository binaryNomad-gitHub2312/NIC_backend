import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NIC_Deployments.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Check if PORT is set (for Railway), otherwise use 8000 for local
    port = os.environ.get("PORT", "8000")
    execute_from_command_line([sys.argv[0], "runserver", f"0.0.0.0:{port}"])

if __name__ == '__main__':
    main()
