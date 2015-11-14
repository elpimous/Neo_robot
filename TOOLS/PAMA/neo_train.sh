#!/bin/bash 

# path to adapted model
ACOUSTIC_MODEL=/home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt
# path to directory for output
ADAPTED_MODEL=/home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapted
# path to the DIC file
DIC=/home/neo/Documents/PAMA/model/frenchWords62K.dic
# path to the text file with list of .wav files which will be used during the adaptation
FILEIDS=/home/neo/Documents/PAMA/adapt.fileids
# path to the file with trancriptions of .wav files
TRANSC=/home/neo/Documents/PAMA//adapt.transcription
# path to sphinxtrain utils (/usr/local/libexec/sphinxtrain by default)
SPHINXTRAIN=/home/neo/Documents/PAMA

if [ ! $SPHINXTRAIN ]
then
	SPHINXTRAIN=/usr/local/libexec/sphinxtrain
fi

# Convert mdef to text
pocketsphinx_mdef_convert -text $ACOUSTIC_MODEL/mdef $ACOUSTIC_MODEL/mdef.txt

# Generate acoustic model features from our .wav files
# we must set feat.params file of our acoustic model and .fileids file with list of .wav files
$SPHINXTRAIN/sphinx_fe \
 -argfile /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/feat.params \
 -c /home/neo/Documents/PAMA/adapt.fileids \
 -samprate 16000 \
 -di . \
 -do . \
 -ei wav \
 -eo mfc \
 -mswav yes

# Accumulating observation counts

$SPHINXTRAIN/bw \
 -hmmdir /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt \
 -moddeffn /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/mdef.txt \
 -svspec 0-12/13-25/26-38 \
 -ts2cbfn .ptm. \
 -feat 1s_c_d_dd \
 -cmn current \
 -agc none \
 -dictfn /home/neo/Documents/PAMA/model/frenchWords62K.dic \
 -ctlfn /home/neo/Documents/PAMA/adapt.fileids \
 -lsnfn /home/neo/Documents/PAMA//adapt.transcription \
 -accumdir .

# MLLR adaptation

$SPHINXTRAIN/mllr_solve \
    -meanfn /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/means \
    -varfn /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/variances \
    -outmllrfn mllr_matrix -accumdir .
mv mllr_matrix /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/

# Map adaptation

#mkdir $ADAPTED_MODEL/acoustic
#cp /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/* /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapted/acoustic/ 
$SPHINXTRAIN/map_adapt \
    -moddeffn /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/mdef.txt \
    -ts2cbfn .ptm. \
    -meanfn /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/means \
    -varfn /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/variances \
    -mixwfn /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/mixture_weights \
    -tmatfn /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/transition_matrices \
    -accumdir . \
    -mapmeanfn /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/means \
    -mapvarfn /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/variances \
    -mapmixwfn /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/mixture_weights \
    -maptmatfn /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/transition_matrices

# Create sendump file 

$SPHINXTRAIN/mk_s2sendump \
    -pocketsphinx yes \
    -moddeffn /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/mdef.txt \
    -mixwfn /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/mixture_weights \
    -sendumpfn /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/sendump

rm /home/neo/Documents/PAMA/model/cmusphinx-fr-ptm-5.2-adapt/mdef.txt
