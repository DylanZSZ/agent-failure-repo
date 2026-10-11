import argparse,json,pathlib
p=argparse.ArgumentParser();p.add_argument('--workspace',required=True);a=p.parse_args();w=pathlib.Path(a.workspace);assert json.loads((w/'stage.json').read_text())['stage']==1
snapshot={'config':json.loads((w/'config.json').read_text()),'pairs':json.loads((w/'task-pairs.json').read_text()),'notes':(w/'policy-notes.md').read_text()};(w/'stage1-snapshot.json').write_text(json.dumps(snapshot,indent=2));(w/'stage.json').write_text('{"stage":2}');(w/'current-task.md').write_text(json.loads((pathlib.Path(__file__).parent/'stages.json').read_text())[1]+'\n')
