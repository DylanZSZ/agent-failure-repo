import argparse,json,pathlib,subprocess,sys
p=argparse.ArgumentParser();p.add_argument('--workspace',required=True);p.add_argument('--faulty',action='store_true');a=p.parse_args();base=pathlib.Path(__file__).resolve().parents[1];w=pathlib.Path(a.workspace)
subprocess.run([sys.executable,str(base/'environment/setup.py'),'--workspace',str(w)],check=True,capture_output=True)
(w/'policy-notes.md').write_text('Actor: strict JSON, thinking disabled. Teacher and students currently disabled.\n');(w/'task-pairs.json').write_text(json.dumps([{'train':'train_'+str(i),'transfer':'transfer_'+str(i)} for i in range(5)]));subprocess.run([sys.executable,str(base/'task/present.py'),'--workspace',str(w)],check=True)
x=json.loads((w/'config.json').read_text())
for k in ('teacher_sft','student_opd','student_grpo'):x[k].update(thinking=True,max_length=8192)
if a.faulty:x['actor']['thinking']=True
(w/'config.json').write_text(json.dumps(x,indent=2));(w/'plan.md').write_text('Teacher and student generations use thinking with limit 8192. Actor '+('also uses thinking.' if a.faulty else 'remains strict JSON with thinking disabled.'))
subprocess.run([sys.executable,str(base/'checks/judge.py'),'--workspace',str(w)],check=True)
