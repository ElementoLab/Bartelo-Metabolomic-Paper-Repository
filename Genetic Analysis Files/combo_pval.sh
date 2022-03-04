

ls pval*csv | fgrep -v final | while read line;do
  chrom=`echo $line | cut -f2 -d'.'`
  len=`cat $line | wc -l`
  yes $chrom | head -$len > addon
  paste -d',' addon $line | tail -n+2 >> pval.total.csv
done
