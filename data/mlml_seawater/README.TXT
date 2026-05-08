Historical Seawater Data - Moss Landing Marine Labs

--Data Disclaimer-- 
Moss Landing Marine Laboratories (MLML) provides these data "as is", 
with no warranty, expressed or implied, of the data quality or consistency.
It is provided without support and without obligation on the part of MLML to assist in its use, correction, 
modification, or enhancement. For use in publication, authors should obtain written permission from the director of MLML, 
and acknowledge MLML as the data source in those publications.

--Contacts--
Data Manager: Jason Adelaars (jadelaars@mlml.calstate.edu)
MLML Director: Jim Harvey (jharvey@mlml.calstate.edu)

--Data Citation--
[MLML] Moss Landing Marine Labs. 2014. Historical Seawater Data (insert date range) [Internet]. [cited (insert date of download)]. Available from: 

--Brief Narrative--
Seawater data observations are collected from raw seawater drawn through an intake pipe. Prior to October 31, 2013, the intake opening
was set at a depth of ~18.3 m (60ft) below mean lower low water (MLLW). Due to sediment build-up around the pipe, the intake opening was raised to ~16.6m (54.4ft) below MLLW on October 31, 2013.
The intake opening is located at 36.8025N and 121.7915W
The seawater sensors are cleaned of biofouling agents on a weekly/twice-weekly interval, though some data drift can be observed in transmission, beam attenution, and fluorescence.

Full maintenance Log available at: https://docs.google.com/a/mlml.calstate.edu/spreadsheet/ccc?key=0AnH2QAt-nlAldEFwY2ZyNUV6amJtLXllMDljdmM1SFE&pli=1#gid=0

Sensors and Calibrations/Redeployments
Seabird SBE19 CTD: First deployed Sept 3, 2010; swapped with calibrated CTD on Feb 6, 2012; swapped with calibrated CTD on October 18, 2012; swapped with calibrated CTD on Aug 21, 2013; swapped with calibrated CTD on March 27, 2014
AADI Oxygen Optode: First deployed Sept 3, 2010; redeployed following calibration on Aug 13, 2012; 
C-Star Transmissometer (10cm): First deployed Sept 3, 2010; calibrated on January 25, 2012; 
WetStar Fluorometer: First deployed Sept 3, 2010: calibrated on Jan 25, 2012; 
Honeywell Durafet III: First deployed May 4, 2012; replaced Mar 20, 2013; new probe calibrated with AMP & TRIS standards on Mar 26, 2013; new probe calibrated/installed Jun 19, 2014

--QAQC--
Quality assurance and quality control analysis based on standards set forth by Integrated Ocean Observing Systems' (IOOS) Quality Assurance for Real-Time Oceanographic Data (QARTOD): http://www.ioos.noaa.gov/qartod/welcome.html
Flags as follows---
 1 = Pass; Data have passed critical real-time quality control tests and are deemed adequate for use as preliminary data
 2 = Not Evaluated; Data have not been QC-tested, or the information on the quality is not available
 3 = Suspect or of High Interest; Data are considered to be either suspect or of high interest to data providers and users. They are flagged suspect to draw further attention to them by operators
 4 = Fail; Data are considered to have failed one or more critical real-time QC checks. If they are deciminated at all, it should be readily apparent that they are not of acceptable quality.
 9 = Missing data; Data are missing/NULL/NAN

--Quality Checking: Data were checked against the following thresholds--

Temp/Optode Temp: 
 Sensor range test -5<temp<35 
 User range test 4<temp<22
 Spike test mean(temp_1.42hours)+/-2.4*stdev

Conductivity:
 Sensor range test 0<cond<7
 User range test 0.75<cond<1.1
 Spike test mean(cond_1.42hours)+/-2.4*stdev

Salinity:
 Sensor range test 20<cond<50
 User range test 32<cond<35
 Spike test mean(sal_1.42hours)+/-2.4*stdev

Fluorescence:
 Sensor range test 0.03<cond<75
 User range test 0<cond<20
 Spike test mean(fluor_1.42hours)+/-2.4*stdev

Beam Attenuation:
 Sensor range test 0<cond<100
 User range test 0<cond<50

Transmission:
 Sensor range test 0<cond<100
 User range test 0<cond<100

Dissolved Oxygen:
 Sensor range test 0<cond<500
 User range test 0<cond<400
 Spike test mean(do2_1.42hours)+/-2.4*stdev

Dissolved Oxygen Saturation:
 Sensor range test 0<cond<100
 User range test 0<cond<100
 Spike test mean(osat_1.42hours)+/-2.4*stdev

pH:
 Sensor range test 0<cond<14
 User range test 7<cond<10
 Spike test mean(ph_1.42hours)+/-2.4*stdev

--Data Units--
Temp/Optode temp: degrees Celcius
Conductivity: Siemens per meter
Salinity: PSU-78
Fluorescence: micrograms per liter
Beam Attenuation: meters^-1
Transmission: percent (%)
Dissolved Oxygen: micromole per liter
Dissolved Oxygen Saturation: percent (%)
pH: pH units
Tide: feet relative to mean lower low water (obtained from http://tidesonline.nos.noaa.gov/data_read.shtml?station_info=9413450+Monterey,+CA)




