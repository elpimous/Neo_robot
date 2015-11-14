#!/usr/bin/env python
# -*- coding: utf-8 -*-

#**************************************************************
#
#    python testing model (accuracy test after adapting
#
#**************************************************************

import os
import rospy
import subprocess


class Test():

  def __init__(self):
    pass


  def runCmdOutput(self, cmd, timeout=None):
        self.ph_out = None # process output
        self.ph_err = None # stderr
        self.ph_ret = None # return code
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if not timeout:
            self.ph_ret = p.wait()
        else:
            fin_time = time.time() + timeout
            while p.poll() == None and fin_time > time.time():
                time.sleep(1)
            if fin_time < time.time():
                os.kill(p.pid, signal.SIGKILL)
                raise OSError("Process timeout has been reached")
            self.ph_ret = p.returncode
        self.ph_out, self.ph_err = p.communicate()
        return self.ph_out

  def accu(self):
     self.link =  "/home/neo/Documents/PAMA"
     os.system("pocketsphinx_batch  -adcin yes  -cepdir /home/neo/Documents/PAMA/test_adapt_model/wav  -cepext .wav  -ctl /home/neo/Documents/PAMA/test_adapt_model/adaptation-test.fileids  -lm /home/neo/Documents/PAMA/model/french3g62K.lm.bin -dict /home/neo/Documents/PAMA/model/frenchWords62K.dic -hmm /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt -hyp /home/neo/Documents/PAMA/test_adapt_model/adapation-test.hyp")

     """
     v = re.search("Decoding 'adapt(.+?)'", decode)
     n = re.search("AVERAGE(.+?) ", decode)
     if v:
       print "vvvvvvvvvvvvvvvvvvvvvvvvv "+v
     if n:
       print "nnnnnnnnnnnnnnnnnnnnnnnnnn "+n
     """
     os.system("cd /home/neo/Documents/PAMA && ./word_align.pl /home/neo/Documents/PAMA/test_adapt_model/adaptation-test.transcription /home/neo/Documents/PAMA/test_adapt_model/adapation-test.hyp")

Test().accu()
