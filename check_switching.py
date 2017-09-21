import os
from os import system

def diff_letters(a,b):
    return sum ( a[i] != b[i] for i in range(len(a)) )


nr_lines_file = 1000000
nr_comparisons = nr_lines_file - 1

videos = ["BasketballDrive_1920x1080_50","Jockey_3840x2160","Cactus_1920x1080_50","ShakeNDry_3840x2160"]
qps = ["22","27","32","37"]

#videos = ["BasketballDrive_1920x1080_50"]
#qps = ["32"]

models = ["BINARY","HYBRID"]
q_dqs = ["QUANT","DEQUANT"]

system("mkdir -p RESULT_SWITCHING")

switchings = {}
switchings["QUANT"] = ["w","offset","qbits","qcoeff","mult","sum"]
switchings["DEQUANT"] = ["w","offset","qbits","qcoeff","ifresult","mult","sum"]

header = {}
header["QUANT"] = "\t".join(["Video","QP","w","offset","qbits","qcoeff","mult","sum"])
header["DEQUANT"] = "\t".join(["Video","QP","w","offset","qbits","qcoeff","ifresult","mult","sum"])

files_32 = ["mult","offset","sum"]

for model in models:
	for q_dq in q_dqs:
		with open("RESULT_SWITCHING/OUTPUT_%s_%s.txt" % (q_dq, model), "w") as f_out:
			print >> f_out, header[q_dq]
			
			for video in videos:
				for qp in qps:

					results = {}

					path_in = "OUTPUT_%s_%s/%s/%s" % (q_dq, model, video, qp)
					#print path_in
					for name_file in os.listdir(path_in):
						#print name_file
						type_file = name_file.split("_")[2][:-4]

						if type_file in switchings[q_dq]:
							with open("%s/%s" % (path_in, name_file), "r") as f_in:
								lines = f_in.readlines()
								split_old = lines[0].split()[0]
	
								diff = 0
								for line in lines[1:]:
									split = line.split()[0]
									#print [split_old,split,directory+"/"+name_file]
									diff += diff_letters(split_old, split)
									split_old = split

								diff /= float(nr_comparisons)

								n_div = 16.0
								if type_file in files_32:
									n_div = 32.0

								results[name_file.split("_")[2][:-4]] = diff*100.0/n_div
					#print "%s\t%s\%s" % (video,qp,"\t".join([str(results[x]) for x in switchings[q_dq]]))
					print >> f_out, "%s\t%s\t%s" % (video, qp, "\t".join([str(results[x]) for x in switchings[q_dq]]))
