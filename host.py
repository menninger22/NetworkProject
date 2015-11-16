################################################################################
#
# Ricky Galliani, Tim Menninger, Rush Joshi, Schaeffer Reed
# Network Simulator Project
# CS 143 -- Fall 2015
#
# host.py
#
# This contains the host class, which is the object used to represent a
# host in the network.
#
################################################################################






################################################################################
#                                                                              #
#                               Imported Modules                               #
#                                                                              #
################################################################################

# So we can use command line arguments.
import sys

# Import network objects
import packet as p
import link as l
import router as r
import flow as f
import event as e

# Import the constants and the conversion functions
import constants as ct
import conversion as cv

# Import utility functions
import utility as u

# Import functions to carry out the simulation
sim  = sys.modules['__main__']

# Import the config parser
import config_parser as cp

# Import the queue Python package for the link buffers which are FIFO
import queue

# Import heapq library so we can use it for our events.
import heapq 


################################################################################
#                                                                              #
#                                   Host Class                                 #
#                                                                              #
################################################################################

class Host:

	def __init__(self, the_host_name):
		''' 
		Initialize an instance of Host by intitializing its attributes.
		'''
		# Name of the host, each hostname is unique string (i.e., "H1")
		self.host_name = the_host_name
		
		# The link_name representing the Link to this Host
		self.link = None
		
		
	def add_link(self, link_name):
		'''
		Adds a link to the list of links.
		'''
		self.link = link_name
		
		
	def send_packet(self, arg_list):
		'''
		Enqueues a packet to be sent.
		'''
		# The argument list is just the packet.
		[packet] = arg_list
		print (self.host_name + ' sending packet ' + packet.ID + ' at time ' + str(sim.network_now()))
		
		# First want to put the current time on the packet so we can calculate
		#	RTT later.
		packet.time = sim.network_now()
		
		# Get the link that we are going to send the packet on.
		link = sim.links[self.link]
		
		# Give the packet to the link to handle.  Here, it will either be
		#	enqueued on a buffer or transmitted.
		link.put_packet_on_buffer(self.host_name, packet)
		
		
	def receive_packet(self, arg_list):
		'''
		Receives a packet and responds to it depending on whether it is data or
		acknowledgement.
		'''
		# Unpack the argument list.
		[flow_name, packet_ID] = arg_list
		packet = sim.packets[(flow_name, packet_ID)]
		flow = sim.flows[flow_name]
		
		# If this is a data packet, create an ack packet and send it back.
		if packet.type == ct.PACKET_DATA:	
			# This is what we want, create an ack packet and send it.
			ack_pkt = p.Packet('ack_' + flow.create_packet_ID(), flow_name,
							   self.host_name, packet.src, ct.PACKET_ACK,
							   ct.PACKET_ACK_SIZE)
							   
			# Set the data of the ack to be what we are expecting.  The src will
			#	cross check this with what he sent and resend or not accordingly
			ack_pkt.set_data(flow.expecting)
			
			# Add the packet to our dictionary of packets.
			sim.packets[(flow_name, ack_pkt.ID)] = ack_pkt
			
			# Send the packet!
			self.send_packet([ack_pkt])
			
			# Check if it is the one that this dest is expecting.
			if packet.data == flow.expecting:
				# Increment what we are now expecting.
				flow.expecting += 1
				
		elif packet.type == ct.PACKET_ACK:
			# If this is acknowledgement, see if any packets were lost.
			if packet.data == flow.to_complete:
				# This is what we were waiting for.  We now have one more
				#	complete
				flow.to_complete += 1
				flow.window_size += 1
				if len(flow.packets_in_flight) > 0:
					heapq.heappop(flow.packets_in_flight)
				flow.update_flow()
				
			else:
				# Packets were lost.  Resend any and all that were in flight.
				flow.window_size -= 1
				flow.resend_inflight_packets()
				
		
		
		
		
		
		
		
		
