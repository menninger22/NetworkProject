Questions for Ritty:

The acknowledgement question

How/when are packets made 

Does it take time to make packets?

Does host need to remember how much data it's sending?  How much it's received?



If we are doing Discrete Event Simulation, what do the events look like?  
The global queue of events store (Event, time) tuples, right?

Use heapqueue from python

simulating 
while heapqueue:
	pop event
	forward time to time of that event
	call handle functions

Can we talk through the process of sending packets from one host to another
and as it relates to the Link Rate, Link Delay, and Link Buffer? Just need
general clarification as for what those terms are and how they affect the 
process of sending packets from hosts to other hosts/routers. 

Need to get good definitions for some important terms, hard to find: 
1. Buffer Occupancy

	per-link, per-directions (because there are two buffers for each link)
	Just how many packets are in the buffer versus how big the buffer is (65%)

	Buffer Size: 64 KB

	Sum of all packets in the buffer / Buffer Size

2. Packet Loss 
 	(Just the number of packets lost, right? But is it per flow? total?)


3. Flow Rate

	How many kilobytes per second (throughput)
	Just the data packets

Do our classes have all the attributes they need to be able to measure 
everything that they need to measure?  

Do we need a simulation class? / Where is the best place to store the data 
for the metrics during the simulation? 

-- Amount of time to transmit a packet onto a link --
packet transmission time = packet size / link rate


Steps to complete for Test Case 0

1) Load network topology 
2) Make objects
3) Create routing tables
4) Flow 1 make a data packet
5) Host 1 will send the data packet
6) Link 1 will enqueue the packet to its buffer
7) Link 1 will carry the data packet
8) Host 2 will receive the data packet
9) Make an ack packet
10) Link 1 will enqueue the ack packet
11) Link 1 will carry the ack packet 
12) Host 2 will receive an ack packet


