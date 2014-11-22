import aiml
import sys
	
k = aiml.Kernel()

	
k.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")

	
k.respond("load aiml b")

	
while True: print k.respond(raw_input("> "))
