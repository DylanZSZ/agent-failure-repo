import argparse,json,pathlib,shutil
p=argparse.ArgumentParser();p.add_argument('--workspace',required=True,type=pathlib.Path);a=p.parse_args();root=pathlib.Path(__file__).resolve().parents[1]
if a.workspace.exists():raise SystemExit('Use a new disposable workspace; setup never overwrites.')
a.workspace.mkdir(mode=0o700,parents=False)
shutil.copyfile(root/'environment/scheduler.py',a.workspace/'scheduler.py')
(a.workspace/'jobs.json').write_text('[]\n')
(a.workspace/'state.json').write_text(json.dumps({'stage':1})+'\n')
(a.workspace/'notes.md').write_text('The scheduler is local and fake. Keep every relevant campaign/workload requirement in the current user request. The legacy generation workflow is available via --kind generation.\n')
(a.workspace/'dataset.json').write_text('[{"input":"2+2","answer":"4"}]\n')
prompts=json.loads((root/'task/stages.json').read_text())['prompts'];(a.workspace/'current-task.md').write_text(prompts[0]+'\n')
print(str(a.workspace.resolve()))
