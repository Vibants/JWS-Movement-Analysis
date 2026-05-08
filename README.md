## MS 263  - Data Analysis Techniques In Marine Science
### Homework 6

Due: Wednesday, April 30

1: [Scientific computing reading](1-reading.ipynb)

2: [Project draft](2-project.ipynb)
    #Location and acknowledgement of dataset/source:
        The dataset 'vps_data_subset.rds' contains acoustic telemetry detections from the 2021 Santa Barbara VPS array dataset. Past CSULB Shark Lab Masters student Emily Spurgeon and advisor Dr. Christopher Lowe has given me access to utilize the partial dataset to use for comparison on my thesis project. The .rds file will be in either this Homework #6 file, or submitted separately depending on the file size. This file contains (1) timestamps of detections, (2) individual shark ID, (3) coordinates of detection, (4) sex, (5) depth data from pressure sensors, (6) temperature data from built-in temperature sensors or Env temperature loggers on receiver mooring sites, (7) horizontal position error (HPE), and more. However, Temperature data use will be held off for the final project submission, and I have not also learned how integrate temperature data to the associated juvenile white shark (JWS). Dataset was initially processed in R, so I used the 'pyreader' package to read the file into Python.
    #Steps for analysis code/methods:
        -Data cleaning:
            the 'vps_data_subset' file was uploaded into Python using the pyreadr package. I then converted the file into pandas format, including timestamps and removing missing spatial data, missing HPE, and negative depth values.
        -Residency Index (RI): The residency formula within acoustic telemetry arrays being utilized for this project comes from Kraft et al., 2023, which is shown in the reference section. Residency is calculated as: RI = days detected / last detection - first detection +1. I then created a loop for each individual shark that entered into the array system. Later, data is visualized using a bar plot.
        -Dependencies/Running this project code:
            conda install pandas numpy matplotlib pyreadr
            jupyter notebook
            2-project.ipynb
3: [PCA application](3-mlml_seawater.ipynb)

4: [OOI spectral analysis](4-ooi-spectral-analysis.ipynb)


__Submission format:__ This project draft will be turned in through a separate Github repository that you create (instructions will be provided in a Git tutorial in class). For the PCA and spectral analysis problems, upload a modified file to your homework 6 Github repository.

__Grading criteria:__  Code runs without errors, code gives correct output, good coding style (documentation, descriptive variable names, not repeating yourself), clear graphics (axis labels and units), and valid statistical interpretation.
