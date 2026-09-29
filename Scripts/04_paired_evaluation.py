import argparse,json
from pathlib import Path
import pandas as pd
from scipy.stats import binomtest
MAP={"husband":"Everyday Vocabulary","person":"Everyday Vocabulary","creature":"Everyday Vocabulary","farm":"Agriculture","vehicle":"Transportation","medicine":"Medicine","poison":"Medicine","heaven":"Spiritual Concepts","spiritual power":"Spiritual Concepts","spirit world":"Spiritual Concepts","afterlife":"Spiritual Concepts","sky":"Spiritual Concepts","authority":"Moral / Philosophical Concepts","character":"Moral / Philosophical Concepts","behavior":"Moral / Philosophical Concepts","command":"Moral / Philosophical Concepts","inheritance":"Moral / Philosophical Concepts","permission":"Moral / Philosophical Concepts","moral nature":"Moral / Philosophical Concepts","war":"Moral / Philosophical Concepts","creation":"Ontological Concepts","existence":"Ontological Concepts","being":"Ontological Concepts","spear":"Ontological Concepts"}
def pred(f):
 q=pd.read_csv(f)
 for c in ["prediction","predicted_label","answer"]:
  if c in q:return q[c].astype(str).str.strip()
 return q.iloc[:,-1].astype(str).str.strip()
p=argparse.ArgumentParser(); p.add_argument("--gold",default="data/yortib_200.json"); p.add_argument("--baseline",required=True); p.add_argument("--sovereign",required=True); p.add_argument("--out",default="results/paired_results.xlsx"); a=p.parse_args()
with open(a.gold,encoding="utf8") as f:d=json.load(f)
if isinstance(d,dict): d=d.get("data",d.get("items",[]))
g=pd.DataFrame(d); g["baseline_pred"]=pred(a.baseline).values; g["sovereign_pred"]=pred(a.sovereign).values
g["baseline_correct"]=g.baseline_pred.eq(g.answer.astype(str).str.strip()); g["sovereign_correct"]=g.sovereign_pred.eq(g.answer.astype(str).str.strip())
bc,sc=g.baseline_correct,g.sovereign_correct; bo=int((bc&~sc).sum()); so=int((~bc&sc).sum()); pval=binomtest(min(bo,so),bo+so,.5).pvalue
g["category"]=g.answer.map(MAP)
assert not g.category.isna().any()
Path(a.out).parent.mkdir(parents=True,exist_ok=True)
overall=pd.DataFrame({"metric":["N","baseline_accuracy","sovereign_accuracy","difference_pp","baseline_only_correct","sovereign_only_correct","exact_mcnemar_p"],"value":[len(g),bc.mean(),sc.mean(),100*(sc.mean()-bc.mean()),bo,so,pval]})
with pd.ExcelWriter(a.out) as w:
 overall.to_excel(w,"overall",index=False); g.groupby("focus_word")[["baseline_correct","sovereign_correct"]].mean().reset_index().to_excel(w,"focus_word",index=False); g.groupby("category")[["baseline_correct","sovereign_correct"]].mean().reset_index().to_excel(w,"categories",index=False); pd.crosstab(bc,sc).to_excel(w,"paired_contingency"); g.loc[~sc,["id","focus_word","answer","baseline_pred","sovereign_pred"]].to_excel(w,"remaining_errors",index=False); g.to_excel(w,"item_level",index=False)
print(overall.to_string(index=False))
