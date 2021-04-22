import time 

class CountDownTimer(Timer):
    def run(self):
        counter = self.runTime
        for sec in range(self.runTime):
            print counter
            time.sleep(1.0)
            counter -=1
        print "Done"


c = CountDownTimer()
c.start()
