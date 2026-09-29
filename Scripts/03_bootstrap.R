library(readr)
set.seed(20260929); x<-read_csv("results/figure_data/item_level_with_gold.csv",show_col_types=FALSE)
d<-as.numeric(x$sovereign_correct)-as.numeric(x$baseline_correct); B<-10000
z<-replicate(B,mean(sample(d,replace=TRUE))); out<-data.frame(estimate=mean(d),lower_95=quantile(z,.025),upper_95=quantile(z,.975),B=B,seed=20260929)
dir.create("results/r",recursive=TRUE,showWarnings=FALSE); write.csv(out,"results/r/bootstrap.csv",row.names=FALSE); print(out)
