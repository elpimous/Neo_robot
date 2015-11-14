depedencies :
°°°°°°°°°°°°°
install python-imaging-tk   
install pyaudio

important, do a : sudo chmod 777 -R <your PAMA directory>


install notes :
°°°°°°°°°°°°°°°

install bison, sphinxtrain alpha5, sphinxbase alpha5, and pocketsphinx alpha5
     http://cmusphinx.sourceforge.net/wiki/download


to launch :
°°°°°°°°°°°
launch pama.py
(if it can't automatically launch, start it from terminal and report errors !)


usage :
°°°°°°°
- enter your links, (if exists, they will appear),
- select your mode :
	* automatic : sentences will appear automatically (you can add your sentences in "sentences.list")
        * manual : type your sentence in the white box
- click "rec" to record voice,
- choose keep voice, or record again,
- choose if you want another sentence,(click "no" will start adaptation with all sentences you made before)
- wait until it's finished
  Done.

____________________________________________________________________________________________________________________

NB.: ABOUT ERRORS :

--- Sphinx_fe: error while loading shared libraries: libsphinxbase.so.3: cannot open shared object file: No such file or directory
	you need to properly reinstall sphinxbase (./configure, make, make install) and reboot
___________________________________________________________________________________________________________________________

--- Be sure to copy :
	bw
	map_adapt
	mk_s2sendump
	mllr_solve
in PAMA root.
___________________________________________________________________________________________________________________________

Don't forget : sudo chmod 777 -R <your PAMA directory>
___________________________________________________________________________________________________________________________

---/config/pama.config : contain your links (blanck in first, and full after first imput in PAMA
___________________________________________________________________________________________________________________________

---/model : must contain a directory, and 2 files (see textfile inside)
___________________________________________________________________________________________________________________________

---/verify that "pama.config" contains the 4 links + "english" or "français" otherwise it won't work
___________________________________________________________________________________________________________________________


PLEASE, REPORT ANY PROBLEMS AT : elpimous12@orange.fr
thanks,
Vincent.

