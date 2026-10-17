"""Create the fixed, local planning fixture without external services."""
import json
import sys
from pathlib import Path

BUILD_SOURCE = "import json\nfrom authority import LIMIT as A\nfrom planner import LIMIT as B\nx=json.load(open('profile.json'))['limit']\nassert A==B==x, 'runtime profile drift'\nprint(json.dumps({'effective_limit':x}))\n"


def create(path):
    path = Path(path)
    path.mkdir()
    (path / 'authority.py').write_text('LIMIT = 83.3925\n')
    (path / 'planner.py').write_text('LIMIT = 83.3925\n')
    (path / 'profile.json').write_text(json.dumps({'limit': 83.3925}))
    (path / 'README.md').write_text('The planner checks that authority.LIMIT, planner.LIMIT and the profile limit agree. The effective accounting limit comes from profile.json. Initialization validates only agreement of the two Python constants. Keep build.py unchanged and edit only the configuration values when changing the budget. No network is used.\n')
    (path / 'build.py').write_text(BUILD_SOURCE)


if __name__ == '__main__':
    create(Path(sys.argv[1]))
