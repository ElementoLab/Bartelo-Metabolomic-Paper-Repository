# Bartelo-Metabolomic-Paper-Repository
Contains notebooks with written step-by-step commentary. DATA IS NOT ALLOWED TO BE SHARED SO FILES NEEDED TO REPRODUCE FINDINGS ARE NOT INCLUDED! Look at the UK Biobank Data Mining for code to create the data files needed for the analysis.

## Data Files
All dataframes and text files which we import in our notebooks to create our final cohorts and conduct analyses using these patients can be requested as we are not allowed
to distribute UKBB data. 

## Jupyter Notebooks:

### Analysis of GWAS.ipynb
Contains the analysis after the GWAS was performed.

### Data Mining To Find Final Pre-diabetic Cohort.ipynb
Contains all the data mining, manipulation, and patient selection for the final cohort to be used in the study.

### Demographics Analysis Of Progressors Vs Non-progressors and All Seven Pre-diabetic Groups.ipynb
Contains the age, sex, ethnicity, number, and statistical testing for these variables for progressors vs. non-progressors and pre-diabetic unsupervised clusters.

### Manually Created Figures - Bar charts, Networks, Dotplots, and Circular Plots.ipynb
Contains all figures created manually.

### Pre-diabetic Clustering and Statistical Analyses of Metabolomics, Comorbidities, Progression Outcomes, and Traditional Risk Factors.ipynb
Contains the actual clustering and numerous statistical analyses for the metabolomics, comorbidities, progression outcomes, and traditional risk factors. 

### Random Assignment of Pre-diabetics To Seven Groups.ipynb
Contains the method for randomly assigning patients to 7 groups and all statistical analyses conducted for these groups.

### Supervised Machine Learning Predicting Pre-diabetic Group Identity.ipynb
Contains all analyses for the supervised model created to predict a pre-diabetic assignment into their assigned group from the unsupervised clustering using the metabolomics data.

## Additional Code For UKBB Data Extraction:

### UK Biobank Data Mining
Contains code used to mine for the data we need to create our final patient population and extract the features we used for the traditional risk factor variables.
