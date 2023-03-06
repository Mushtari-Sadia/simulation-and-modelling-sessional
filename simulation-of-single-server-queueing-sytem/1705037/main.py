from utils import *

def initialize():
    global sim_time, server_status, num_in_q, time_last_event
    global num_custs_delayed, total_of_delays, area_num_in_q, area_server_status
    global time_next_event, total_of_delays
    sim_time = 0.0
    server_status = IDLE
    num_in_q = 0
    time_last_event = 0.0
    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0
    total_of_delays = 0.0
    time_next_event = [sim_time + expon(mean_interarrival), 1.0e+30]


def timing():
    global next_event_type, num_events, time_next_event, sim_time
    min_time_next_event = 1.0e+29
    next_event_type = 0
    for i in range(num_events):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i + 1

    if next_event_type == 0:
        outfile = open("out.txt", "a")
        outfile.write("Event list is empty at time " + str(sim_time))
        outfile.close()
        exit(1)
    sim_time = min_time_next_event


def arrive():
    global time_next_event, server_status, num_in_q, time_arrival
    global total_of_delays, num_custs_delayed, sim_time
    time_next_event[0] = sim_time + expon(mean_interarrival)

    if server_status == BUSY:
        num_in_q += 1
        if num_in_q > Q_LIMIT:
            outfile = open("out.txt", "a")
            outfile.write("Overflow of the array time_arrival at " + str(sim_time))
            outfile.close()
            exit(1)
        time_arrival[num_in_q] = sim_time
    else:
        delay = 0.0
        total_of_delays += delay

        num_custs_delayed += 1
        server_status = BUSY

        time_next_event[1] = sim_time + expon(mean_service)


def depart():
    global num_in_q, server_status, time_next_event, num_custs_delayed
    global sim_time, total_of_delays
    if num_in_q == 0:
        server_status = IDLE
        time_next_event[1] = 1.0e+30
    else:
        num_in_q -= 1
        delay = sim_time - time_arrival[1]
        total_of_delays += delay

        num_custs_delayed += 1
        time_next_event[1] = sim_time + expon(mean_service)

        for i in range(1,num_in_q+1):
            time_arrival[i] = time_arrival[i + 1]


def report():
    outfile2 = open("out.txt", "a")
    outfile2.write("\n\nAverage delay in queue " + str(total_of_delays/num_custs_delayed) + " minutes\n\n")
    outfile2.write("Average number in queue " + str(area_num_in_q/sim_time) + "\n\n")
    outfile2.write("Server utilization " + str(area_server_status/sim_time) + "\n\n")
    outfile2.write("Time simulation ended " + str(sim_time) + " minutes\n\n")
    outfile2.close()


def update_time_avg_stats():
    global sim_time, time_last_event, area_num_in_q, num_in_q
    global area_server_status, server_status

    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time
    area_num_in_q += num_in_q * time_since_last_event
    area_server_status += server_status * time_since_last_event


num_events = 2
time_arrival = [None] * (Q_LIMIT + 1)

infile = open("in.txt", "r")
inputs = infile.read()
inputs = inputs.split(' ')
mean_interarrival, mean_service, num_delays_required = float(inputs[0]), float(inputs[1]), int(inputs[2])
infile.close()

outfile = open("out.txt", "w")
outfile.write("Single-server queueing system\n\n")
outfile.write("Mean interarrival time " + str(mean_interarrival) + " minutes\n\n")
outfile.write("Mean service time " + str(mean_service) + " minutes\n\n")
outfile.write("Number of customers " + str(num_delays_required) + "\n\n")
outfile.close()

initialize()

while num_custs_delayed < num_delays_required:
    timing()
    update_time_avg_stats()
    if next_event_type == 1:
        arrive()
    elif next_event_type == 2:
        depart()

report()
