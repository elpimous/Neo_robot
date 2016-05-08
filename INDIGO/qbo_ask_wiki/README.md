QBO_WIKI
========

dependencies : pip install wikipedia

MAI 2016 7 AVRIL version 1.0 : creation

######################################################################
#                                                                    #
#   a package to search on wikipedia and speak wanted infos          #
#                                                                    #
######################################################################


this node creates a service called "/wiki"


*** When qbo_wiki is running, you can make QBO speak response ***



try :
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

open one terminal : rosrun qbo_ask_wiki ask_wiki.py

in other terminal : rosservice call /wiki "the word you search"

ex : rosservice call /wiki "einstein"

