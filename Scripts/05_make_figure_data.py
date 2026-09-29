import argparse,json
from pathlib import Path
import pandas as pd
p=argparse.ArgumentParser(); p.add_argument("--gold",default="data/yortib_200.json"); p.add_argument("--paired",required=True); p.add_argument("--outdir",default="results/figure_data"); a=p.parse_args()
with open(a.gold,encoding="utf8") as f:d=json.load(f)
if isinstance(d,dict):d=d.get("data",d.get("items",[]))
g=pd.DataFrame(d); q=pd.read_csv(a.paired)
b=next(c for c in q if c.lower() in ["baseline","baseline_pred","baseline_prediction"]); s=next(c for c in q if c.lower() in ["sovereign","sovereign_pred","sovereign_prediction"])
g["baseline_correct"]=q[b].astype(str).str.strip().eq(g.answer.astype(str).str.strip()); g["sovereign_correct"]=q[s].astype(str).str.strip().eq(g.answer.astype(str).str.strip())
o=Path(a.outdir); o.mkdir(parents=True,exist_ok=True)
pd.DataFrame({"condition":["Baseline","Sovereignty-preserving"],"accuracy":[g.baseline_correct.mean(),g.sovereign_correct.mean()]}).to_csv(o/"overall_accuracy.csv",index=False)
g.groupby("focus_word")[["baseline_correct","sovereign_correct"]].mean().reset_index().to_csv(o/"focus_accuracy.csv",index=False)
g[["id","focus_word","answer","baseline_correct","sovereign_correct"]].to_csv(o/"item_level_with_gold.csv",index=False)
print("Figure data written to",o)
