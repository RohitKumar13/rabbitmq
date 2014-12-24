#!/usr/bin/env python

import os
import pika
from ConfigParser import SafeConfigParser

## Read from configuration file
path = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'configuration.ini'
parser = SafeConfigParser()
parser.read(path)
RabbitMQ_hostname = parser.get('RabbitMQ_connection', 'host_name')
queue_name = parser.get('RabbitMQ_connection', 'queue_name')

class RabbitMQ(object):
	
	def __init__(self):
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(RabbitMQ_hostname))
		self.channel = self.connection.channel()
		
	def send_data(self, queue_name, send_data):
		self.channel.queue_declare(queue_name)
		self.channel.basic_publish(exchange='', routing_key = queue_name, body = send_data)
		self.connection.close()
	
	def receive_data(self, queue_name):
		self.channel.queue_declare(queue_name)
		def callback(ch, method, properties, body):
			print " [x] Received %r" % (body,)
		self.channel.basic_consume(callback,queue=queue_name,no_ack=True)
		self.channel.start_consuming()

	
if __name__ == "__main__":
	    dRMQ = RabbitMQ()
	    dRMQ.send_data(queue_name,'add your message here')
	    dRMQ.receive_data(queue_name)


