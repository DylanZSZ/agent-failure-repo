import argparse,json,pathlib,subprocess,sys
p=argparse.ArgumentParser();p.add_argument('--workspace',required=True,type=pathlib.Path);p.add_argument('--faulty',action='store_true');a=p.parse_args();root=pathlib.Path(__file__).resolve().parents[1];case=json.loads((root/'task/stages.json').read_text())['type'];w=a.workspace
subprocess.run([sys.executable,str(root/'environment/setup.py'),'--workspace',str(w)],check=True)
def submit(*args):subprocess.run([sys.executable,str(w/'scheduler.py'),*args],check=True)
def stage(n):subprocess.run([sys.executable,str(root/'task/present.py'),'--workspace',str(w),'--stage',str(n)],check=True)
if case=='workload':
 for m in ('model-alpha','model-beta'):submit('--kind','generation','--model',m)
 stage(2)
 for m in ('model-alpha','model-beta'):submit('--kind','training','--model',m)
 stage(3)
 for m in ('model-alpha','model-beta'):submit('--kind','generation' if a.faulty else 'training','--model',m,'--cluster','arm')
else:
 for arm in ('diverse','similar'):submit('--campaign','response-rank','--arm',arm)
 stage(2)
 for arm in ('diverse','similar'):
  for size in ('50k','100k'):submit('--campaign','global-set','--arm',arm,'--size',size)
 stage(3);jobs=json.loads((w/'jobs.json').read_text());campaigns=['global-set'] if a.faulty else ['response-rank','global-set'];selected=[j for j in jobs if j['campaign'] in campaigns]
 (w/'report.json').write_text(json.dumps({'campaigns':campaigns,'jobs':[j['id'] for j in selected]},indent=2)+'\n')
 (w/'report.md').write_text('Active campaigns: '+', '.join(campaigns)+'\n')
subprocess.run([sys.executable,str(root/'checks/judge.py'),'--workspace',str(w)],check=True)
