from flask import Blueprint, render_template
import os
from .utils import cephboto
from pathlib import Path
bp = Blueprint('player', __name__, url_prefix='/player')

CACHE_DIR= os.path.join(__name__.split('.')[0], 'static/cache' )

@bp.route('/<filename>')
def index(filename):
    cachename = os.path.join(CACHE_DIR, filename)
    if not Path(filename).is_file():
        cephboto.get_file(filename, cachename)
    video={}
    video['filename']=filename
    video['loc']=os.path.join('static/cache',filename)
    return render_template('player/index.html', video=video)