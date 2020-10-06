import threading
import time

class myThread(threading.Thread):
   def __init__(self,threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.exitFlag=False


   def run(self,stop_point=None):

        counter=0
        while True:
            if counter%5==0:
                print("%s is running at %s --- %s" % (self.name,counter,time.time()))

            if stop_point!= None:
                if counter>=stop_point:

                    break
            if self.exitFlag or counter>50:

                break

            time.sleep(1)
            counter+=1
        print("%s is Exiting at %s " % (self.name,time.time()))


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
    thread1.join()
    thread2.start()

    #Again after 18 second stop thread 3 and start thread 1
    time.sleep(18)
    thread3.stop()
    thread3.join()
    thread1=myThread(1,"Thread 1")
    thread1.start()




#output-----
#i have added sec into output so that we can seen 5 sec distance.
"""


Thread 1 is running at 0 --- 1601974507.2539134
Thread 3 is running at 0 --- 1601974507.2649164
Thread 1 is running at 5 --- 1601974512.268181
Thread 3 is running at 5 --- 1601974512.2701814
Thread 1 is running at 10 --- 1601974517.2705617
Thread 3 is running at 10 --- 1601974517.2725623
Thread 1 is running at 15 --- 1601974522.2728307
Thread 3 is running at 15 --- 1601974522.2748334
Thread 1 is running at 20 --- 1601974527.2759948
Thread 1 is Exiting at 1601974527.2779932
Thread 3 is running at 20 --- 1601974527.2779932
Thread 2 is running at 0 --- 1601974527.2789917
Thread 3 is running at 25 --- 1601974532.2803695
Thread 2 is running at 5 --- 1601974532.2823703
Thread 3 is running at 30 --- 1601974537.2826405
Thread 2 is running at 10 --- 1601974537.2846391
Thread 3 is running at 35 --- 1601974542.2849076
Thread 2 is running at 15 --- 1601974542.2869077
Thread 3 is Exiting at 1601974545.2866678
Thread 1 is running at 0 --- 1601974545.2875612
Thread 2 is running at 20 --- 1601974547.2901773
Thread 1 is running at 5 --- 1601974550.2899384
Thread 2 is running at 25 --- 1601974552.2924466
Thread 1 is running at 10 --- 1601974555.2922077
Thread 2 is running at 30 --- 1601974557.2947085
Thread 1 is running at 15 --- 1601974560.296477



"""