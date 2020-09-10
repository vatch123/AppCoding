# Application Layer Coding

The current state of the repository emulates the work of ICC paper.

The entire code is written in python with `numpy` and `matplotlib` as the only dependencies.

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
This will run the first simulation as mentioned in the ICC paper.