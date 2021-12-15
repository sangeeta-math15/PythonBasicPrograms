#The KeyboardInterrupt exception is raised when you try to stop a running program
# by pressing ctrl+c or ctrl+z in a command line
try:
    inp = input()
    print ('Press Ctrl+C or Interrupt the Kernel:')
except KeyboardInterrupt:
    print ('Caught KeyboardInterrupt')
else:
    print ('No exception occurred')
