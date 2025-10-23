Requirements:

* Python 3.x
* SimPy library (pip install simpy)
* matplotlib (for plotting charts)

This project simulates a call center with limited agents using SimPy to study queue behavior and waiting times.

It evaluates how system performance changes with different parameters such as the number of agents, call arrival rate, and service rate.

File 1 – call\_center\_simulation.py:

Runs the main simulation and three experiments:

* Vary number of agents
* Vary call arrival rate
* Vary service rate


File 2 – visualizations.py:

Generates bar charts showing:

* Average Wait Time vs Number of Agents
* Average Wait Time vs Arrival Rate
* Average Wait Time vs Service Rate


To Run the simulation:
    python call\_center\_simulation.py


Generate visualizations:
    python visualizations.py


Libraries: simpy, matplotlib


This simulation helps analyze waiting time, throughput, and agent utilization to understand call center performance and optimize resource allocation.



