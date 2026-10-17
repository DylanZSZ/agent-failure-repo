import argparse,json,pathlib
p=argparse.ArgumentParser();p.add_argument('--workspace',required=True,type=pathlib.Path);p.add_argument('--stage',required=True,type=int,choices=[2,3]);a=p.parse_args();root=pathlib.Path(__file__).resolve().parents[1];state=json.loads((a.workspace/'state.json').read_text())
if a.stage!=state['stage']+1:raise SystemExit('Advance exactly one stage; do not skip prerequisites.')
state['stage']=a.stage;(a.workspace/'state.json').write_text(json.dumps(state)+'\n')
text=json.loads((root/'task/stages.json').read_text())['prompts'][a.stage-1];(a.workspace/'current-task.md').write_text(text+'\n');print(text)
