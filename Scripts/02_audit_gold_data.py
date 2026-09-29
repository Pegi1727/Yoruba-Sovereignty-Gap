import argparse,json
from pathlib import Path
import pandas as pd
p=argparse.ArgumentParser(); p.add_argument("--data",default="data/yortib_200.json"); p.add_argument("--out",default="audit/gold_audit_report.xlsx"); a=p.parse_args()
with open(a.data,encoding="utf8") as f:d=json.load(f)
if isinstance(d,dict): d=d.get("data",d.get("items",[]))
df=pd.DataFrame(d); Path(a.out).parent.mkdir(parents=True,exist_ok=True)
tabs={"overview":pd.DataFrame({"metric":["N","unique IDs","unique sentence+focus","unique answers"],"value":[len(df),df.id.nunique(),df[["sentence","focus_word"]].drop_duplicates().shape[0],df.answer.nunique()]}),"focus_words":df.focus_word.value_counts().rename_axis("focus_word").reset_index(name="N"),"semantic_labels":df.answer.value_counts().rename_axis("semantic_label").reset_index(name="N")}
with pd.ExcelWriter(a.out) as w:
 [v.to_excel(w,sheet_name=k,index=False) for k,v in tabs.items()]
print("Wrote",a.out)
