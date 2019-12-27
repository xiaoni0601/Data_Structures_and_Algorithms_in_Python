#队列的应用：
#打印任务问题：模拟流程
# 1. 创建打印队列对象；
# 2.时间按照秒的单位流逝（按照概率生成打印作业；if打印机空闲；if打印机；if打印完成）；
# 3.时间用尽，开始统计平均等待时间

from pythonds.basic.queue import Queue
import random
#定义如下对象类：
class Printer: #定义打印机的类，包括：初始化init方法；打印一秒tick；忙busy与否；打印新作业。
    def __init__(self,ppm):
        self.pagerate = ppm #打印速度，每分钟多少页数
        self.currentTask = None #当前打印任务，初始化的时候处于空闲状态，none
        self.timeRemaining = 0 #任务倒计时，还差多少时间打印完毕
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages()  * 60/self.pagerate #ppm为分钟换算成秒*60
    
    
class Task: #包括1.初始化；2.返回生成时间戳；3.返回页数；4.等待时间
        def __init__(self,time):
            self.timestamp = time #生成时间戳
            self.pages = random.randrange(1,21) #打印页数
        def getStamp(self):
            return self.timestamp
        def getPages(self):
            return self.pages
        def waitTime(self,currenttime):
            return currenttime - self.timestamp
    
def newPrintTask():
        num = random.randrange(1,181) #概率是1/180，期间均为true，之外为false
        if num == 180:
            return True
        else:
            return False

def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.busy()) and \
            (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()
    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average wait %6.2f secs %3d tasks remaining." %(averageWait,printQueue.size()))
for i in range(10):
    simulation(3600,5)
for i in range(10):
    simulation(3600,10)
