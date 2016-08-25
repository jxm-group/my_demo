#!/usr/bin/env python
#coding:utf-8
'''
Created on Sep 17, 2014

@author: root
'''

import commands
import os,sys 

if os.name == 'posix' and sys.version_info[0] < 3:
    import subprocess32 as subprocess
else:
    import subprocess


class MultiMonitor(object):
    def __init__(self,parent=None):
        super(MultiMonitor,self).__init__()

    #***********************
    # 验证　xrandr 有没有
    #**********************
    @classmethod 
    def checkXrandr(cls,command):
        pass

    #获取 命令行 的执行结果
    @classmethod
    def __execUnixCmd(cls,command):
        output = ""
        statusOutput = commands.getstatusoutput(command)    # 得到命令行标准输出
        if statusOutput[0] == 0:                            # 如果是0，则执行成功
            output = statusOutput[1]                        # 第二个元素就是命令行执行后的输出
        else:
            output = ""

        result = output.split("\n")
        return result


    #***********************
    #获取当前连接的显示器
    #**********************
    @classmethod
    def getCurActiveMonitors(cls):
        monitorList = []
        atemp = MultiMonitor.__execUnixCmd("xrandr |awk '/connected/'")
        temp = cls.__execUnixCmd("xrandr |awk '/connected/'")

        for i in range(len(temp)):
            if(temp[i].split(" ")[1] == "connected"):
                monitorList.append(temp[i].split(" ")[0]);

        return monitorList

    # ********************************
    # 获取当前连接的显示器名称
    # 返回: 列表 ["name1","name2"....]
    # *******************************
    def getActiveMonitors(self):
    
        #QStringList monitorList, temp;
        monitorList = []
        temp = MultiMonitor.__execUnixCmd("xrandr |awk '/connected/'")
       
        for i in range(len(temp)):
            if(temp[i].split(" ")[1] == "connected"):
                monitorList.append(temp[i].split(" ")[0]);

        return monitorList

    @classmethod
    def setSingelMonitors(cls):
        try:
            monitorsList  = cls.getCurActiveMonitors()
            print str(monitorsList)
            if len(monitorsList) > 1 :
                for i in range(len(monitorsList)):
                    if i > 0:
                        cmd = "xrandr --output %s --off "% monitorsList[i]
                        os.system(cmd)  # 关闭 屏幕
            return 0
        except Exception:
            return -1


    #获取当前屏幕分辨率
    def getCurrentResolution(self):
        temp = MultiMonitor.__execUnixCmd("xrandr |awk '/connected/'");
        print "---:",temp
        for i in range(len(temp)):
            if(temp[i].split(" ")[1] == "connected"):
                resolution = temp[i].split(" ")[2]
        #print resolution,"----"  
        return resolution

    def enableSameDoubleMonitor(self):

        monitorsList = self.getActiveMonitors()
        if(len(monitorsList) == 1):
            return -1
        if(len(monitorsList) == 0):
            return -2
        resultionList = self.getMulCurrentResolution()
        if(len(resultionList) == 0):
            return -3
        resultion = resultionList[0].split("+")[0]


        cmd = "xrandr --output %s --off "% monitorsList[1]
        os.system(cmd)  # 关闭双屏

        # cmd = "xrandr --auto  --output " + monitorsList[0] + " --mode " + resultion
        cmd = "xrandr --output %s --auto "% monitorsList[1]
        os.system(cmd)

        return 0
    
    #启用多显示器(双平异显）
    def enableMultiMonitor(self):

        monitorsList = self.getActiveMonitors()
        if(len(monitorsList) == 1):
            return -1
        if(len(monitorsList) == 0):
            return -2
        resultionList = self.getMulCurrentResolution()
        if(len(resultionList) == 0):
            return -3
        resultion = resultionList[0].split("+")[0]

        # "xrandr --output VGA1 --auto --right-of LVDS1 --primary" # 主屏幕VGA1  ,
        # "xrandr --output VGA1 --auto --right-of LVDS1"            # 主屏幕LVDS1, VGA1 位于 右边
        #  xrandr --output VGA1 --auto --right-of LVDS1 --mode 800x600

        # cmd = "xrandr --auto  --output " + monitorsList[0] + " --mode " + resultion
        cmd = "xrandr --output %s --auto --right-of %s "% (monitorsList[1],monitorsList[0])
        os.system(cmd)
        return 0

    def getMulCurrentResolution(self):

        temp = MultiMonitor.__execUnixCmd("xrandr |awk '/connected/'");
        resolutionList = []
       
        for i in range(len(temp)):
            if(temp[i].split(" ")[1] == "connected"):
                resolution = temp[i].split(" ")[2]
                resolutionList.append(resolution)

        return resolutionList
    
    #禁用多显示器
    def disableMultiMonitor(self):

        monitorsList = self.getActiveMonitors()
        if(len(monitorsList) == 1):
            return -1
        if(len(monitorsList) == 0):
            return -2
        resultionList = self.getMulCurrentResolution()

        if(len(resultionList) == 0):
            return -3
        cmd = "xrandr "
        for i in range(1,len(monitorsList)):
            if i != 0: 
                cmdTemp = cmd + " --output " + monitorsList[i] + " --off "
                os.system(cmdTemp)
        return 0
      
    # 获取终端所支持分辨率列表
    def getScreenResolutionlist(self):
        screenResolution = []
        #xrandr | grep -v "disconnected"  |grep -v "Screen"  |  grep " .*x" | sed "s/^\ \ \ //g" | sed "s/\ connected\ */--/g" | sed "s/primary //g" | sed "s/\ .*$//"

        cmd = "xrandr | grep -v \"disconnected\" |grep -v \"Screen\"" \
            + "|grep \" .*x\" | sed  \"s/^\ \ \ //g\" | sed \"s/\ connected\ */--/g\"" \
            + "| sed \"s/primary //g\"| sed \"s/\ .*$//\""
        try:
            f = os.popen(cmd, "r")
            while True:
                x = f.readline().strip('\n')  # 去掉\n
                if x == "":
                    break
                screenResolution.append(x)
            f.close()
            #screenResolution.reverse()
            return screenResolution
        except Exception:
            raise Exception("getScreenResolution err")

    # *********************************
    # 略微　复杂 ,
    # *********************************
    def getScreenResolution_List(self):
        resolution_list = self.getScreenResolutionlist()
        #print resolution_list
        resolution_tmp=[]
        tmp = [] 
        for resolution in  resolution_list :
            if resolution.find("--") >= 0:
                #print resolution, "find"
                if len(tmp) > 0:
                    resolution_tmp.append(tmp)
                tmp = [] 
            tmp.append(resolution)

        if len(tmp) > 0: 
            resolution_tmp.append(tmp)
        return  resolution_tmp                

def test_main_01():
 
    mutimonitor = MultiMonitor()
    # print "当前分辨率:", mutimonitor.getCurrentResolution() # 获取当前分辨率
    print "屏幕列表  :",mutimonitor.getActiveMonitors()
    
    #mutimonitor_list = mutimonitor.getScreenResolutionlist()
    #print mutimonitor_list

    mutimonitor_list = mutimonitor.getScreenResolution_List()
    print "分辨率列表"
    for mutimonitor in mutimonitor_list:
        print ":" ,mutimonitor

    #print "启用双屏异显:", mutimonitor.enableMultiMonitor() #启用多显示器(双平异显）
    #print mutimonitor.enableSameDoubleMonitor()  #启用多显示器(双平同显）
    #print mutimonitor.disableMultiMonitor()

if __name__ == "__main__":
    print "\033[0;31;1m --- test main --- \033[0m"
    test_main_01()
    print "\033[0;32;1m --- test end ---\n \033[0m"

