import os
import shutil
import tempfile
import uuid
import flask
import asciiii


def create_ascii(photo, lines, color):
    return asciiii.app.config["RESULTS_FOLDER"] + '2.png'


def save_file(file):
    """Save image files into /var/uploads/."""
    # Save POST request's file object to a temp file
    dummy, temp_filename = tempfile.mkstemp()
    file.save(temp_filename)

    # Compute filename
    dummy, suffix = os.path.splitext(file.filename)
    filename_uuid = uuid.uuid4().hex + suffix
    filename = os.path.join(
        asciiii.app.config["UPLOAD_FOLDER"],
        filename_uuid
    )

    # Move temp file to permanent location
    shutil.move(temp_filename, filename)
    asciiii.app.logger.debug("Saved %s", filename)
    return filename
