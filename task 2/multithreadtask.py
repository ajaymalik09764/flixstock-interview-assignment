import threading
import time

class myThread(threading.Thread):
   def __init__(self,threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.exitFlag=False


   def run(self):


      print("Starting " + self.name)

      counter=0
      delay=5
      while counter<50:
          if self.exitFlag:
              break

          print("%s is running at %s" % (self.name,counter))
          time.sleep(delay)
          counter+=delay

      print("Exiting " + self.name)

   def stop(self):
     self.exitFlag=True



if __name__ == "__main__":
    thread1=myThread(1,"Thread 1")
    thread2=myThread(2,"Thread 2")
    thread3=myThread(3,"Thread 3")


    #Initially start thread 1 and 3
    thread1.start()
    thread3.start()

    #After 20 second stop thread 1 start thread 2
    time.sleep(20)
    thread1.stop()
    thread2.start()

    #Again after 18 second stop thread 3 and start thread 1
    time.sleep(18)
    thread3.stop()
    thread1=myThread(1,"Thread 1")
    thread1.start()
