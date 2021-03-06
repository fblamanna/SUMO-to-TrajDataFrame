# SUMO to TrajDataFrame

This repository contains scripts and methods to convert a [FCD](https://sumo.dlr.de/docs/Simulation/Output/FCDOutput.html) (Floating Car Data) simulation output from SUMO to a `TrajDataFrame` able to be used in [scikit-mobility](https://github.com/scikit-mobility/scikit-mobility) package.

## Requirements
External packages required are *pandas* and *scikit-mobility* (see [installation guide](https://github.com/scikit-mobility/scikit-mobility#installation)). SUMO is required to perform the simulations.

## SUMO Configuration

1. Get SUMO Network from OpenStreetMap

Since a `TrajDataFrame` requires geographical coordinates of vehicle traces (latitude and longitude), we start building a network in SUMO from OSM with the built-in importer (see [this tutorial](https://sumo.dlr.de/docs/Tutorials/OSMWebWizard.html)). Once imported, the network should be up and running in your SUMO-gui interface.

2. Build SUMO config file (*.cfg*)

We have to run the simulation through command line to get the Floating Car Data outputs (FCD). SUMO provides a *.cfg* file complete with all the information needed to run a simulation within the selected area and the time period. The minimum requirements of a SUMO configuration file are the network (*.net.xml*) and demand (*.rou.xml*) files:

~~~
<configuration>
    <input>
        <net-file value="<project name>.net.xml"/>
        <route-files value="<project name>.rou.xml"/>
    </input>
</configuration>
~~~

If you imported the network through OSM directly into SUMO, you should already find a *.cfg* file in the imported project folder. This is ready to be parsed by the `SUMOtoTraj.py` script. For further configuration options please take a look at [this page](https://sumo.dlr.de/docs/Basics/Using_the_Command_Line_Applications.html).

## SUMOtoTraj

The script workflow takes the following steps:
1. Run a SUMO simulation according to *.cfg* file
2. Convert FCD *.xml* file to a FCD *.csv* file
3. Convert the *.csv* file into a DataFrame and `TrajDataFrame`

### Procedure

Just put the script into your working directory (or point it to the path of the script) and run:

`$ python SUMOtoTraj.py project_name outputfile_name vehicle_sample`

where:

- *project_name* is the name of the .cfg file
- *outputfile_name* is the name of the FCD output file generated by SUMO
- *vehicle_sample* (float) is the desired set of vehicles which generate fcd output (0 to 1, all vehicles)

The script returns:

- a *outputfile_name.xml* FCD file
- a *outputfile_name.csv* FCD file
- a `TrajDataFrame`

## Examples
You may find some examples of running the script and working with a `TrajDataFrame` in the [notebook page](https://github.com/fblamanna/SUMO-to-TrajDataFrame/tree/main/notebook)