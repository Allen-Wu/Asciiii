import sys
import os
import shutil
import tempfile
import uuid
import engine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from engine.main import run
from engine import util


def create_ascii(photo, lines, eta, color, light):
    config = {'file': util.get_abs_path('server/var/uploads/' + photo), 'line': int(lines), 'eta': float(eta), 'light': light}
    res = run(**config)
    return res


def save_file(file):
    # Save POST request's file object to a temp file
    dummy, temp_filename = tempfile.mkstemp()
    file.save(temp_filename)

    # Compute filename
    dummy, suffix = os.path.splitext(file.filename)
    filename_uuid = uuid.uuid4().hex + suffix
    if suffix not in engine.app.config["ALLOWED_EXTENSIONS"]:
        return ""
    filename = os.path.join(
        engine.app.config["UPLOAD_FOLDER"],
        filename_uuid
    )

    # Move temp file to permanent location
    shutil.move(temp_filename, filename)
    engine.app.logger.debug("Saved %s", filename)
    return filename_uuid
