# Bartelo-Metabolomic-Paper-Repository
Contains notebooks and files needed to reproduce the findings from the publication. WARNING: SOME FILES WERE TOO LARGE TO BE INCLUDED ON GITHUB AND WILL HAVE TO BE CREATED USING THE UKBB DATA DIRECTLY OR REQUESTED FROM THE ELEMENTOLAB BY EMAILING NIB4003@MED.CORNELL.EDU!!! - THIS INCLUDES THE GENETIC ANALYSIS RESULTS

## Data Files
Contains created dataframes and text files which we import in our notebooks to create our final cohorts and conduct analyses using these patients. 

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
