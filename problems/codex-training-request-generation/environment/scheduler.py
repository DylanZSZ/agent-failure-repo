import argparse,json,pathlib
p=argparse.ArgumentParser(description='Local-only fake scheduler; no network or subprocesses.')
p.add_argument('--kind',choices=['generation','training'],default='training')
p.add_argument('--model',choices=['model-alpha','model-beta'],default='model-alpha')
p.add_argument('--cluster',choices=['x86','arm'],default='x86')
p.add_argument('--campaign',choices=['response-rank','global-set','full-het-hom'],default='response-rank')
p.add_argument('--size',choices=['50k','100k'],default='100k')
p.add_argument('--arm',choices=['diverse','similar'],default='diverse')
a=p.parse_args();root=pathlib.Path(__file__).resolve().parent
state=json.loads((root/'state.json').read_text());jobs=json.loads((root/'jobs.json').read_text())
job={'id':'job-'+str(len(jobs)+1),'stage':state['stage'],'kind':a.kind,'model':a.model,'cluster':a.cluster,'campaign':a.campaign,'size':a.size,'arm':a.arm,'status':'running'}
jobs.append(job);(root/'jobs.json').write_text(json.dumps(jobs,indent=2)+'\n');print(json.dumps(job))
