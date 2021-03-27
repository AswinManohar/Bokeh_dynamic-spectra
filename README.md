# Bokeh_dynamic-spectra

Visualize plots generated from the single_pulse_search.py with boxtool to select data points and generate dynamic spectra.
Input:  filename, results_location


For the purpose of generating dynamic spectrum for selected pulses in the plot, we built our
own interactive single pulse plotter. The interactive single pulse plotter is a simple web application
that takes the file name as input and accesses the the corresponding raw data from the database.
It then works on the ".singlepulse" files to generate a single pulse plot that allows one to zoom
into the pulse of interest with an accuracy of concentrating one pulse at particular time and DM.
In addition to that, one can also use a crop tool to highlight any particular cluster in the plot and
generate dynamic spectrum for all the pulses within the cluster. The dynamic spectrum is generated
using DSPSR (Digital signal processing of pulsar astronomical timeseries).

![alt text](https://drive.google.com/drive/my-drive/Screenshot from 2021-03-27 12-51-00.png)
