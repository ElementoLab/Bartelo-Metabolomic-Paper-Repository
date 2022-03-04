import pandas as pd
import numpy as np
import pdb
import sys
from sklearn.impute import SimpleImputer
from scipy.stats import kruskal
import scikit_posthocs as sp


#curr_chrom = sys.argv[1]
#curr_ind = sys.argv[2]

ans = pd.read_csv("finish.raw", sep = " ")
decode = pd.read_csv("prediabetic_patient_eid_and_group_labels_for_scott.csv")

#########################################
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(ans.iloc[:,6:])
ans.iloc[:,6:] = imputer.transform(ans.iloc[:,6:])

pdb.set_trace()

ans = ans.iloc[np.in1d(ans["FID"], decode["eid"]), :]
decode = decode.iloc[np.in1d(decode["eid"], ans["FID"]), :]
ans = ans.sort_values("FID")
decode = decode.sort_values("eid")
ans["labels"] = decode["labels"].to_numpy()
ans = ans.iloc[:, 6:]


print("start")
all_p = list()
for i in range(ans.shape[1]-1):
  try:
    pdb.set_trace()
    all_p.append(sp.posthoc_conover(a = ans, val_col = ans.columns[i], group_col = 'labels'))
    all_p[i]["rs"] = ans.columns[i]
  except:
    print("fail")


final = pd.concat(all_p)
final.to_csv("pval.final_py.csv", index = True)
print("end")
