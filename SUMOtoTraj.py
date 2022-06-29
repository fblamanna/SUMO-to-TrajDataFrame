#
# Run SUMO Shell from Python Script
# Export FCD output data and build a trajdataframe to be imported in scikit-mobility
# $ python3 SUMOtoTraj.py <project name> <output file name> <probability>
#
#
# Import Packages
import pandas as pd
import skmob
import os
import sys

# ---------------------------
# Run SUMO
# ---------------------------

# Run Simulation and get output file
os.system("sumo -c " + sys.argv[1] + ".sumocfg \
			--fcd-output " + sys.argv[2] + ".xml" + " \
			--device.fcd.probability " + sys.argv[3] + " \
			--fcd-output.geo")

# Convert output from xml to csv
os.system("python3 /usr/share/sumo/tools/xml/xml2csv.py " + sys.argv[2] + ".xml")

# ---------------------------
# FCD to Traj - Trajdataframe
# ---------------------------

# Read csv
df = pd.read_csv(sys.argv[2] + '.csv', sep=';')

# Convert datetime column - steps to datetime - current datetime + delta
df['datetime'] = pd.to_datetime('now', utc=True) + pd.to_timedelta(df['timestep_time'], unit='s')

# TrajDataFrame from Dataframe
tdf = skmob.TrajDataFrame(df,  
                          longitude='vehicle_x', 
                          latitude='vehicle_y',
                          datetime='datetime', 
                          user_id='vehicle_id')
