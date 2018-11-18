#gen_timestamp.py
#nutkong

#it should read number of files in the directory and generate the timestamps.txt
import os, fnmatch

init_timestamp = 4001
fps = 1000
files_type = '*.png'
outputfile = 'orbslam2_timestamp.txt'

def GenerateTimestamp(footage_dir):
  n_files = CountFiles(footage_dir)
  time_step = float(1)/fps*1000
  print time_step
  print n_files
  print init_timestamp

  outfile = open(str(outputfile), "w")

  for i in range(n_files):
    new_timestamp = init_timestamp + i*int(time_step)
    outfile.write('0' + str(new_timestamp) + '\n')

  outfile.close()

def CountFiles( footage_dir):
  return  len(fnmatch.filter(os.listdir( footage_dir ), files_type ))


GenerateTimestamp('/home/nutkong/Desktop/5001_N/')
