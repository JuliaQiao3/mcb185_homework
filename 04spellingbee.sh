ln -s ../MCB185/data/dictionary.gz ./dictionary.gz  
gunzip -c dictionary.gz| grep -E '^[oziacnr]{4,}$' | grep "r"
gunzip -c dictionary.gz| grep -E '^[oziacnr]{4,}$' | grep "r" |wc -l
