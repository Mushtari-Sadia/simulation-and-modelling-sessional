# simulation-and-modelling-sessional
This repository contains all the assignments from CSE412 course.



## simulation-of-single-server-queueing-sytem

The task is to perform a simulation of a single-server queueing system.

The system as well as the performance measures is described in the text book in section 1.4.

The input and output should be text files. FIGURE 1.19 ( in Section 1.4.5 Simulation Output and Discussion) shows an example of the input and the output.

## monte-carlo-simulation

### 5a
This task is related to the optimal stopping problem, or more specifically, the optimal stopping marriage problem. For a light-hearted introduction to the marriage problem, you may go through the link:
https://www.npr.org/sections/krulwich/2014/05/15/312537965/how-to-marry-the-right-girl-a-mathematical-solution


The rules are as follows,

(1) There is a population of potential candidates (size n) from which one has to be selected.

(2) You may meet or interview by picking one candidate from the population. In this way, you can meet the entire population one at a time.

(3) After each interview, you have to decide if this candidate is the one to be selected. If 'yes', the process terminates (success or failure can be determined at this point). If 'no', the process continues until the entire population is exhausted (remember that if the population is exhausted, then the last candidate is the one who will be selected, according to rule 1).

(4) Once a candidate is rejected after the interview, you can not go back for a review and the rejection is final.

A strategy may be followed where a sample group of size m is to be interviewed at first only for the purpose of setting a standard which is the best from this sample group. Nobody can be selected from this sample group while interviewing them one after the other. After the standard is set, anyone who is better than the standard will be selected.

For this task, you have to take an input of population size n, sample size m, and the sucess criterion s. Here, s can be 1, 3, 5, or 10 which means the strategy is successful if the best or anyone from top 3 or top 5 or top 10 was selected.

For a certain value of n, assume that each candidate has a unique rank from 1 to n and the sample size m can be from 0 to n-1. For a fixed value of n and s, the output is the probability of success of a sample size m. From the output, we can know the probability distribution of success  of a strategy (m), given the value of population size n and the success defined by s.

You may do this simulation by excel (spreadsheet) or by writing a program. 

### 5b

The Monte-carlo technique originated during the second world war 
atomic bomb development. The bomb which was dropped on 06 August, 
1945 had around 60 Kg of fissionable mass. Less than one Kg underwent 
nuclear fission, but it was enough to produce an explosion which 
released energy equivalent to 15 kilotons of TNT and destroyed a city. 
In nuclear fission, a neutron is bombarded to hit a nucleus of an atom 
(uranium-235 or plutonium-239). When an atom undergoes nuclear 
fission, a few neutrons (the expected number depends on several 
factors, usually between 2.5 and 3.0) are ejected from the reaction. 
These free neutrons will then interact with the surrounding material, and 
if more fissile fuel is present, some may be absorbed and cause more 
fissions. Thus, the cycle repeats to give a reaction that is self-sustaining. 
The critical mass is the smallest amount of fissile material needed for a 
sustained nuclear chain reaction. When a nuclear chain reaction in a 
mass of fissile material is self-sustaining, the mass is said to be in a critical state in which there is no increase or decrease in power, temperature, 
or neutron population. 
Suppose pi, i = 0, 1, 2, 3 are the probabilities that a neutron will result in a fission that produces i new neutrons. The task is to calculate the 
probability distribution of the number of neutrons produced in the n-th 
generation of a chain reaction. 
This problem is similar to problems like spreading a disease. Also, it is 
related to family name extinction problem studied during nineteenth 
century. For the family name extinction problem, p0 = 0.4825 and pi = 
(0.2126) (0.5893)^(i -1). 
Assume i = 0, 1, 2, 3 and calculate the probabilities of having 0, 1, 2, 3, 4 number of neutrons in the n-th generation.

## output-data-analysis


A spreadsheet simulation for single-server queueing system is to be done for output data analysis.

(1) Consider rho is 0.9 (if interarrival times has 60 seconds as mean, then the service time has a mean of 54 seconds) and simulate for at least n =  1000 replications (runs) and each replications with at least m = 500 customers.

(2) The starting conditions should be varied with the number of customers, s = 0, 5, 10, 12, 15. Here s represents the number in system at time zero.

(3) For each starting condition, show the plot of E(Di) for n = 250, 500, 750, 1000 replications in a single graph  considering m = 500 customers.

(4) Finally, show the plot of E(Di) for n = 1000 replications and m = 500 customers for different starting conditions s in a single graph. 

## project-scheduling-with-triangular-distributions

PERT (Program Evaluation and Review Technique) Chart Analysis is a widely used project management tool for scheduling, organizing,
and coordinating tasks within a certain project. The PERT Chart provides a graphical representation of a project's timeline, enabling
project managers to break down each individual task within the project for analysis.
In this assignment, we will analyze two simulated projects using information from their corresponding PERT charts. We will use following 3
(three) probability distributions in this assignment to introduce stochasticity in the simulation.
1. Triangular TRIANG(a, b, m) distribution
2. Right-triangular RT(a, b) distribution
3. Left-triangular LT(a, b) distribution
Here, a is location parameter, b-a is scaling parameter, and m is shape parameter. These distributions will be used to determine the
duration of each task within a project.

## simulation-of-inventory-sytem

The task is to perform a simulation of an inventory system.

The system as well as the performance measures is described in the text book in section 1.5.

The input and output should be text files. FIGURE 1.44 ( in Section 1.5.4 Simulation Output and Discussion) shows an example of the input and the output.