import os
from os import system

#videos = ["BasketballDrive_1920x1080_50","Jockey_3840x2160"]
videos = ["BasketballDrive_1920x1080_50","Jockey_3840x2160","Cactus_1920x1080_50","ShakeNDry_3840x2160"]
qps = ["22","27","32","37"]
q_dqs = ["QUANT","DEQUANT"]

#videos = ["BasketballDrive_1920x1080_50"]
#qps = ["32"]

for q_dq in q_dqs:
	
	system("mkdir -p OUTPUT_%s_HYBRID" % (q_dq))
	
	for video in videos:

		system("mkdir -p OUTPUT_%s_HYBRID/%s" % (q_dq, video))

		for qp in qps:

			system("mkdir -p OUTPUT_%s_HYBRID/%s/%s" % (q_dq, video, qp))

			path_in = "/".join(["OUTPUT_%s_BINARY" % (q_dq),video,qp])
			
			path_out = "/".join(["OUTPUT_%s_HYBRID" % (q_dq),video,qp])

			for name_file in os.listdir(path_in):
				
				with open("%s/%s" % (path_in, name_file), "r") as f_in, open("%s/%s" % (path_out, name_file), "w") as f_out:
					lines = f_in.readlines()
					for line in lines:

						split = line.split()[0]
						split_hyb = ""

						for v,w in zip(split[0::2], split[1::2]):
							split_hyb += v
							split_hyb += str(int(bool(int(v)) ^ bool(int(w))))
						
						print >> f_out, split_hyb
