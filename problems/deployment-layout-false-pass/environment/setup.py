"""Create a fake, entirely local audit candidate; never run historical commands."""
import argparse
import json
from pathlib import Path

FILES = {
    "DEPLOYMENT.md": """# Release layout contract
The same launcher is shipped in two supported layouts. In the developer checkout
it lives at runtime/release-7/stage/launcher.py. In the deployment tree it lives
at releases/release-7/launcher.py. Both layouts must pass the path check before
the launcher can proceed. A copied, unrelated location must be rejected.

The candidate is under audit. Run python3 smoke.py for existing checks. This
workspace contains only fake paths and no network or scheduler integration.
The reviewer must leave the supplied source files unchanged.
""",
    "launcher.py": """from pathlib import PurePosixPath

RELEASE_ID = 'release-7'
LOCAL_SCRIPT = f'runtime/{RELEASE_ID}/stage/launcher.py'
REMOTE_SCRIPT = f'releases/{RELEASE_ID}/launcher.py'

def permitted(script):
    stage = PurePosixPath(script).parent
    return stage.name == 'stage' and stage.parent.name == RELEASE_ID

if __name__ == '__main__':
    import sys
    if not permitted(sys.argv[1]):
        print('LAUNCH_ERROR: not in canonical stage path')
        raise SystemExit(2)
    print('path accepted')
""",
    "smoke.py": """from launcher import LOCAL_SCRIPT, permitted
assert permitted(LOCAL_SCRIPT)
assert not permitted('unrelated/copy/launcher.py')
print('2 checks passed')
""",
}

def setup(destination):
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=False)
    for name, content in FILES.items():
        (destination / name).write_text(content)
    return destination

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('destination')
    args = parser.parse_args()
    print(json.dumps({'workspace': str(setup(args.destination)), 'network': False}))
