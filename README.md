# Replicating Large Scale Simulation of Tor 

Our goal is to replicate the results of a paper titled [Large Scale Simulation of Tor](https://www.researchgate.net/publication/221053183_Large_Scale_Simulation_of_Tor).

We simulate the connection tracking attack described in the paper. The paper uses a tool called SSFNet, which has been deprecated since the paper was written. We attempt to produce similar results using a more modern simulation tool called [Shadow](https://shadow.github.io/). 

We use tornetgen to generate the networks and then run shadow on these networks. Results from this experiment can be seen under tornetgen/results and the main scripts used to generate these results are tornetgen/parser.py and tornetgen/plot.py.
