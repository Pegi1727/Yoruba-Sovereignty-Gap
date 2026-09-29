library(readr); library(dplyr)
x<-read_csv("results/figure_data/item_level_with_gold.csv",show_col_types=FALSE)
wilson<-function(k,n){z<-qnorm(.975);p<-k/n;den<-1+z^2/n;c((p+z^2/(2*n)-z*sqrt(p*(1-p)/n+z^2/(4*n^2)))/den,(p+z^2/(2*n)+z*sqrt(p*(1-p)/n+z^2/(4*n^2)))/den)}
rows<-list()
for(w in unique(x$focus_word)){q<-filter(x,focus_word==w);for(v in c("baseline_correct","sovereign_correct")){ci<-wilson(sum(q[[v]]),nrow(q));rows[[length(rows)+1]]<-data.frame(focus_word=w,condition=v,N=nrow(q),accuracy=mean(q[[v]]),CI_lower=ci[1],CI_upper=ci[2])}}
out<-bind_rows(rows); write_csv(out,"results/r/focus_word_ci.csv"); print(out)
