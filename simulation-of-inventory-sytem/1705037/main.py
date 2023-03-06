from utils import *


def initialize():
    global sim_time, initial_inv_level, inv_level, time_last_event
    global total_ordering_cost, area_holding, area_shortage
    global time_next_event
    sim_time = 0.0

    inv_level = initial_inv_level
    time_last_event = 0.0

    total_ordering_cost = 0
    area_holding = 0.0
    area_shortage = 0.0

    time_next_event = [1.0e+30, sim_time + expon(mean_interdemand), num_months, 0.0]


def timing():
    global next_event_type, num_events, time_next_event, sim_time
    min_time_next_event = 1.0e+29
    next_event_type = 0
    for i in range(num_events):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i + 1
            # print(next_event_type)

    if next_event_type == 0:
        outfile2 = open("out.txt", "a")
        outfile2.write("Event list is empty at time " + str(sim_time))
        outfile2.close()
        exit(1)
    sim_time = min_time_next_event


def order_arrival():
    global time_next_event, inv_level, amount
    inv_level += amount
    time_next_event[0] = 1.0e+30


def demand():
    global mean_interdemand, prob_distrib_demand, inv_level
    global sim_time, time_next_event
    inv_level -= random_integer(prob_distrib_demand)
    time_next_event[1] = sim_time + expon(mean_interdemand)


def evaluate():
    global inv_level, smalls, bigs, amount
    global total_ordering_cost, setup_cost, incremental_cost
    global time_next_event, sim_time, minlag, maxlag

    if inv_level < smalls:
        amount = bigs - inv_level
        total_ordering_cost += setup_cost + incremental_cost * amount
        time_next_event[0] = sim_time + uniform(minlag, maxlag)

    time_next_event[3] = sim_time + 1.0


def report():
    avg_ordering_cost = total_ordering_cost / num_months
    avg_holding_cost = holding_cost * area_holding / num_months
    avg_shortage_cost = shortage_cost * area_shortage / num_months

    outfile2 = open("out.txt", "a+")
    outfile2.write("\n\n(" + str(smalls) + "," + str(bigs) + ")\t\t" + str(float("{:.2f}".format(avg_ordering_cost + avg_holding_cost + avg_shortage_cost))) + "\t"*3 + str(float("{:.2f}".format(avg_ordering_cost))) + "\t"*3 + str(
        float("{:.2f}".format(avg_holding_cost))) + "\t"*3 + str(float("{:.2f}".format(avg_shortage_cost))))
    outfile2.close()


def update_time_avg_stats():
    global sim_time, time_last_event, inv_level
    global area_holding, area_shortage

    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time

    if inv_level < 0:
        area_shortage -= inv_level * time_since_last_event
    elif inv_level > 0:
        area_holding += inv_level * time_since_last_event


num_events = 4

infile = open("in.txt", "r")
inputs = infile.read()
inputs = inputs.split()
print(inputs)
initial_inv_level, num_months, num_policies, num_values_demand = int(inputs[0]), int(inputs[1]), int(inputs[2]), int(
    inputs[3])
mean_interdemand, setup_cost, incremental_cost, holding_cost, shortage_cost, minlag, maxlag = float(inputs[4]), float(
    inputs[5]), \
                                                                                              float(inputs[6]), float(
    inputs[7]), \
                                                                                              float(inputs[8]), float(
    inputs[9]), float(inputs[10])

prob_distrib_demand = []
for i in range(11, 11 + num_values_demand):
    prob_distrib_demand.append(float(inputs[i]))
infile.close()

outfile = open("out.txt", "w")
outfile.write("Single-product inventory system\n\n")
outfile.write("Initial inventory level " + str(initial_inv_level) + " items\n\n")
outfile.write("Number of demand sizes " + str(num_values_demand) + " \n\n")
outfile.write("Distribution function of demand sizes\t")
for i in range(num_values_demand):
    outfile.write(str(prob_distrib_demand[i]) + " ")
outfile.write("\n\n")
outfile.write("Mean interdemand time " + str(mean_interdemand) + " months\n\n")
outfile.write("Delivery lag range " + str(minlag) + " to " + str(maxlag) + " months\n\n")
outfile.write("Length of the simulation " + str(num_months) + " months\n\n")
outfile.write("K = " + str(setup_cost) + " i = " + str(incremental_cost) + " h = " + str(holding_cost) + " pi = " + str(
    shortage_cost) + "\n\n")
outfile.write("Number of policies " + str(num_policies) + "\n\n")
outfile.write("\t" + "\tAverage\t\t" * 4 + "\n")
outfile.write("Policy\t" + "total cost\t" + "ordering cost\t" + "holding cost\t" + "shortage cost\t" + "\n")
outfile.close()
count = 0
next_event_type = 0
for i in range(num_policies):
    smalls, bigs = int(inputs[11 + num_values_demand + count]), int(inputs[11 + num_values_demand + count + 1])
    count += 2
    initialize()
    while True:
        timing()
        update_time_avg_stats()
        if next_event_type == 1:
            order_arrival()
        elif next_event_type == 2:
            demand()
        elif next_event_type == 4:
            evaluate()
        elif next_event_type == 3:
            report()
            break
