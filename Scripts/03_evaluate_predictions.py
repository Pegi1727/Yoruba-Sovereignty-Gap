import argparse,json
from pathlib import Path
import pandas as pd
p=argparse.ArgumentParser(); p.add_argument("--gold",default="data/yortib_200.json"); p.add_argument("--pred",required=True); p.add_argument("--out",default="results/single_condition.xlsx"); a=p.parse_args()
with open(a.gold,encoding="utf8") as f:d=json.load(f)
if isinstance(d,dict): d=d.get("data",d.get("items",[]))
g=pd.DataFrame(d); q=pd.read_csv(a.pred); col="prediction" if "prediction" in q else q.columns[-1]
assert len(g)==len(q); g["prediction"]=q[col].astype(str).str.strip(); g["correct"]=g.prediction.eq(g.answer.astype(str).str.strip())
Path(a.out).parent.mkdir(parents=True,exist_ok=True)
with pd.ExcelWriter(a.out) as w:
 pd.DataFrame({"N":[len(g)],"accuracy":[g.correct.mean()]}).to_excel(w,"overall",index=False)
 g.groupby("focus_word").correct.mean().reset_index(name="accuracy").to_excel(w,"focus_word",index=False)
 pd.crosstab(g.answer,g.prediction).to_excel(w,"confusion_matrix")
print("accuracy =",g.correct.mean())
