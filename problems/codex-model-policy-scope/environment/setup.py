import argparse,json,pathlib,shutil
p=argparse.ArgumentParser();p.add_argument('--workspace',required=True);a=p.parse_args();w=pathlib.Path(a.workspace);w.mkdir(parents=True,exist_ok=False);base=pathlib.Path(__file__).resolve().parents[1]
shutil.copyfile(base/'environment/config.json',w/'config.json');(w/'plan.md').write_text('Actor emits strict JSON with thinking disabled. Model generations currently have thinking disabled and a 2048 limit.\n');(w/'stage.json').write_text('{"stage":1}');(w/'current-task.md').write_text(json.loads((base/'task/stages.json').read_text())[0]+'\n');print(str(w))
