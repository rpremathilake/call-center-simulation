import matplotlib.pyplot as plt

# Sample data from experiments (replace with your actual results)
agents = [2, 3, 6]
avg_wait_agents = [4.5, 2.8, 0.9]  # average wait times in minutes
avg_queue_agents = [3.5, 2.0, 0.5]  # average queue lengths
util_agents = [90, 70, 50]  # utilization %

arrival_rates = [0.5, 0.75, 1.0]
avg_wait_arrival = [2.8, 5.5, 11.0]
avg_queue_arrival = [2.0, 4.5, 10.0]
util_arrival = [70, 90, 100]

service_rates = [1/3, 1/2, 1]
avg_wait_service = [2.8, 1.5, 0.7]
avg_queue_service = [2.0, 1.0, 0.0]
util_service = [70, 60, 40]

# Visualization 1: Bar Chart - Average Wait Time vs Number of Agents
plt.figure(figsize=(8, 5))
plt.bar(agents, avg_wait_agents, color='skyblue')
plt.xlabel('Number of Agents')
plt.ylabel('Average Wait Time (min)')
plt.title('Experiment 1: Average Wait Time vs. Number of Agents')
plt.xticks(agents)
plt.grid(axis='y')
plt.show()

# Visualization 2: Line Plot - Average Wait Time vs. Arrival Rate
plt.figure(figsize=(8, 5))
plt.plot(arrival_rates, avg_wait_arrival, marker='o', color='salmon', label='Wait Time')
plt.xlabel('Arrival Rate (calls/min)')
plt.ylabel('Average Wait Time (min)')
plt.title('Experiment 2: Average Wait Time vs. Arrival Rate')
plt.grid(True)
plt.legend()
plt.show()

# Visualization 3: Bar Chart - Average Queue Length vs. Service Rate
plt.figure(figsize=(8, 5))
plt.bar([f"{1/s:.1f} min/call" for s in service_rates], avg_queue_service, color='lightgreen')
plt.xlabel('Average Service Time per Call')
plt.ylabel('Average Queue Length')
plt.title('Experiment 3: Average Queue Length vs. Service Rate')
plt.grid(axis='y')
plt.show()