# Link Class

from CS143Project.misc.constants import *

class Link:

	def __init__(self, the_link_name, the_capacity, the_delay, the_buffer, 
			     endPt1, endPt2):
		'''
		Initialize an instance of Link by intitializing its attributes.
		'''
		# Name of the Link, each name is a unique string (i.e. "L1")
		self.link_name = the_link_name

		# Flag indicating whether Link is used/free in one direction
		#     LINK_USED_HIGH -> Used in direction of higher Host/Router name
		#     LINK_USED_LOW  -> Used in direction of lower Host/Router name
		#     LINK_FREE      -> Free in both directions
		self.in_use = LINK_FREE

		# How fast the Router can send data (in MB/sec) 
		self.rate = the_rate

		# How much data can be stored in the buffer (in KB)
		self.buffer_size = the_buffer_size

		# Amount of time it takes to send Packet down link (in ms)
		self.delay = the_delay

		# Define the endpoints so we know how to define flow on this 
		# half-duplex link. Could be a Router or Host
		self.end_points = (end_pt1, end_pt2)

		# Router buffer which will hold the Packet before the
		# corresponding Packet are transmitted to Link 
		self.buffers = ([],[])
		
		# Packet currently on the link
		self.packets_carrying = []
		
		# Amount of data on link
		self.current_load = 0
		
	def enqueue_packet():
		'''
		Adds a Packet to the Packet queue where it will wait to be transmitted
		along this link.
		'''

	def dequeue_packet():
		'''
		Dequeues a Packet from the Packet queue to transmit along this link.
		'''

	def carry_packet():
		'''
		Updates the Link to reflect that a packet is now in transmission.
		'''

	def print_contents():
		'''
		Prints the status of all atributes of this Pink.
		'''




	# def carryPacket(self, packet):
	# 	'''
	# 	Update to reflect that packet is being sent on link.  This returns an 
	# 	appropriate error code.
	# 	'''
	# 	# Make sure the packet is able to be sent on this link.
	# 	if packet.src not in self.endPoints:
	# 		return LINK_ERROR
	# 	elif packet.dest not in self.endPoints:
	# 		return LINK_ERROR
			
	# 	# Check if there is enough space for this packet
	# 	if self.currentLoad + packet.size > self.capacity:
	# 		return LINK_FULL
		
	# 	# Make sure the data is going in the correct direction.
	# 	if self.in_use != LINK_FREE:
	# 		if packet.dest == endPoints[1] and self.in_use != LINK_USED_HIGH:
	# 			return LINK_FULL
	# 		elif self.in_use != LINK_USED_LOW:
	# 			return LINK_FULL
	# 	elif packet.dest == endPoints[1]:
	# 		self.in_use = LINK_USED_HIGH
	# 	else:
	# 		self.in_use = LINK_USED_LOW
			
	# 	# Add the data to the link
	# 	self.packetsCarrying.append(packet)
	# 	self.currentLoad += packet.size
		
	# 	return SUCCESS
		

	# def print_contents(self):
	# 	'''
	# 	Prints the contents of the Link to standard output.
	# 	'''
	# 	print("-" * 25)
	# 	print("Link Name: " + self.link_name)
	# 	print("Link: " + str(self.in_use))
	# 	print("Capacity: " + str(self.capacity))
	# 	print("Delay: " + str(self.delay))
	# 	print("-" * 25)
