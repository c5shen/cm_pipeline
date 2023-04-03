python3 ../simple_cm.py \
        --quiet \
        -i /shared/rsquared/cen_cleaned.tsv  \
        -c leiden \
        -d working_dir_test1 \
        -g 0.01 \
        -t 1log10 \
        -e ~/cen_leiden.01_nontree_n10_clusters.tsv \
        -o cen_leiden.01_nontree_n10_clusters_cm_simple2.txt