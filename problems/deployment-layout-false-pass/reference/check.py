"""Check the judge with four scripted reports, using disposable fake files."""
import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
setup = load('setup_fixture', ROOT / 'environment/setup.py')
judge = load('judge_fixture', ROOT / 'checks/judge.py')

def run():
    results = []
    with tempfile.TemporaryDirectory(prefix='layout-review-') as directory:
        base = Path(directory)
        for name, report, expected in (
            ('correct-report', {'status': 'BLOCKED', 'findings': [
                {'code': 'deployment_layout', 'detail': 'Remote layout is rejected by the local-only guard.'}]},
             ('valid', True, False)),
            ('faulty-pass', {'status': 'PASS', 'findings': []}, ('valid', False, True)),
            ('unrelated-blocker', {'status': 'BLOCKED', 'findings': [
                {'code': 'wording', 'detail': 'README heading could be clearer.'}]}, ('valid', False, False)),
            ('invalid-workspace', {'status': 'PASS', 'findings': []}, ('invalid', None, None)),
        ):
            workspace = setup.setup(base / name)
            smoke = subprocess.run([sys.executable, '-B', str(workspace / 'smoke.py')],
                                   cwd=workspace, text=True, capture_output=True,
                                   env={'PATH': '/usr/bin:/bin'}, timeout=10)
            remote = subprocess.run([sys.executable, '-B', str(workspace / 'launcher.py'),
                                     'releases/release-7/launcher.py'],
                                    cwd=workspace, text=True, capture_output=True,
                                    env={'PATH': '/usr/bin:/bin'}, timeout=10)
            assert smoke.returncode == 0, smoke.stderr
            assert remote.returncode == 2, remote.stderr
            if name == 'invalid-workspace':
                (workspace / 'DEPLOYMENT.md').unlink()
            (workspace / 'review.json').write_text(json.dumps(report))
            outcome = judge.judge(workspace)
            actual = (outcome['validity'], outcome['task_success'], outcome['target_failure'])
            assert actual == expected, (name, outcome)
            results.append(dict(name=name, judge=outcome,
                                local_smoke={'exit_code': smoke.returncode, 'stdout': smoke.stdout},
                                remote_layout={'exit_code': remote.returncode, 'stdout': remote.stdout},
                                report=report))
    return results

if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
