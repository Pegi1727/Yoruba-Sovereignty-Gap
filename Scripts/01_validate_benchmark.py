import argparse,json
from pathlib import Path
import pandas as pd
p=argparse.ArgumentParser(); p.add_argument("--json",default="data/yortib_200.json"); p.add_argument("--xlsx",default="data/yortib_200.xlsx"); p.add_argument("--out",default="audit/benchmark_validation.csv"); a=p.parse_args()
with open(a.json,encoding="utf8") as f:d=json.load(f)
if isinstance(d,dict): d=d.get("data",d.get("items",[]))
j=pd.DataFrame(d); x=pd.read_excel(a.xlsx)
req=["id","sentence","focus_word","options","answer"]
assert all(c in j for c in req) and all(c in x for c in req)
r={"json_n":len(j),"xlsx_n":len(x),"json_duplicate_ids":int(j.id.duplicated().sum()),"xlsx_duplicate_ids":int(x.id.duplicated().sum()),"json_ids_1_200":set(j.id)==set(range(1,201)),"xlsx_ids_1_200":set(x.id)==set(range(1,201)),"id_sets_match":set(j.id)==set(x.id)}
for c in ["sentence","focus_word","answer"]:
 r[c+"_mismatches"]=int((j.set_index("id")[c].astype(str).sort_index()!=x.set_index("id")[c].astype(str).sort_index()).sum())
Path(a.out).parent.mkdir(parents=True,exist_ok=True); pd.DataFrame([r]).to_csv(a.out,index=False); print(pd.Series(r))
