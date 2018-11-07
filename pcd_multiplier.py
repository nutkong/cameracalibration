import os, fnmatch

def readPCDFile(filename):
  file = open(filename,"r")
  outfile = open("pcd_multiply_nk.pcd","w")
  lines_to_write = []
  for line in file:
    if( float(line.split()[0]) == False  and type( float(line.split()[0])) == float):
        print "yay nuber!!!!"
        print line

    lines_to_write.append(line)

    print line.split()

  outfile.writelines(lines_to_write)
  outfile.close

readPCDFile('/home/nutkong/Documents/dso_with_saving_pcl/build/pcl_data.pcd')
