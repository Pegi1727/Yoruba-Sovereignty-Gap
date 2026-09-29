library(readr)
x<-read_csv("results/figure_data/item_level_with_gold.csv",show_col_types=FALSE)
tab<-table(x$baseline_correct,x$sovereign_correct); b<-tab["TRUE","FALSE"]; c<-tab["FALSE","TRUE"]; p<-binom.test(min(b,c),b+c,.5)$p.value
out<-data.frame(both_correct=tab["TRUE","TRUE"],baseline_only=b,sovereign_only=c,both_wrong=tab["FALSE","FALSE"],exact_mcnemar_p=p)
write.csv(out,"results/r/mcnemar.csv",row.names=FALSE); print(out)
