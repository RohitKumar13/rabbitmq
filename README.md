rabbitmq
========

A Python script to send and recieve messages/data from RabbitMQ.

## Install 
>sudo apt-get install rabbitmq-server

Ref : http://www.rabbitmq.com/install-debian.html

## Python Plugins
To install libraries run : 
> sudo pip install -r requirements.txt
 
 or install pika
 
 > sudo pip install pika==0.9.8

## Description
   rabbitmq.py
   - send_data() : To post message/data to queue
   - receive_data() : To pull message/data from queue
   
## Configuration
   configuration.ini -  add your configuration details here 



