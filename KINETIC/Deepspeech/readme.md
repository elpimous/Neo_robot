MODS FOR DEEPSPEECH MOZILLA FOR MULTILANGUAGE (I hope. LOL)
Tested with French, (use of special characters :âàéèêîôùûç)
               xxx on python 2.7 xxx
===========================================================

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
	open file : your_root/DeepSpeech/data/alphabet/alphabet.txt
	replace 2nd lign (!important : second line only!) with your own alphabet.
		!important! use commas to separate each characters
