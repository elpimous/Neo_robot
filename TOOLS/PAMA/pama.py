#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
##############################################################
#
#  A TKINTER ELPIMOUS PROGRAM FOR POCKETSPHINX ADAPTATION
#
#  CALLED : P.A.M.A = POCKETSPHINX ACOUSTIC MODEL ADAPTATION
#
#  HOPE IT WILL BE USEFUL
#
#  VINCENT FOUCAULT /                          elpimous@2015
#
##############################################################

import re
import subprocess  
import glob
import tempfile
import pyaudio
import sys
import wave
import os
import difflib
import tkMessageBox
import matplotlib.pyplot as plt
import numpy as np
import fileinput
from pylab import *
from time import sleep
from array import array
from struct import pack
from tkMessageBox import *
from random import choice

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

from PIL import ImageTk, Image
import Tkinter as tk


# fonctions for the GUI #############################################################################################

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('Pocketsphinx_Acoustic_Model_Adaptation -- ver.02.00 --                     elpimous12@orange.fr  ')
    geom = "786x450"
    root.geometry(geom)
    w = Pocketsphinx_Acoustic_Model_Adaptation (root)
    root.mainloop()

w = None
def create_Pocketsphinx_Acoustic_Model_Adaptation(root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    #rw.title('Pocketsphinx_Acoustic_Model_Adaptation')
    geom = "786x450"
    w.geometry(geom)
    w_win = Pocketsphinx_Acoustic_Model_Adaptation (w)
    return w_win

def destroy_Pocketsphinx_Acoustic_Model_Adaptation():
    global w
    w.destroy()
    w = None


class Pocketsphinx_Acoustic_Model_Adaptation:

    def __init__(self, master=None):
        self.racine = os.getcwd()
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#d9d9d9'
        self.font10 = "-family {DejaVu Sans} -size -10 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        self.font11 = "-family {DejaVu Sans Mono} -size -12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font14 = "-family {DejaVu Sans} -size 15 -weight normal -slant"  \
            " italic -underline 0 -overstrike 0"
        self.font30 = "-family {DejaVu Sans Mono} -size -30 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        master.configure(borderwidth="4")
        master.resizable(0,0)
        master.configure(relief="ridge")
        master.configure(background="#344c78")
        master.configure(cursor="icon")
        master.configure(height="350")
        master.configure(highlightbackground="#9eacbe")
        master.configure(highlightcolor="#98abc0")
        master.configure(width="600")
        self.hmm_value=StringVar()
        self.lm_value=StringVar()
        self.dic_value=StringVar()
        self.text_value=StringVar()
        self.dir_value=StringVar()
	self.THRESHOLD = 2000
	self.CHUNK = 1024
	self.FORMAT = pyaudio.paInt16
	self.CHANNELS = 1
	self.RATE = 16000
	self.SILENCE_DURATION = 40 # end recording after period of silence reaches this value
	self.WAIT_DURATION = 300 # end recording if no input before this value is reached
	self.SPEECH_DURATION = 300 # end recording if too much input
        self.notext = False
        self.automode = False
        self.miss_words = False
        self.Record = True
        self.lang = ""
        self.lang2 = ""
        self.mode = ""
        ################# change for next lign   ############################
        self.i = 168
        self.menubar = Menu(master,font=self.font10,bg=_bgcolor,fg=_fgcolor)
        master.configure(menu = self.menubar)
        """
        erase_files = self.racine+"/adapt*"
        print "directory cleaned !"
        for f in glob.glob(erase_files):
          os.remove(f)
        """

        # language selected at startup
        open_racines = open(self.racine+"/config/pama.config", "r")
        lignes = open_racines.readlines()
        open_racines.close()
        self.lang = str(lignes[4]).replace("\n","")
        if self.lang == "english":
          self.lang2 = "français"
          self.en = True
        else:
          self.lang2 = "english"
          self.en = False


        self.about = Menu(master,tearoff=0)
        self.menubar.add_cascade(menu=self.about,
                activebackground="#d9d9d9",
                activeforeground="#111111",
                background="#d9d9d9",
                font=self.font10,
                foreground="#000000",
                label="About")
        self.about.add_command(
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font=self.font10,
                foreground="#000000",
                label="Help",
                command=self.Help_PAMA)
        self.about.add_command(
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font=self.font10,
                foreground="#000000",
                label="Language",
                command=self.Language)
        self.about.add_command(
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font=self.font10,
                foreground="#000000",
                label="Accuracy",
                command=self.Accuracy)
        self.about.add_command(
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font=self.font10,
                foreground="#000000",
                label="Author",
                command=self.About_PAMA)
        self.exit = Menu(master,tearoff=0)
        self.menubar.add_cascade(menu=self.exit,
                activebackground="#d9d9d9",
                activeforeground="#111111",
                background="#d9d9d9",
                font=self.font10,
                foreground="#000000",
                label="Exit")
        self.exit.add_command(
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font=self.font10,
                foreground="#000000",
                label="Exit now",
		command=root.quit)

        self.pama_pic = Button(master)
        self.pama_pic.place(relx=0.59, rely=0.04, height=175, width=298)
        self.pama_pic.configure(activebackground="#d9d9d9")
        self._img2 = PhotoImage(file=self.racine+"/gif/pama.gif")
        self.pama_pic.configure(image=self._img2)
        self.dir = Message(master)
        self.dir.place(relx=0.04, rely=0.39, relheight=0.05, relwidth=0.08)
        self.dir.configure(text='''Dir : :''')
        self.dir.configure(width=70)

        self.dic = Message(master)
        self.dic.place(relx=0.04, rely=0.31, relheight=0.05, relwidth=0.08)
        self.dic.configure(text='''Dic :''')
        self.dic.configure(width=70)

        self.lm = Message(master)
        self.lm.place(relx=0.04, rely=0.23, relheight=0.05, relwidth=0.08)
        self.lm.configure(text='''Lm :''')
        self.lm.configure(width=70)

        self.hmm = Message(master)
        self.hmm.place(relx=0.04, rely=0.15, relheight=0.05, relwidth=0.08)
        self.hmm.configure(text='''Hmm:''')
        self.hmm.configure(width=70)

        self.lm_racine = Entry(root,textvariable=self.lm_value)
        self.lm_racine.place(relx=0.11, rely=0.23, relheight=0.05, relwidth=0.45)
        self.lm_racine.configure(background="white")
        self.lm_racine.configure(font=self.font11)
        self.lm_racine.configure(selectbackground="#c4c4c4")
        self.lm_racine.configure(width=356)

        self.dir_racine = Entry(root,textvariable=self.dir_value)
        self.dir_racine.place(relx=0.11, rely=0.39, relheight=0.05, relwidth=0.45)
        self.dir_racine.configure(background="white")
        self.dir_racine.configure(font=self.font11)
        self.dir_racine.configure(selectbackground="#c4c4c4")
        self.dir_racine.configure(width=358)

        self.dic_racine = Entry(root,textvariable=self.dic_value)
        self.dic_racine.place(relx=0.11, rely=0.31, relheight=0.05, relwidth=0.45)
        self.dic_racine.configure(background="white")
        self.dic_racine.configure(font=self.font11)
        self.dic_racine.configure(selectbackground="#c4c4c4")
        self.dic_racine.configure(width=358)

        self.hmm_racine = Entry(root,textvariable=self.hmm_value)
        self.hmm_racine.place(relx=0.11, rely=0.15, relheight=0.05, relwidth=0.45)
        self.hmm_racine.configure(background="white")
        self.hmm_racine.configure(font=self.font11)
        self.hmm_racine.configure(selectbackground="#c4c4c4")
        self.hmm_racine.configure(width=358)

        self.Message_racines = Message(master)
        self.Message_racines.place(relx=0.04, rely=0.04, relheight=0.08
                , relwidth=0.52)
        if self.en:
          self.Message_racines.configure(text='''Before use, you must enter each file and dir. racine !!!''')
        else:
          self.Message_racines.configure(text='''Entrez les liens vers vos fichiers avant de commencer''')
        self.Message_racines.configure(width=416)

        self.Entry1 = Entry(master,textvariable=self.text_value)
        self.Entry1.place(relx=0.04, rely=0.47, relheight=0.21, relwidth=0.93)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font=self.font10)
        self.Entry1.configure(justify=CENTER)
        self.Entry1.configure(width=740)

        self.Message1 = Message(master)
        self.Message1.place(relx=0.04, rely=0.71, relheight=0.25, relwidth=0.55)
        self.Message1.configure(font=font14)
        self.Message1.configure(justify=CENTER)
        if self.en:
          self.Message1.configure(text=self.mode+'''Sentence :\nVerify the text you enter :\nIncorrect words will not appear in dic''')
        else :
          self.Message1.configure(text=self.mode+'''Séquences :\nVérifiez l'orthographe de votre saisie !\nToute erreur ne sera pas corrigée''')
        self.Message1.configure(width=435)

        self.pama_racines()

# rec Button
        self.Button1 = Button(master, highlightthickness=0, borderwidth=0, command=self.REC)
        self.Button1.place(relx=0.7, rely=0.68, height=130, width=150)
        self.Button1.configure(background = "#344c78")

        self.recB = PhotoImage(file=self.racine+"/gif/rec.gif")
        self.Button1.configure(image=self.recB)
        self.Button1.configure(text='''Button''')
        self.Button1.configure(width=137)

        self.Message2 = Message(master)
        self.Message2.place(relx=0.04, rely=0.47, relheight=0.03, relwidth=0.23)
        if self.en :
          self.Message2.configure(text='''Hey, waiting choice''')
        else :
          self.Message2.configure(text='''J'attends votre choix''')
        self.Message2.configure(width=200)

        """
# stop_rec Button
        self.Button10 = Button(master, highlightthickness=0, borderwidth=0, command=self.REC)
        self.Button10.place(relx=0.78, rely=0.62, height=150, width=150)
        self.Button10.configure(background = "#344c78")

        self.recB10 = PhotoImage(file=self.racine+"/gif/stop.gif")
        self.Button10.configure(image=self.recB10)
        self.Button10.configure(text='''STOP''')
        self.Button10.configure(width=137)
        """

# info Button
        self.Button2 = Button(master, command=self.racine_infos)
        self.Button2.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.Button2.configure(activebackground="#d9d9d9")
        self.img = PhotoImage(file=self.racine+"/gif/intro.gif")
        self.imgfr = PhotoImage(file=self.racine+"/gif/introfr.gif")
        if self.en :
          self.Button2.configure(image=self.img)
        else :
          self.Button2.configure(image=self.imgfr)


# help screen popup
    def Help_PAMA(self):
        help = Tk()
        if self.en :
          help.title("elpimous@2015   --  Better help in readme.md")
        else:
          help.title("elpimous@2015   --  Plus d'aide dans readme.md")
        help.configure(background="#31404e")
        help.configure(highlightbackground="#31404e")
        help.configure(highlightcolor="black")
        geom = "611x300"
        help.geometry(geom)
        self.menubar = Menu(help)
        help.configure(menu = self.menubar)
        self.Message2 = Message(help)
        self.Message2.place(relx=0.23, rely=0.03, relheight=0.08, relwidth=0.53)
        self.Message2.configure(justify=CENTER)
        self.Message2.configure(relief=RIDGE)
        if self.en :
          self.Message2.configure(text='''Welcome in PAMA, read carefully this help before use.''')
        else:
          self.Message2.configure(text='''Bienvenue dans PAMA, veuillez consulter l'aide !''')
        self.Message2.configure(width=325)
        self.Labelframe1 = LabelFrame(help)
        self.Labelframe1.place(relx=0.02, rely=0.17, relheight=0.78
                , relwidth=0.96)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(text='''Help''')
        self.Labelframe1.configure(width=586)
        self.Message1 = Message(self.Labelframe1)
        self.Message1.place(relx=0.03, rely=0.04, relheight=0.14, relwidth=0.92)
        if self.en :
          self.Message1.configure(text='''Welcome to PAMA, a python, GUI program, to help you to adapt your existing language model''')
        else:
          self.Message1.configure(text='''Bienvenue dans PAMA, un programme qui vous aidera dans l'adaptation de votre modèle acoustique''')
        self.Message1.configure(width=535)
        self.Message1.configure(justify=CENTER)

        self.Message3 = Message(self.Labelframe1)
        self.Message3.place(relx=0.2, rely=0.26, relheight=0.04)
        if self.en :
          self.Message3.configure(text='''1°/ enter the 4 needed racines, otherwise it will not work,''')
        else:
          self.Message3.configure(text='''1°/ saisissez les 4 emplacements de vos fichiers,''')
        self.Message3.configure(width=355)
        self.Message3.configure(justify=CENTER)

        self.Message4 = Message(self.Labelframe1)
        self.Message4.place(relx=0.2, rely=0.36, relheight=0.14)
        if self.en :
          self.Message4.configure(text='''2°/ Type sentence, then click "REC" button,''')
        else:
          self.Message4.configure(text='''2°/ Entrez une séquence, puis cliquez sur "rec",''')
        self.Message4.configure(width=475)
        self.Message4.configure(justify=CENTER)

        self.Message5 = Message(self.Labelframe1)
        self.Message5.place(relx=0.2,rely=0.55, relheight=0.1)
        if self.en :
          self.Message5.configure(text='''3°/ follow instructions, until model is adapted''')
        else:
          self.Message5.configure(text='''3°/ suivez les instructions jusqu"à la validation de la compilation''')
        self.Message5.configure(width=485)
        self.Message5.configure(justify=CENTER)

        self.Message7 = Message(self.Labelframe1)
        self.Message7.place(relx=0.62, rely=0.85, relheight=0.1, relwidth=0.39)
        if self.en:
          self.Message7.configure(text='''See readme.md file before use.''')
        else:
          self.Message7.configure(text='''Pensez à consulter readme.md''')
        self.Message7.configure(width=225)


# language popup
    def Language(self):
      if self.en:
        language = tkMessageBox.askyesno("Select PAMA language...","Actual language is "+self.lang+"\nChange to "+self.lang2+" ?")
      else:
        language = tkMessageBox.askyesno("Selection de la langue...","Le programme est en "+self.lang+"\nChanger pour "+self.lang2+" ?")
      if language:
        open_racines = open(self.racine+"/config/pama.config", "w")
        open_racines.write(self.hmm+"\n")
        open_racines.write(self.lm+"\n")
        open_racines.write(self.dic+"\n")
        open_racines.write(self.dir+"\n")
        open_racines.write(self.lang2)
        open_racines.close()
        if self.en:
          language_popup = tkMessageBox.showinfo("", "Langue modifiée.\nLe programme va redémarrer.")
          root.destroy()
          vp_start_gui()
        else:
          language_popup = tkMessageBox.showinfo("", "Language changed.\nProgram will restart.")
          root.destroy()
          vp_start_gui()
      else:
        pass


# about popup
    def About_PAMA(self):
        self.style = Toplevel (root)
        self.style.deiconify()
        if self.en:
          self.style.title('About me...')
        else:
          self.style.title("A propos de l'auteur...")
        geom = "740x424"
        self.style.geometry(geom)
        self.menubar = Menu(self.style)
        self.style.configure(menu = self.menubar)
        self.TLabel = ttk.Label(self.style)
        self.TLabel.place(relx=0.0, rely=0.0, height=424, width=740)
        self.TLabel.configure(width=740)
        self._img3 = PhotoImage(file=self.racine+"/gif/about_me.gif")
        self._img3fr = PhotoImage(file=self.racine+"/gif/about_me.gif")
        if self.en:
          self.TLabel.configure(image=self._img3)
        else:
          self.TLabel.configure(image=self._img3fr)


    def REC(self):

        # change button pic
        #self.Button1 = Button(master, highlightthickness=0, borderwidth=0, command=self.stop_recording)
        self.recB = PhotoImage(file=self.racine+"/gif/stop.gif")
        self.Button1.configure(image=self.recB)
        root.update()
        self.text_popup()
        self.recording_voice()


    def stop_recording(self):
        print "stop rec pushed"
        self.recB11 = PhotoImage(file=self.racine+"/gif/rec.gif")
        self.Button10.configure(image=self.recB11)
        self.stop_needed = True


# recover existing racines, or let blank
    def pama_racines(self):
     if (os.path.exists(self.racine+"/config/pama.config")):
       open_racines = open(self.racine+"/config/pama.config", "r")
       lignes = open_racines.readlines()
       open_racines.close()
       self.hmm_racine.insert(0,str(lignes[0]).replace("\n",""))
       self.lm_racine.insert(0,str(lignes[1]).replace("\n",""))
       self.dic_racine.insert(0,str(lignes[2]).replace("\n",""))
       self.dir_racine.insert(0,str(lignes[3]).replace("\n",""))
       self.lang = str(lignes[4]).replace("\n","")
       root.update()
     else : pass


    def text_popup(self):
        self.read_text = self.text_value.get().encode('utf-8')
        if self.read_text == "":
          self.next_try()
          self.notext = True
        if not self.read_text == "":
          self.notext = False


    def recording_voice(self):
      if self.notext == False:
       # rec file and stop after 3sec silence,
       os.system("rec --encoding signed-integer --bits 16 --type wav --channels 1 --rate 16000 tempWavFile.wav silence -l 0% 1.0 2.5 1.0%")
       print "audio 1 ok"
       sleep(0.2)
       print "eeeeeeeeeeeeeeeeeeee"

       # remove silence in front of audiofile, and let 0.2s silence, and reverse file
       os.system("rec tempWavFile.wav tempWavFile2.wav silence 1 0.2 1% reverse")
       print "audio 2 ok"
       sleep(0.3)
       # remove silence in end of audiofile, and let 0.2s silence, and reverse file, for normal order
       os.system("rec tempWavFile2.wav "+self.racine+"/adapt"+str(self.i)+".wav silence 1 0.2 1% reverse")
       print "audio 3 ok"
       sleep(0.3)

       self.recB = PhotoImage(file=self.racine+"/gif/rec.gif")
       self.Button1.configure(image=self.recB)
       root.update()
       self.listen_audio()
       self.keep_audio()


    def listen_audio(self):
      os.system("aplay "+self.racine+"/adapt"+str(self.i)+".wav")


    def racine_infos(self):
      self.Button2.destroy()
      if self.en:
        racineinfos = tkMessageBox.showwarning("Pama racines -- verification", "Did you input the 4 racines correctly ? _________________________________________ \nHmm: your acoustic model location\nLm: idem\nDic: idem\nDir: PAMA location on disk\n_________________________________________\n\nIf not, enter them after next popup screen !!!")
      else:
        racineinfos = tkMessageBox.showwarning("Vérification des liens Pama", "Avez-vous correctement entré les liens du modèle acoustique ? _________________________________________ \nHmm: votre modèle acoustique,\nLm: idem,\nDic: idem,\nDir: Emplacement du rep. PAMA.\n_________________________________________\n\nSinon, remplissez-les après le popup suivant.")
      if racineinfos:
        self.pama_mode()
      else:
        self.pama_mode()

    def pama_mode(self):
      if self.en:
        mode_Sentence = tkMessageBox.askyesno("Choose learning mode", "Would you try automatic process ? ")
      else:
        mode_Sentence = tkMessageBox.askyesno("choix du mode d'apprentissage", "Voulez-vous démarrer le mode automatique ? (voir readme.md)")
      if mode_Sentence:
        self.automode = True
        if self.en:
          self.Message2.configure(text='''Automatic sentences mode :''')
        else:
          self.Message2.configure(text='''Mode automatique :''')
        self.record_info()
        root.update()
        self.auto_mode()
      else:
        self.automode = False
        if self.en:
          self.Message2.configure(text='''Enter here your sentence :''')
        else:
          self.Message2.configure(text='''Entrez votre phrase :''')
        self.record_info()
        root.update()
        pass

    def auto_mode(self):
      if self.automode == True:
        sentence = open(self.racine+"/config/sentences.list", "r")
        self.sentences = sentence.read()
        self.Sentences = self.sentences.split("\n")
        self.sentence = (choice(self.Sentences))
        if self.sentence == "\n":
            self.auto_mode()
        self.Entry1.insert(0,self.sentence)
        root.update()
        sentence.close()
      else:
        pass

# recover errors from terminal, write missing words in txt file
    def read_words(self):
      open_read = self.ph_err      # read terminal and look for missing words
      open_newwords = open(self.racine+"/adapt.newwords", "w")      # open txt to save missing words if exists
      print "============================================================="
      print self.ph_err
      print "============================================================="
      print open_read
      m = re.search("Unable to lookup word '(.+?)' in the dictionary", open_read) # localize string between 2 other strings
      if m:
        self.miss_words = True
        found = m.group(1)
        open_newwords.write(found+"\n")
      open_newwords.close()


# insert missing words in popup alert
    def missing_words(self):
      self.read_words()
      miss = open(self.racine+"/adapt.newwords", "r")      # open txt to read missing words if exists
      self.Errors = miss.read()
      miss.close()


# recording information popup 
    def record_info(self):
     self.hmm = self.hmm_value.get().encode('utf-8')
     self.lm = self.lm_value.get().encode('utf-8')
     self.dic = self.dic_value.get().encode('utf-8')
     self.dir = self.dir_value.get().encode('utf-8')
     open_racines = open(self.racine+"/config/pama.config", "w")
     open_racines.write(self.hmm+"\n")
     open_racines.write(self.lm+"\n")
     open_racines.write(self.dic+"\n")
     open_racines.write(self.dir+"\n")
     open_racines.write(self.lang)
     open_racines.close()
     if self.en:
       nb = tkMessageBox.showwarning("Recording process ","To record sample, follow this help\n_______________________________________\n\n1° Click 'rec',\nRecording will stop automatically.\n_______________________________________\n\nP.S : now, your racines input are saved. If unsatisfied, restart program and make changes.")
     else:
       nb = tkMessageBox.showwarning("Enregistrement ","Pour enregistrer, suivez l'aide :\n_______________________________________\n\n1° Cliquez sur le micro,\n2° Parlez...\n3° L'enregistrement stoppera automatiquement.\n_______________________________________\n\nP.S : maintenant, vos liens sont sauvegardés. Si vous voulez les modifier, redémarrez le programme.")

# keep recording popup
    def keep_audio(self):
      if self.en:
        keep = tkMessageBox.askyesno("Continue to next sentence, or try again", "Keep the audio record ?")
      else:
        keep = tkMessageBox.askyesno("Satisfait de l'enregistrement ?", "Voulez-vous garder cet enregistrement ?")
      if keep:
        self.Entry1.delete(0, 'end')
        self.text()
        self.next_sentence()
      else:
        pass

# continue recording or adapt popup
    def next_sentence(self):
      if self.en:
        nSentence = tkMessageBox.askyesno("Choose between Continue or Adapt", "Continue to next sentence ? ")
      else:
        nSentence = tkMessageBox.askyesno("continuer ou adapter ?", "voulez-vous encore enregistrer ? ")
      if nSentence:
        self.i+=1
        self.auto_mode()
      else:
        self.process()

# empty sentence / can't record nothing !!!
    def next_try(self):
      if self.en:
        next = tkMessageBox.showwarning("Empty sentence !!!", " You can't 'REC' without any text.   ")
      else:
        next = tkMessageBox.showwarning("Pas de phrase !!!", " Vous ne pouvez pas enregistrer sans texte.   ")
      self.notext = True
      self.recB = PhotoImage(file=self.racine+"/gif/rec.gif")
      self.Button1.configure(image=self.recB)
      root.update()


# backup text, and save informations in 2 differents text files, NEEDED FOR CMUSPHINX ADAPT PROCESS
    def text(self):

      a = self.read_text.lower().replace("-"," ").replace(",","").replace(".","").replace("...","").replace("?","").replace("!","").replace(":","").replace(";","").replace("(","").replace(")","").replace("'"," ").replace("’"," ").replace('"',"")

      open_adapt = open(self.racine+"/adapt.transcription", "a")
      open_adapt
      open_adapt.write("<s> ")
      open_adapt.write(a)
      open_adapt.write(" </s> (adapt"+str(self.i)+")\n")
      open_adapt.close()

      b= "adapt"+str(self.i)+"\n"
      open_fileids = open(self.racine+"/adapt.fileids", "a")
      open_fileids
      open_fileids.write(b)
      open_fileids.close()


############# recover terminal infos, needed for compilation errors finding ###########


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


########################################################################################
##################################  PROCESSING  ########################################
########################################################################################


    def process(self):
        print "\n\n\n ********************************************"
        print " *    GENERATING ACOUSTIC FEATURE FILES     *"
        print " *     on génère lee fichiers MFCC:     *"
        print " ********************************************\n\n\n"
        os.system ("cd "+self.racine+" && sphinx_fe -argfile "+self.hmm+"/feat.params \
        -samprate 16000 -c "+self.racine+"/adapt.fileids \
       -di . -do . -ei wav -eo mfc -mswav yes")


        print "\n\n\n ********************************************"
        print " *     CONVERTING SENDUP AND MDEF FILES     *"
        print " *     on converti le sendup et le mdef :   *"
        print " ********************************************\n\n\n"
        os.system ("pocketsphinx_mdef_convert -text "+self.hmm+"/mdef "+self.hmm+"/mdef.txt")


        print "\n\n\n ********************************************"
        print " *     ACCUMULATION OBSERVATION COUNTS      *"
        print " *     création des profiles :              *"
        print " ********************************************\n\n\n"
        self.runCmdOutput("cd "+self.racine+" && ./bw  -hmmdir "+self.hmm+"  -moddeffn "+self.hmm+"/mdef.txt  -ts2cbfn .ptm.  -feat 1s_c_d_dd  -svspec 0-12/13-25/26-38  -cmn current  -agc none  -dictfn "+self.dic+"  -ctlfn "+self.racine+"/adapt.fileids  -lsnfn "+self.racine+"/adapt.transcription  -accumdir .")


        print "\n *********************************************************"
        print " *                  READ CARFULLY LOG !!!                *"
        print " *     If you see unknown words, add them on DIC file    *"
        print " *  Lire attentivement le log, et s'assurer qu'il n'y a  *"
        print " *  de mots inconnus. Sinon, les ajouter au fichier dic  *"
        print " *********************************************************\n"
        self.missing_words()
        if self.miss_words == False:
          errors = tkMessageBox.showinfo("Missing word(s) in dictionary"," All words are in your dictionary,\n you can continue.")
          print "\n Ok, next process..."
          print "\n\n\n *********************************************"
          print " *     CREATING TRANSFORMATION WITH MLLR     *"
          print " *     transformation avec le MLLR :         *"
          print " *********************************************\n\n\n"

          os.system ("cd "+self.racine+" && ./mllr_solve     -meanfn "+self.hmm+"/means     -varfn "+self.hmm+"/variances     -outmllrfn mllr_matrix -accumdir .")


          print "\n\n\n ********************************************"
          print " *            INSERTING MATRIX IN MODEL           *"
          print " *   reconstruction du modèle avec les matrix :   *"
          print " ********************************************\n\n\n"
          os.system ("cd "+self.racine+" && ./mllr_transform -inmeanfn "+self.hmm+"/means -outmeanfn "+self.hmm+"/new_means -mllrmat "+self.racine+"/mllr_matrix")


          print "\n\n\n ********************************************"
          print " *        REPLACE MEANS WITH NEW ONE        *"
          print " *  remplacement du means par le nouveau    *"
          print " *     et efface l' ancien fichier means    *"
          print " ********************************************\n\n\n"
          os.system ("cp "+self.hmm+"/new_means"+self.hmm+"/means")
          os.system ("rm "+self.hmm+"/new_means")


          print "\n\n\n ********************************************"
          print " *  AGAIN, ACCUMULATION OBSERVATION COUNTS  *"
          print " *       2 ème création des profiles        *"
          print " *         avec le means modifié :          *"
          print " ********************************************\n\n\n"
          self.runCmdOutput("cd "+self.racine+" && ./bw  -hmmdir "+self.hmm+"  -moddeffn "+self.hmm+"/mdef.txt  -ts2cbfn .ptm.  -feat 1s_c_d_dd  -svspec 0-12/13-25/26-38  -cmn current  -agc none  -dictfn "+self.dic+"  -ctlfn "+self.racine+"/adapt.fileids  -lsnfn "+self.racine+"/adapt.transcription  -accumdir .")


          print "\n\n\n ***********************************************"
          print " *  UPDATING THE ACOUSTIC MODEL WITH MAP UTIL  *"
          print " *      mise a jour du modèle avec le MAP      *"
          print " *              sans les variances             *"
          print " ***********************************************\n\n\n"
          os.system("cd "+self.racine)
          os.system("./map_adapt \
    -moddeffn "+self.hmm+"/mdef.txt \
    -ts2cbfn .ptm. \
    -meanfn "+self.hmm+"/means \
    -varfn "+self.hmm+"/variances \
    -mixwfn "+self.hmm+"/mixture_weights \
    -tmatfn "+self.hmm+"/transition_matrices \
    -accumdir . \
    -mapmeanfn "+self.hmm+"/means \
    -mapmixwfn "+self.hmm+"/mixture_weights \
    -maptmatfn "+self.hmm+"/transition_matrices")


          """
          print "\n\n\n ******************************************"
          print " *  RECREATING THE ADAPTED SENDUP FILE    *"
          print " *   RECONSTRUCTION DU FICHIER SENDUP :   *"
          print " ******************************************\n\n\n"
          os.system ("cd "+self.racine+" && ./mk_s2sendump \
    -pocketsphinx yes \
    -moddeffn "+self.hmm+"/mdef.txt \
    -mixwfn "+self.hmm+"/mixture_weights \
    -sendumpfn "+self.hmm+"/sendump")

          print "\n\n\n ****************************************"
          print " *     CONVERTING  MDEF FILE to bin     *"
          print " *     on reconverti le mdef en bin:    *"
          print " ****************************************\n\n\n"
          os.system ("pocketsphinx_mdef_convert -bin "+self.hmm+"/mdef.txt "+self.hmm+"/mdef")
          """


          print "\n\n\n ************************************************************************"
          print "   Congratulations! You now have an adapted acoustic model!\n  You can delete the files cmusphinx-fr-ptm-5.2-adapt/mixture_weights\n  and cmusphinx-fr-ptm-5.2-adapt/mdef.txt\n "
          print "         Bravo, fini, tu as adapté ton modèle acoustique !!! "
          print " ************************************************************************\n\n\n"

          self.congratulations()

        else :
          if self.en:
            errors = tkMessageBox.askyesno("Missing word(s) in dictionary, please add it in dic file !","  Here are missing words in dic :\n\nopen *.dic, add words & phonems\n_________________________________________\n\nWhen finished, click OK to compile.\n_________________________________________\n\n Words to add :\n\n"+str(self.Errors)+"\n_________________________________________\n\n Or click no to exit program")
            if errors:
              self.miss_words = False
              self.process()
            else:
              root.destroy()
          else:
            errors = tkMessageBox.askyesno("Erreurs lors de la compilation ","  Les mots suivants sont absents du dictionnaire :\n\nOuvrez votre dictionnaire et ajoutez les mots et leurs phonèmes\n_________________________________________\n\nQuand vous avez fini, cliquez sur ok\n_________________________________________\n\n Mot(s) a ajouter :\n\n"+str(self.Errors)+"\n_________________________________________\n\n Ou cliquez sur no pour quitter le programme")
            if errors:
              self.miss_words = False
              self.process()
            else:
              root.destroy()
               
######################################################################################
##################################  ACCURACY  ########################################
######################################################################################

# Accuracy popup
    def Accuracy(self):
        self.accu = Toplevel (root)
        self.accu.deiconify()
        if self.en:
          self.accu.title('Accuracy test.')
        else:
          self.accu.title("Test du taux de reconnaissance.")
        geom = "767x430"
        self.accu.geometry(geom)
        self.menubar2 = Menu(self.accu)
        self.accu.configure(menu = self.menubar2)
        self.TLabel = ttk.Label(self.accu)
        self.TLabel.place(relx=0.0, rely=0.0, height=430, width=767)
        self.TLabel.configure(width=740)
        self.accubg = PhotoImage(file=self.racine+"/gif/accuracy_bg.gif")
        self.TLabel.configure(image=self.accubg)

        self.previous = Entry(self.accu)
        content_variable = open(self.racine+"/test_adapt_model/do_not_erase", "r")
        file_lines = content_variable.readlines() 
        content_variable.close () 
        last_line = file_lines [ len ( file_lines ) -1].replace("\n","")
        self.previous.place(relx=0.04, rely=0.8, relheight=0.14, relwidth=0.31)
        self.previous.configure(background="white")
        self.previous.configure(font=self.font30)
        self.previous.configure(justify=RIGHT)
        self.previous.configure(selectbackground="#c4c4c4")
        self.previous.configure(width=256)
        self.prev = Message(self.previous)
        self.prev.place(height=20, width=75)
        self.prev.configure(justify=CENTER)
        self.prev.configure(font=self.font11)
        self.prev.configure(text="Previous :")
        self.prev.configure(width=325)
        self.previous.insert(0,last_line+" % ")
        self.previous.update()

        # a recuperer dans le log !!!
        self.actual = Entry(self.accu)
        self.actual.place(relx=0.04, rely=0.6, relheight=0.14, relwidth=0.31)
        self.actual.configure(background="white")
        self.actual.configure(font=self.font30)
        self.actual.configure(justify=RIGHT)
        self.actual.configure(selectbackground="#c4c4c4")
        self.actual.configure(width=256)
        self.actu = Message(self.actual)
        self.actu.place(height=20, width=75)
        self.actu.configure(justify=LEFT)
        self.actu.configure(font=self.font11)
        self.actu.configure(text="  Actual :  ")
        self.actu.configure(width=325)
        self.accu.update()

        # a recuperer dans le log !!!
        self.newSentenceDecoding = "1"
        self.log = Entry(self.accu)
        self.log.place(relx=0.39, rely=0.16)
        self.log.place(height=70, width=457)
        self.log.configure(background="white")
        self.log.configure(font=self.font11)
        self.log.configure(justify=CENTER)
        self.log.configure(selectbackground="#c4c4c4")
        self.log_mess = Message(self.log)
        self.log_mess.place(height=20, width=80)
        self.log_mess.configure(justify=CENTER)
        self.log_mess.configure(font=self.font11)
        self.log_mess.configure(text="Log :")
        if self.en:
          self.log.insert(0,"Waiting for you...")
        else:
          self.log.insert(0,"En attente...")
        self.accu.update()

        self.accuracy_bt = Button(self.accu, command = self.err_recovery)
        self.accuracy_bt.place(relx=0.39, rely=0.38)
        self.accuracy_bt.configure(activebackground="#d9d9d9")
        self.graph_btn = PhotoImage(file=self.racine+"/gif/accuracy_button.gif")
        self.graph_btnfr = PhotoImage(file=self.racine+"/gif/accuracy_buttonfr.gif")
        if self.en:
          self.accuracy_bt.configure(image=self.graph_btn)
        else :
          self.accuracy_bt.configure(image=self.graph_btnfr)
        self.accu.update()


# graph creation
    def PercentsGraph(self):
      fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
      fig = plt.figure(1)
      fig.set_figheight(2.5)
      fig.set_figwidth(4.5)
      rect = fig.patch
      plot(self.y,marker='o',markerfacecolor = 'red')

      xlabel('Tests')
      ylabel('')
      title('Accuracy percentage graph.')
      grid(True)
      plt.savefig(self.racine+"/gif/graph.png")
      #plt.close()


# Accuracy process
    def err_recovery(self):
      self.graph_btn2 = PhotoImage(file=self.racine+"/gif/accuracy_working.gif")
      self.accuracy_bt.configure(image=self.graph_btn2)
      self.accu.update()
      self.log.delete(0, 'end')
      if self.en:
        self.log.insert(0,"Please wait : decodind sentence(s)...")
      else:
        self.log.insert(0,"Veuillez patienter, le décodage est en cours...")
      self.accu.update()
      self.runCmdOutput("pocketsphinx_batch  -adcin yes  -cepdir "+self.racine+"/test_adapt_model/wav  -cepext .wav  -ctl "+self.racine+"/test_adapt_model/adaptation-test.fileids  -lm /home/neo/Documents/PAMA/model/french3g62K.lm.bin -dict /home/neo/Documents/PAMA/model/frenchWords62K.dic -hmm /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt -hyp "+self.racine+"/test_adapt_model/adapation-test.hyp ")
      print self.ph_out
      print self.ph_err
      self.runCmdOutput("cd "+self.racine+"&& ./word_align.pl "+self.racine+"/test_adapt_model/adaptation-test.transcription "+self.racine+"/test_adapt_model/adapation-test.hyp")
      print self.ph_out
      print self.ph_err
      accuracity = self.ph_out
      m = re.search("TOTAL Percent correct(.+?)\n", accuracity) # localize string between 2 other strings
      if m:
        found = m.group(1)
        percent = re.search("Accuracy = (.+?)%", found)
        percent2 = percent.group(1)
        self.new_percentage = int(float(percent2))
        openfile = open(self.racine+"/test_adapt_model/do_not_erase", "a")
        openfile.write(str(self.new_percentage)+"\n")
        openfile.close()
      self.actual.delete(0, 'end')
      self.actual.insert(0,str(self.new_percentage)+" % ")

      #gValues = open(self.racine+"/test_adapt_model/do_not_erase", "r")
      #gvalue2 = gValues.read()
      self.y = []
      for line in open(self.racine+"/test_adapt_model/do_not_erase", "r"):
        if line.strip():           # line contains eol character(s)
          n = (line)
          self.y.append(n)

      self.PercentsGraph() # create graph

      self.graph_btn3 = PhotoImage(file=self.racine+"/gif/graph.png")
      self.accuracy_bt.configure(image=self.graph_btn3)
      self.log.delete(0, 'end')
      if self.en:
        self.log.insert(0,"Decodinf finished.")
      else:
        self.log.insert(0,"Analyse terminée.")
      self.accu.update()


######################################################################################

    def congratulations(self):
      if self.en:
        result = tkMessageBox.showinfo("elpimous@2015","Congratulations, you have adapted your model")
      else:
        result = tkMessageBox.showinfo("elpimous@2015","Bravo, vous venez d'adapter votre modèle")
      root.destroy()



if __name__ == '__main__':
  vp_start_gui()

