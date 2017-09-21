import os

def file_len(fname):
        i = 0
        with open(fname,"r") as f:
                for i,l in enumerate(f):
                        pass
        return i+1

videos = ["BasketballDrive_1920x1080_50","Cactus_1920x1080_50","Jockey_3840x2160","ShakeNDry_3840x2160","BQTerrace_1920x1080_60","Jockey_3840x2160","Kimono1_1920x1080_24","ParkScene_1920x1080_24"]

#videos = ["BasketballDrive_1920x1080_50"]
#videos = ["BasketballDrive_1920x1080_50","Jockey_3840x2160"]
qps = ["22","27","32","37"]
q_dqs = ["QUANT","DEQUANT"]
#qps = ["32"]

for q_dq in q_dqs:
	for video in videos:
	        for qp in qps:
			dir_ = "%s" % ("/".join(["OUTPUT_%s" % (q_dq), video, qp]))
			for name_file in os.listdir("%s" % ("/".join(["OUTPUT_%s" % (q_dq), video, qp]))):
				n_lines = file_len("%s/%s" % (dir_, name_file))
	                	if n_lines != 1000000:
	                		print [q_dq,video,qp,n_lines,name_file]
