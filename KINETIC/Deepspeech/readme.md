MODS FOR DEEPSPEECH MOZILLA FOR MULTILANGUAGE (I hope. LOL)
Tested with French, (use of special characters :âàéèêîôùûç)
===========================================================
v1.0
====

for python 2.7
==============


The principle :
---------------
	let the program read a string, containing YOUR OWN alphabet language,
	deduct the "n_character" value (len(string)+3)
		(perhaps change 3 by another value. Ex : "'" character for french !)
	replace each character by it placement value in string
		(no more use of ascii table convert !)

Normally, It should help all people who use of characters != of [a-z]


Needs :
-------

1/ COPY files in correct Dirs;


2/ open file : your_root/DeepSpeech/data/alphabet/alphabet.txt
	replace 2nd lign (!important : second line only!) with your own alphabet.
		!important! use commas to separate each characters. ex : a,b,c,d


3/ Do some changes in Deepspeech.py, spell.py and text.py,
	(all changes are marked with "***********  MOD for personal alphabet use !!!  ************",
	for an easy find in text)

        Or copy/pastle my files on yours !!!
	====================================


4/ add program 'alphabet_converter.py'  to  your_root/DeepSpeech/util/



Finally:
--------
	feed your word.txt with your natural sentences
	build your own LM
	test !
