"""Replay the review's synthetic checker inputs, after independently inspecting judges.
Usage: python3 reproduce-checker-review-a.py /path/to/repo checker-review-a.json output.json
No model, network, scheduler, host environment variables, or historical commands used.
"""
import argparse,hashlib,json,pathlib,re,subprocess,sys,tempfile
p=argparse.ArgumentParser();p.add_argument('repository',type=pathlib.Path);p.add_argument('receipt',type=pathlib.Path);p.add_argument('output',type=pathlib.Path);a=p.parse_args()
root=a.repository.resolve();old=json.loads(a.receipt.read_text());rows=[]
with tempfile.TemporaryDirectory(prefix='submission-check-a-') as td:
 t=pathlib.Path(td)
 for case in old['trials']:
  judge=root/'problems'/case['id']/'checks/judge.py'
  digest=hashlib.sha256(judge.read_bytes()).hexdigest()
  if digest!=case['judge_sha256']:raise SystemExit('Judge changed: '+case['id']+'; inspect it before a new review.')
  decision=t/'decision.json';decision.write_text(json.dumps(case['input']))
  run=subprocess.run([sys.executable,'-I',str(judge),str(decision)],cwd=t,env={'PATH':'/usr/bin:/bin','LANG':'C'},capture_output=True,text=True,timeout=5)
  try:result=json.loads(run.stdout)
  except ValueError:result=None
  err=run.stderr.replace(str(root),'<repo>').replace(td,'<temporary>')
  rows.append(dict(case,exit_code=run.returncode,result=result,stderr=err))
a.output.write_text(json.dumps({'kind':'reviewer_scripted_check','model_calls':0,'trials':rows},indent=2)+'\n')
print('Recorded',len(rows),'local checker trials to',a.output)
