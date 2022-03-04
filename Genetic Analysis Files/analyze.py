import pandas as pd
import numpy as np
import pdb
import sys
from sklearn.impute import SimpleImputer
from scipy.stats import kruskal

curr_chrom = sys.argv[1]
curr_ind = sys.argv[2]

ans = pd.read_csv("ready." + str(curr_chrom) +  ".raw", sep = " ")
decode = pd.read_csv("prediabetic_patient_eid_and_group_labels_for_scott.csv")

#########################################
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(ans.iloc[:,7:])
ans.iloc[:,7:] = imputer.transform(ans.iloc[:,7:])

all_g = list()
for curr_lab in np.unique(decode['labels']):

  g = decode['eid'][decode['labels'] == curr_lab]
  x = ans.loc[np.in1d(ans['FID'], g),:]
  all_g.append(x.iloc[:,7:].to_numpy())


print("start")
all_p = list()
for i in range(all_g[0].shape[1]):
  try:
    all_p.append(kruskal(all_g[0][:,i], all_g[1][:,i], all_g[2][:,i], all_g[3][:,i], all_g[4][:,i], all_g[5][:,i], all_g[6][:,i])[1])
  except:
    all_p.append(1)

final = pd.DataFrame({"rsid":ans.columns.to_numpy()[7:], "p":np.array(all_p)})
final.to_csv("pval." + str(curr_chrom) + "." + str(curr_ind) + ".csv", index = False)
print("end")
