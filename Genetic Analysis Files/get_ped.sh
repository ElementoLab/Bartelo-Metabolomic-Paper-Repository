

#plink2 --bgen ~/athena/ukbiobank/imputed/ukbb.${1}.bgen ref-first --sample ~/athena/ukbiobank/imputed/ukbb.${1}.sample --exclude /home/kulmsc/athena/ukbiobank/custom_qc/impute_bad/impute.${1}.snps --keep-fam need_eid --make-bed 
#plink --bfile plink2 --recode A --out ready

#python analyze.py $1

#rm ready.bed ready.bim ready.fam plink2.bed plink2.bed plink2.fam


####################################################


plink2 --bgen ~/athena/ukbiobank/imputed/ukbb.${1}.bgen ref-first --sample ~/athena/ukbiobank/imputed/ukbb.${1}.sample --exclude /home/kulmsc/athena/ukbiobank/custom_qc/impute_bad/impute.${1}.snps --keep-fam need_eid --make-bed --out input.$1
split -n 2 input.${1}.bim
mv xaa xaa.$1
mv xab xab.$1

cat xaa.$1 | cut -f2 > use_ids.$1
plink --bfile input.$1 --extract use_ids.$1 --recode A --out ready.$1

python analyze.py $1 1

cat xab.$1 | cut -f2 > use_ids.$1
plink --bfile input.$1 --extract use_ids.$1 --recode A --out ready.$1

python analyze.py $1 2

rm input.${1}.bed input.${1}.fam input.${1}.bim
rm ready.${1}.bed ready.${1}.fam ready.${1}.bim
rm xaa.$1 xab.$1

#######################################################

#bgenix -g /home/kulmsc/athena/ukbiobank/imputed/ukbb.${1}.bgen -incl-rsids use_rsid > temp.bgen
#plink2 --bgen temp.bgen ref-first --sample ~/athena/ukbiobank/imputed/ukbb.${1}.sample --keep-fam need_eid --make-bed 
#plink --bfile plink2 --recode A --out ready
