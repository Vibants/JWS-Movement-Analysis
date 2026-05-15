# Juvenile White Shark (JWS; Carcharodon carcharias) Movement Analysis

1) Project Summary
This project analyzes JWS movement behavior collected from a Vemco Positioing System (VPS)
acoustic array by the CSULB Shark Lab in 2021, based in Santa Barbara, CA, established as
an historical nursery habitat. The dataset includes information related to individually tagged
JWS, detection times within the array, estimated positions using horizontal position error,
temperature values, and many more to describe the movement patterns within the array. The 
purpose of this final project is to describe patterns in JWS residency, horizontal space use, 
and depth usage in relation to sea surface temperature waters in a nearshore habitat. As 
practiced in the rough draft, the major goal of this final project is to exercise 
reproducibility, create a clear coding structure, access datsets, and utilize relevant 
packages for cleaning/analysis/figure making. All files for the final project uses the terminal
and Jupyter notebook for analysis workflow and the creation of .py files to make useful 
functions for calculating residency within the VPS array.

2)  Location of data and acknowledgement of source
Data used for this project is stored in the repository as an subset R data file, not
encapsulating the full dataset. Dataset was supported by past Shark Lab master's student Emily
Spurgeon.

3) Depencies
For my analysis, I used Python packages, similar to those that we used during the course of 
the semester for data cleaning, analysis,and plotting. At the start of the coding file, 
importing of all the useful packages will be made before coding practices. The main packages 
used in this project
are:
	-numpy
	-pandas
	-matplotlib
	-scipy
	-xarray
	-cartopy
	-pyreader
Most of these packages are ones that we have used, except for the "pyreadr" package. Emily
Spurgeon was used as source of help during the coding of this subset of VPS data because of
her familiarity of coding workflow with this type of data and I'm still trying to grasp.
This package is needed because the data file was stored as an R.rds file. A "vps_functions.py"
file will also be imported at the start of the coding workflow to calculate Time Difference of
Arrival (TDOA) or residency within the array.

4) Location of data in repository, or how to access data

The data file will be stored directly inside the "JWS-Movement-Analysis" GitHub project
repository. The files for this final project will be imported as:

	-README.md
	-FINAL_projectdraft_MS263.ipynb
	-vps_data_subset.rds
	-vps_functions.py   
  
 
