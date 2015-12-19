Qbo_listen
==========

for google stt, use : roslaunch qbo_listen neo_listen_google.launch

Be sure to add your own private google key 
(https://sites.google.com/a/chromium.org/dev/developers/how-tos/api-keys)




for pocketsphinx use :  roslaunch qbo_listen neo_listen_vocal_move.launch (for example)

 HERE SOME MODIFICATIONS TO DO FOR ANYTHING ELSE THAN FRENCH.


#########################################################################################
#
#  Permit voice recognition, where Julius had problems on ubuntu > ver. 11
#
#  can use lot of language models
#
#  for the nexgen Open-Source robot "QBO" from The CORPORA society.
#     (Big thanks for their wonderful and no-limit product !!!)
#
#  Vincent FOUCAULT, elpimous12@orange.fr
#
#########################################################################################

You will find on config rep. some files needed for pocketsphinx, for orders recognition !

#########################################################################################
#                                                                                       #
#                       You can change all words or phrases !!!                         #
#                                                                                       #
#########################################################################################


                                     tip here :
 
                    modify <your_files>.corpus , and create your words,
              go to : http://www.speech.cs.cmu.edu/tools/lmtool-new.html

            click on : Upload a sentence corpus file, and select your file,

                         click on compile knowledge base

                      save the first 2 files (*.dic and *.lm)

 rename as <same_as_existing>.dic, and <same_as_existing>.lm and put them in config rep.


