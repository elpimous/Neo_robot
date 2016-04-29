#!/usr/bin/env python
# -*- coding: utf-8 -*-

#**************************************************************
#
#   A python program to aid everyone adapt acoustic model
#   -----------------------------------------------------
#
#   - adapt your own voice,
#   - add new words
#
#**************************************************************

import sys, os, re
import rospy
import subprocess
import glob
from random import choice


class adapt():

  def __init__(self):

    self.i = 0
    self.racine = os.getcwd()
    # put your direct links here, to avoid each manual input at each startup, if done, you can directly press '2' at startup !
    # placez ici vos liens vers votre modèle acoustique et le rép. d'installation, ainsi vous pourrez presser directement '2' au démarrage !
    self.lm = self.racine+"/model/fr.lm.bin"
    self.dic = self.racine+"/model/fr.dict"
    self.hmm = self.racine+"/model/fr_ptm_5.2"
    self.link = self.racine




  def Link(self):

    os.system('clear')
    print "\n\n\n HERE IS A SIMPLE TOOL FOR POCKETSPHINX ADAPTATION"
    print " I made it for personal use, so use it at your own risk"
    print " ------------------------------------------------------"
    print " 1°/ You'll have to setup program,"
    print " 2°/ you'll have to write sentences, and record audio."
    print " READ CARFULLY and follow instructions to compile model"
    print " backup actual model, before use"
    print " ------------------------------------------------------\n\n\n\n"
    print " **************************************"
    print " please enter your link to pocket_adapt : "
    print " entrez le lien vers pocket_adapt : "
    print "      ....../pocket_adapt"
    print " **************************************"
    self.link =  raw_input(">> ")
    answer = raw_input (" your pocket_adapt repertory is here  : << "+ self.link + " >> correct ? y / n.  \n>> ")
    if answer == str("y"):
      self.add_lm()
    elif answer == str("n"):
      print " Ok, try again !  \n"
      self.Link()


    
  def add_lm(self):
    os.system('clear')
    print "\n ***************************************************"
    print " please enter your 'LM' or 'LM.BIN' model location : "
    print " entrez le lien vers votre 'LM' or 'LM.BIN' : "
    print " ***************************************************"
    self.lm =  raw_input(">> ")
    answer = raw_input (" your lm location is : "+ self.lm + ", correct ? y / n.  \n>> ")
    if answer == str("y"):
      self.add_dic()
    elif answer == str("n"):
      print " Ok, try again !  \n"
      self.add_lm()



  def add_dic(self):
    os.system('clear')
    print "\n ***************************************"
    print " Please, enter your 'DIC' model location : "
    print " entrez le lien vers votre 'DIC' : "
    print " ***************************************"
    self.dic =  raw_input(">> ")
    answer = raw_input (" your dic location is : "+ self.dic + ", correct ? y / n.  \n>> ")
    if answer == str("y"):
      self.add_hmm()
    elif answer == str("n"):
      print " Ok, try again !  \n"
      self.add_dic()



  def add_hmm(self):
    os.system('clear')
    print "\n ***************************************"
    print " Please, enter your 'HMM' model location : "
    print " entrez le lien vers votre 'HMM' : "
    print " ***************************************"
    self.hmm =  raw_input(">> ")
    answer = raw_input (" your dic location is : "+ self.hmm + ", correct ? y / n.  \n>> ")
    if answer == str("y"):
      self.add_text_files()
    elif answer == str("n"):
      print " Ok, try again !  \n"
      self.add_hmm()


  def menu(self):
    os.system('clear')
    print "\n\n\n °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
    print " °   Pocket_adapt       °  special menu  °"
    print " °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
    print " °                                       °"
    print " °  start normally               : >> 1  °"
    print " °  start directly sentences     : >> 2  °"
    print " °  start automatic sentences    : >> 3  °"
    print " °  start directly acoustic gen. : >> 4  °"
    print " °                                       °"
    print " °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n"
    answer = raw_input ("  Enter your choice and press Enter :\n  >>  ")
    if answer == "1":
      self.Link()
    if answer == "2":
      self.add_text_files()
    if answer == "3":
      self.add_existing_learning_sentences()
    if answer == "4":
      self.gen_acoustic()

  def add_text_files(self): # add sentences : text and audio
    os.system('clear')
    print "\n\n\n ******************************************************"
    print " *             ACOUSTIC MODEL INITIALIZED             *"
    print " *      now type sentences, and record wav files      *"
    print " *   NOTE THAT IT WILL ERASE SENTENCES DONE BEFORE !  *"
    print " *        maintenant les phrases puis les wav         *"
    print " * ATTENTION, CELA EFFACERA LES SEQUENCES DEJA CREEES *"
    print " ******************************************************\n\n\n"

    answer = raw_input (" IF YOU CONTINUE, AUDIO AND TEXT FILES WILL BE ERASED ! But if you already created model and had sucess, you can press 'y'\n SI VOUS CONTINUEZ, TOUS VOS FICHIERS AUDOI ET TEXTE SERONT EFFACES ! Cependant, si votre modèle a été préalablement construit, vous pouvez presser 'y'\n CONTINUE : y /n\n\n >> ")
    if answer == "y" :
      # erase existing, old recorded files
      erase_files = self.link+"adapt*"
      for f in glob.glob(erase_files):
        os.remove(f)
      answer = raw_input ("\n Add a new sentence : type a phrasis, without points, comma, etc,  and press enter when finished.\n Ecrivez une phrase sans ponctuation, ni guillemets, puis pressez enter\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n>> ")
      self.i +=1

      # adapt.transcription
      a= "<s> "+answer+" </s> (adapt"+str(self.i)+")"
      open_adapt = open(self.link+"/adapt.transcription", "w")
      open_adapt
      open_adapt.write(a)
      open_adapt.close()

      # adapt.fileids
      b= "adapt"+str(self.i)
      open_fileids = open(self.link+"/adapt.fileids", "w")
      open_fileids
      open_fileids.write(b)
      open_fileids.close()

      # wav files
      self.rec = "rec --encoding signed-integer --bits 16 --channels 1 --rate 16000 "+self.link+"/adapt"+str(self.i)+".wav silence 1 0.1 1% 1 1.5 1%"
      answer = raw_input ("\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n When ready, press 'p' and speak the sentence you just wrote\n Do silence when done\n\n >> ")
      if answer == "p":
        while 1 :
          subprocess.Popen(self.rec, shell=True, stdout=subprocess.PIPE).communicate()
          os.system("aplay "+self.link+"/adapt"+str(self.i)+".wav")
          answer = raw_input ("\n WOULD YOU KEEP THIS RECORDING ? / VOULEZ-VOUS GARDER CET ENREGISTREMENT ? y / n \n\n >> ")
          if answer == "y":
            os.system('clear')
            break
          elif answer == "n":
            print ("\n Ok, record a new one  /  Ok, enregistrez a nouveau \n")
            continue

      answer = raw_input ("\n\n Do you want to create another sentence ? y / n \n\n>> ")
      while answer == "y":
        os.system('clear')
        answer = raw_input ("\n\n Ok, add a new sentence and press enter when finished.\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n>> ")
        self.i +=1
        a= "\n<s> "+answer+" </s> (adapt"+str(self.i)+")"
        open_adapt = open(self.link+"/adapt.transcription", "a")
        open_adapt
        open_adapt.write(a)
        open_adapt.close()

        b= "\nadapt"+str(self.i)
        open_fileids = open(self.link+"/adapt.fileids", "a")
        open_fileids
        open_fileids.write(b)
        open_fileids.close()

        self.rec = "rec --encoding signed-integer --bits 16 --channels 1 --rate 16000 "+self.link+"/adapt"+str(self.i)+".wav silence 1 0.1 1% 1 1.5 1%"
        answer = raw_input ("\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n When ready, press 'p' and speak the sentence you just wrote\n Do silence when done\n\n>> ")
        if answer == "p":
          while 1 :
            subprocess.Popen(self.rec, shell=True, stdout=subprocess.PIPE).communicate()
            os.system("aplay "+self.link+"/adapt"+str(self.i)+".wav")
            answer = raw_input ("\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n WOULD YOU KEEP THIS RECORDING ? / VOULEZ-VOUS GARDER CET ENREGISTREMENT ? y / n \n\n>> ")
            if answer == "y":
              os.system('clear')
              break
            elif answer == "n":
              print ("\n Ok, record a new one  /  Ok, enregistrez a nouveau \n")
              continue
          answer = raw_input ("\n\n Do you want to create another sentence ? y / n \n\n>> ")
          os.system('clear')
      else :
        self.gen_acoustic()
    else :
        print "\n\n  ###  OK BYE  ###"


  def add_existing_learning_sentences(self):
    self.sentences = ["dimanche dernier il s est passé une drôle d histoire à marseille","un adolescent de dix sept ans a essayé de voler une voiture dans le cinquième arrondissement de marseille","le jeune homme a réussi à ouvrir la portière d une voiture il est entré et a refermé la portière","manque de chance le système de sécurité de la voiture a fonctionné et le jeune voleur s est retrouvé pris au piège à l intérieur du véhicule","impossible de sortir  ce jour là la chance n était vraiment pas de son côté car son téléphone portable lui permettait d accéder seulement aux appels d urgence","après avoir bien réfléchi il s est décidé à appeler la police très heureuse de pouvoir venir l aider et bien sûr  de lui faire visiter le commissariat de marseille","noël approche les français comme la plupart des européens se préparent à cette fête familiale la plus importante de l année","en france la plupart des gens fêtent noël sauf évidemment les pratiquants des autres religions vous devez savoir que le père noël qui est aujourd hui indissociable de noël est arrivé en france assez tard","on peut même dire qu il est devenu de plus en plus populaire quand les français ont commencé à déserter les églises","je vais vous raconter une petite anecdote qui s est passée dans les années cinquante en france","c est après la seconde guerre mondiale que le père noël est devenu le père noël des petits français","il y avait déjà saint nicolas mais les petits français n avaient pas tous la même image du père noël","c est un homme âgé avec une barbe et un manteau rouge et blanc","a cette époque tout ce qui venait des états unis était très populaire et la manière américaine de fêter noël a eu très vite beaucoup de succès","les prêtres de cette époque ont tout fait pour faire disparaître le père noël","on a pendu le père noël et on l a brûlé devant la cathédrale","les enfants et les gens autour ont été très surpris","les prêtres de l époque ont fait cela parce qu ils étaient très inquiet car le père noël prenait de plus en plus de place dans le coeur des enfants","et on le voyait apparaître dans les écoles publiques alors que les symboles catholiques de noël comme la crèche étaient absent des écoles","ce qui est intéressant dans cette anecdote c est que cet évènement a été repris par france soir et toute la presse nationale","cette histoire finalement se termine bien car le soir même à dix huit heures précise le père noël est ressuscité et les enfants de dijon ont été invités devant l hôtel de ville pour le voir et l écouter","cette petite anecdote montre bien que la manière de fêter noël et les symboles d aujourd hui ne sont pas si anciens que ça"]

    os.system('clear')
    print "\n\n\n ******************************************************"
    print " *             ACOUSTIC MODEL INITIALIZED             *"
    print " *      now read sentences and  record wav files      *"
    print " *   NOTE THAT IT WILL ERASE SENTENCES DONE BEFORE !  *"
    print " *        Lisez à voix haute les phrases suivantes    *"
    print " * ATTENTION, CELA EFFACERA LES SEQUENCES DEJA CREEES *"
    print " ******************************************************\n\n\n"

    answer = raw_input (" IF YOU CONTINUE, AUDIO AND TEXT FILES WILL BE ERASED ! But if you already created model and had sucess, you can press 'y'\n SI VOUS CONTINUEZ, TOUS VOS FICHIERS AUDOI ET TEXTE SERONT EFFACES ! Cependant, si votre modèle a été préalablement construit, vous pouvez presser 'y'\n CONTINUE : y /n\n\n >> ")
    if answer == "y" :
      # erase existing, old recorded files
      erase_files = self.link+"adapt*"
      for f in glob.glob(erase_files):
        os.remove(f)
      self.sentence = (choice(self.sentences))
      print ("\n  When ready, speak this sentence / Quand vous êtes prêt, lisez a haute voix la phrase suivante :\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n   "+self.sentence+"\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n")
      self.i +=1

      # adapt.transcription
      a= "<s> "+self.sentence+" </s> (adapt"+str(self.i)+")"
      open_adapt = open(self.link+"/adapt.transcription", "w")
      open_adapt
      open_adapt.write(a)
      open_adapt.close()

      # adapt.fileids
      b= "adapt"+str(self.i)
      open_fileids = open(self.link+"/adapt.fileids", "w")
      open_fileids
      open_fileids.write(b)
      open_fileids.close()

      # wav files
      self.rec = "rec --encoding signed-integer --bits 16 --channels 1 --rate 16000 "+self.link+"/adapt"+str(self.i)+".wav silence 1 0.1 1% 1 1.5 1%"
      answer = raw_input ("\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n When ready, press 'p' and speak the sentence you just wrote\n Do silence when done\n\n >> ")
      if answer == "p":
        while 1 :
          subprocess.Popen(self.rec, shell=True, stdout=subprocess.PIPE).communicate()
          os.system("aplay "+self.link+"/adapt"+str(self.i)+".wav")
          answer = raw_input ("\n WOULD YOU KEEP THIS RECORDING ? / VOULEZ-VOUS GARDER CET ENREGISTREMENT ? y / n \n\n >> ")
          if answer == "y":
            os.system('clear')
            break
          elif answer == "n":
            print ("\n Ok, record a new one  /  Ok, enregistrez a nouveau \n")
            continue

      answer = raw_input ("\n\n Do you want to create another sentence ? y / n \n\n>> ")
      while answer == "y":
        os.system('clear')
        self.sentence = (choice(self.sentences))
        print ("\n  When ready, speak this sentence / Quand vous êtes prêt, lisez a haute voix la phrase suivante :\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n   "+self.sentence+"\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n")
        self.i +=1
        a= "\n<s> "+self.sentence+" </s> (adapt"+str(self.i)+")"
        open_adapt = open(self.link+"/adapt.transcription", "a")
        open_adapt
        open_adapt.write(a)
        open_adapt.close()

        b= "\nadapt"+str(self.i)
        open_fileids = open(self.link+"/adapt.fileids", "a")
        open_fileids
        open_fileids.write(b)
        open_fileids.close()

        self.rec = "rec --encoding signed-integer --bits 16 --channels 1 --rate 16000 "+self.link+"/adapt"+str(self.i)+".wav silence 1 0.1 1% 1 1.5 1%"
        answer = raw_input ("\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n When ready, press 'p' and speak the sentence you just wrote\n Do silence when done\n\n>> ")
        if answer == "p":
          while 1 :
            subprocess.Popen(self.rec, shell=True, stdout=subprocess.PIPE).communicate()
            os.system("aplay "+self.link+"/adapt"+str(self.i)+".wav")
            answer = raw_input ("\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n WOULD YOU KEEP THIS RECORDING ? / VOULEZ-VOUS GARDER CET ENREGISTREMENT ? y / n \n\n>> ")
            if answer == "y":
              os.system('clear')
              break
            elif answer == "n":
              print ("\n Ok, record a new one  /  Ok, enregistrez a nouveau \n")
              continue
          answer = raw_input ("\n\n Do you want to create another sentence ? y / n \n\n>> ")
          os.system('clear')
      else :
        self.gen_acoustic()
    else :
        print "\n\n  ###  OK BYE  ###"

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
      else :
        self.miss_words = False 
      open_newwords.close()



# insert missing words in popup alert
  def missing_words(self):
      self.read_words()
      miss = open(self.racine+"/adapt.newwords", "r")      # open txt to read missing words if exists
      self.Errors = miss.read()
      if self.Errors== "":
         self.miss_words = False
      miss.close()


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


##################################  PROCESSING  ########################################

  def gen_acoustic(self):
    os.system('clear')
    print "\n\n\n ********************************************"
    print " *    GENERATING ACOUSTIC FEATURE FILES     *"
    print " *     on génère le modèle acoustique :     *"
    print " ********************************************\n\n\n"
    os.system ("cd "+self.link+" && sphinx_fe -argfile "+self.hmm+"/feat.params \
        -samprate 16000 -c "+self.link+"/adapt.fileids \
       -di . -do . -ei wav -eo mfc -mswav yes")

    print "\n\n\n ********************************************"
    print " *     CONVERTING SENDUP AND MDEF FILES     *"
    print " *     on converti le sendup et le mdef :   *"
    print " ********************************************\n\n\n"
    try :
      os.system ("pocketsphinx_mdef_convert -text "+self.hmm+"/mdef "+self.hmm+"/mdef.txt")
    except :
      pass
    print "\n\n\n ********************************************"
    print " *     ACCUMULATION OBSERVATION COUNTS      *"
    print " *     création des profiles :              *"
    print " ********************************************\n\n\n"
    self.runCmdOutput("cd "+self.link+" && sudo ./bw  -hmmdir "+self.hmm+"  -moddeffn "+self.hmm+"/mdef.txt  -ts2cbfn .ptm.  -feat 1s_c_d_dd  -svspec 0-12/13-25/26-38  -cmn current  -agc none  -dictfn "+self.dic+"  -ctlfn "+self.link+"/adapt.fileids  -lsnfn "+self.link+"/adapt.transcription  -accumdir .")

    print "\n *********************************************************"
    print " *                  READ CARFULLY LOG !!!                *"
    print " *     If you see unknown words, add them on DIC file    *"
    print " *  Lire attentivement le log, et s'assurer qu'il n'y a  *"
    print " *  de mots inconnus. Sinon, les ajouter au fichier dic  *"
    print " *********************************************************\n"
    print "            !!! IMPORTANT !!! TAKE A PAUSE !!!"

    self.missing_words()
    if self.miss_words == False:
      print "\n Ok, next process..."
      print "\n\n\n *********************************************"
      print " *     CREATING TRANSFORMATION WITH MLLR     *"
      print " *     transformation avec le MLLR :         *"
      print " *********************************************\n\n\n"
      os.system ("cd "+self.link+" && sudo ./mllr_solve     -meanfn "+self.hmm+"/means     -varfn "+self.hmm+"/variances     -outmllrfn "+self.hmm+"/mllr_matrix -accumdir .")


      print "\n next process..."
      print "\n\n\n *********************************************"
      print " *     inserting mllr_matrix in new model     *"
      print " *                                            *"
      print " *********************************************\n\n\n"
      os.system ("cd "+self.link+" && ./mllr_transform -inmeanfn /home/neo/Documents/PAMA/model/fr_ptm_5.2/means -outmeanfn /home/neo/Documents/PAMA/model/fr_ptm_5.2/new_means -mllrmat /home/neo/Documents/PAMA/mllr_matrix")
      a = raw_input("remplacer le means d'origine par le nouveau, puis cliquez sur entrer")


      print "\n\n\n ***********************************************"
      print " *  UPDATING THE ACOUSTIC MODEL WITH MAP UTIL  *"
      print " *     mise a jour du modèle avec le MAP :     *"
      print " ***********************************************\n\n\n"
      os.system ("cd "+self.link+" && ./map_adapt \
    -moddeffn "+self.hmm+"/mdef.txt \
    -ts2cbfn .ptm. \
    -meanfn "+self.hmm+"/means \
    -varfn "+self.hmm+"/variances \
    -mixwfn "+self.hmm+"/mixture_weights \
    -tmatfn "+self.hmm+"/transition_matrices \
    -accumdir . \
    -mapmeanfn "+self.hmm+"/means \
    -mapvarfn "+self.hmm+"/variances \
    -mapmixwfn "+self.hmm+"/mixture_weights \
    -maptmatfn "+self.hmm+"/transition_matrices")

      """
./map_adapt \
    -moddeffn /home/neo/Documents/PAMA/model/fr_ptm_5.2/mdef.txt \
    -ts2cbfn .ptm. \
    -meanfn /home/neo/Documents/PAMA/model/fr_ptm_5.2/means \
    -varfn /home/neo/Documents/PAMA/model/fr_ptm_5.2/variances \
    -mixwfn /home/neo/Documents/PAMA/model/fr_ptm_5.2/mixture_weights \
    -tmatfn /home/neo/Documents/PAMA/model/fr_ptm_5.2/transition_matrices \
    -accumdir . \
    -mapmeanfn /home/neo/Documents/PAMA/model/fr_ptm_5.2/means2 \
    -mapmixwfn /home/neo/Documents/PAMA/model/fr_ptm_5.2/mixture_weights2 \
    -maptmatfn /home/neo/Documents/PAMA/model/fr_ptm_5.2/transition_matrices2
      """

      print "\n\n\n ******************************************"
      print " *  RECREATING THE ADAPTED SENDUP FILE    *"
      print " *   RECONSTRUCTION DU FICHIER SENDUP :   *"
      print " ******************************************\n\n\n"
      os.system ("cd "+self.link+" && ./mk_s2sendump \
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
      print "   Congratulations! You now have an adapted acoustic model!\n  You can delete the files cmusphinx-fr-ptm-5.2-adapt/mixture_weights\n  and cmusphinx-fr-ptm-5.2-adapt/mdef.txt\n  to save space if you like, because they are not used by the decoder.\n  "
      print "         Bravo, fini, tu as adapté ton modèle acoustique !!! \n     effaces mixture_weights et mdef.txt à l'intérieur ton modele.  "
      print " ************************************************************************\n\n\n"

    else :
      print ("Erreurs lors de la compilation ","  Les mots suivants sont absents du dictionnaire "+(self.Errors))
      attente =  raw_input("corrigez et cliquez entree")
       
      self.gen_acoustic()

adapt().menu()


