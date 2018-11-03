#gen_timestamp.py
#nutkong

#it should read number of files in the directory and generate the timestamps.txt
import os, fnmatch

init_timestamp = 1403715297062142976
fps = 40

def GenerateTimestamp(footage_dir):
  n_files = CountFiles(footage_dir)
  time_step = float(1)/fps*1000
  print time_step

  for i in range(n_files):
    new_timestamp = init_timestamp + i*int(time_step)
    print new_timestamp

def CountFiles( footage_dir):
  return  len(fnmatch.filter(os.listdir( footage_dir ), '*.jpg' ))


GenerateTimestamp('/Users/nutkong/Desktop/images2')
