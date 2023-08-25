import time
import matplotlib.pyplot as plt

outputs = []
for i in range(50000):
    outputs.append((i, time.time_ns()))

x = []
y = []
# Change file name to match each scenario
# 1. No credit on EC2
# 2. Credit on EC2
# 3. VM
# 4. Physical Machine
file = open("cpu_test_scenario_4.txt", "w")
for i in range(len(outputs)):
    file.write(str(outputs[i][0]) + ", " +
               str((outputs[i][1]-outputs[0][1])/1e9) + "\n")
    x.append(outputs[i][0])
    y.append((outputs[i][1]-outputs[0][1])/1e9)
file.close()

print("CPU Test time to run 50,000 iterations: ", y[-1], "s")

plt.plot(x, y)
plt.xlabel("Iteration")
plt.ylabel("Time (s)")
plt.title("CPU Test")
plt.savefig("cpu_test_scenario_3.png")
plt.show()
