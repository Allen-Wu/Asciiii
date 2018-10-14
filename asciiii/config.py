import os

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\xf1\xa7I\x08Q\x85\x08Mk\xd7\x9b\x8f\xb0\x1c\xe8V\xd8\xdd|?$\xf0A\x97'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'asciiii', 'var', 'uploads'
)
ALLOWED_EXTENSIONS = set(['.png', '.jpg', '.jpeg', '.gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
