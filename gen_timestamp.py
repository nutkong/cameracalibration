#gen_timestamp.py
#nutkong

#it should read number of files in the directory and generate the timestamps.txt
import os, fnmatch
files_type = '*.jpg'
outputfile = 'orbslam2_office1_timestamp.txt'

def GenerateTimestamp(footage_dir):
  init_timestamp = '00000.jpg'
  n_files = CountFiles(footage_dir)
  time_step = float(1)
  digit_length = 5
  print time_step
  print n_files
  print init_timestamp

  outfile = open(str(outputfile), "w")

  for i in range(n_files):
    #new_timestamp = int(init_timestamp[:digit_length]) + i*int(time_step)
    new_timestamp = ('0000' + str(int(i*time_step)))[-digit_length:]
    print new_timestamp
    outfile.write( str(new_timestamp) + '\n')

  outfile.close()

def CountFiles( footage_dir):
  return  len(fnmatch.filter(os.listdir( footage_dir ), files_type ))


GenerateTimestamp('/home/nutkong/Desktop/office1-color/')
