library(readr); library(dplyr)
x<-read_csv("results/figure_data/item_level_with_gold.csv",show_col_types=FALSE)
out<-tibble(condition=c("Baseline","Sovereignty-preserving"),N=nrow(x),correct=c(sum(x$baseline_correct),sum(x$sovereign_correct)),accuracy=c(mean(x$baseline_correct),mean(x$sovereign_correct)))
dir.create("results/r",recursive=TRUE,showWarnings=FALSE); write_csv(out,"results/r/descriptives.csv"); print(out)
