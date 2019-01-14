import os

s1 = 'cd ~/one-working'
s2 = ''' nohup nice ~/mosesdecoder/scripts/training/train-model.perl -root-dir train \
 -corpus ~/zhihu-corpus-one/clean/train.clean                             \
 -f ans -e com -alignment grow-diag-final-and -reordering msd-bidirectional-fe \
 -lm 0:3:$HOME/lm/zhihu_comment.one.blm.com:8                          \
 -external-bin-dir ~/mosesdecoder/tools -cores 4 >& training.out '''

# Tuning  use dev data
# token and truecase

s3 = 'cd ~/zhihu-corpus-one'
s4 = ''' ~/mosesdecoder/scripts/recaser/truecase.perl --model truecase-model.cn.ans \
   < token/validset1.token.ans > true/validset1.true.ans'''

s5='''~/mosesdecoder/scripts/recaser/truecase.perl --model truecase-model.cn.com \
   < token/validset1.token.com > true/validset1.true.com'''

# training and launch the tuning process
s6 = 'cd ~/one-working'
s7 = '''
 nohup nice ~/mosesdecoder/scripts/training/mert-moses.pl \
  ~/zhihu-corpus-one/true/validset1.true.ans ~/zhihu-corpus-one/true/validset1.true.com \
  ~/mosesdecoder/bin/moses train/model/moses.ini --mertdir ~/mosesdecoder/bin/ \
  --decoder-flags="-threads 4"  &> mert.out 
 '''

# testing and type the input

s8 = '~/mosesdecoder/bin/moses -f ~/one-working/mert-work/moses.ini'


# test data 
s9 = 'cd ~/zhihu-corpus-one'
s10 = ''' ~/mosesdecoder/scripts/recaser/truecase.perl --model truecase-model.cn.ans \
   < token/testset1.token.ans > true/testset1.true.ans'''
s11 = ''' ~/mosesdecoder/scripts/recaser/truecase.perl --model truecase-model.cn.com \
   < token/testset1.token.com > true/testset1.true.com'''
# filter for this test set

s12 = 'cd ~/one-working'
s13 = ''' ~/mosesdecoder/scripts/training/filter-model-given-input.pl             \
   filtered-zhihu-testset1-ans mert-work/moses.ini ~/zhihu-corpus-one/true/testset1.true.ans \
   -Binarizer ~/mosesdecoder/bin/processPhraseTableMin'''
# test decoder 
s14 = '''nohup nice ~/mosesdecoder/bin/moses            \
   -f ~/one-working/filtered-zhihu-testset1-ans/moses.ini   \
   < ~/zhihu-corpus-one/true/testset1.true.ans                \
   > ~/one-working/testset1.translated.com         \
   2> ~/one-working/zhihu-testet1.out'''


 # get bleu 
s15 = ''' ~/mosesdecoder/scripts/generic/multi-bleu.perl \
   -lc ~/zhihu-corpus-one/true/testset1.true.com              \
   < ~/one-working/testset1.translated.com'''

def process_command(command):
	# print(command)
	os.system(command)
	

commands =' ; '.join([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15])

process_command(commands)