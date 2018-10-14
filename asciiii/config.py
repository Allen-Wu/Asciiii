import os

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# File Upload to var/uploads/
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'asciiii', 'var', 'uploads'
)

ALLOWED_EXTENSIONS = set(['.png', '.jpg', '.jpeg', '.gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
