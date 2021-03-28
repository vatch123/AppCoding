# Application Layer Coding for Delay and Feedback Constraints Scenarios

#### This repository is not being actively maintained but most of the functionality of [[1]](#1) has been implemented. The entire code was ported in MATLAB for further experiments which would be released shortly.

The current state of the repository emulates the work of the paper [[1]](#1).

The entire code is written in python with `matplotlib` as the only dependency.

There are two runnable scripts:
* system.py
* simulation.py

`system.py` performs one transmission of `n` messages from a sender to receiver over a defined a channel
and other parameters. `simulation.py` has a set of simulation as designed in the paper for easy comparison of results.

### Using system.py

* All the different settings that can be used can be listed using the following command
```
python system.py -h
```
This will open the help menu enumerating all the options and how to use

* The file can be run with a particular setting as
```
python system.py -l 8 -n 50 -c Bernouli --scheme ICC
```
This will set the message length as 8 and the number of messages to be 10 transmitted over a Bernouli channel with ICC coding scheme (the scheme in the paper).

* Running with default options
```
python system.py
```
This will transmit `8` bit long `10,000` messages over a bernouli channel with erasure probability of `0.5` and feedback erasrue probability of `0.4` and packet size `4`. 


### Using simulation.py

* It is very straightforward to run. There are five simulations currently more can be added later.
```
python simulation.py
```
This will run all the simulations with similar settings as in the paper. It will show the results as a plot on the screen. Additionally it will also store the plots in a folder name 'plots' and the results of each run in a file in 'logs' folder. The entire thing may take a few minutes to run.

* If you want to run a particular simulation use
```
python simulation.py -n 1
```
This will run the first simulation as mentioned in the paper.

## References
<a id="1">[1]</a> S. S. Borkotoky, U. Schilcher and C. Raffelsberger, *"Application-Layer Coding with Intermittent Feedback Under Delay and Duty-Cycle Constraints,"* ICC 2020 - 2020 IEEE International Conference on Communications (ICC), Dublin, Ireland, 2020, pp. 1-6, doi: 10.1109/ICC40277.2020.9148646.
