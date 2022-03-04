rm merge_list
for i in {1..22};do
  bgenix -g ~/athena/ukbiobank/imputed/ukbb.${i}.bgen -incl-rsids sig_rsid.txt > temp.bgen
  plink2 --bgen temp.bgen ref-first --sample ~/athena/ukbiobank/imputed/ukbb.${i}.sample --make-bed --out use.${i}
  echo use.${i} >> merge_list
done

ls use*bed | cut -f1,2 -d'.' > merge_list
plink --merge-list merge_list --recode A --out finish
rm use*
