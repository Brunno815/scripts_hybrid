import os
from os import system

def num_to_bin(num, wordsize):
    if num < 0:
        num = 2**wordsize+num
    base = bin(num)[2:]
    padding_size = wordsize - len(base)
    return '0' * padding_size + base

videos = ["BasketballDrive_1920x1080_50","Jockey_3840x2160"]

videos = ["BasketballDrive_1920x1080_50","Jockey_3840x2160","Cactus_1920x1080_50","ShakeNDry_3840x2160"]

videos = ["BasketballDrive_1920x1080_50","Jockey_3840x2160","Cactus_1920x1080_50","ShakeNDry_3840x2160","BQTerrace_1920x1080_60","HoneyBee_3840x2160","Kimono1_1920x1080_24","ParkScene_1920x1080_24"]

#videos = ["BasketballDrive_1920x1080_50"]

q_dqs = ["QUANT","DEQUANT"]
files_32 = ["files_quant_mult.txt","files_quant_offset.txt","files_quant_sum.txt","files_dequant_mult.txt","files_dequant_sum.txt","files_dequant_offset.txt"]

for q_dq in q_dqs:

	system("mkdir -p OUTPUT_%s_BINARY" % (q_dq))
	
	for directory in videos:
	
		system("mkdir -p OUTPUT_%s_BINARY/%s" % (q_dq, directory))
		
		for qp in os.listdir("OUTPUT_%s/%s" % (q_dq, directory)):
			
			system("mkdir -p OUTPUT_%s_BINARY/%s/%s" % (q_dq, directory, qp))

			for name_file in os.listdir("OUTPUT_%s/%s/%s" % (q_dq, directory, qp)):
				
				with open("OUTPUT_%s/%s/%s/%s" % (q_dq, directory, qp, name_file), "r") as f_in, open("OUTPUT_%s_BINARY/%s/%s/%s" % (q_dq, directory, qp, name_file) ,"w") as f_out:
					n_bits = 16

					if name_file in files_32:
						n_bits = 32

					for line in f_in.readlines():
						split_line = line.split()
						#print split_line[0]
						bin_value = num_to_bin(int(split_line[0]), n_bits)
						print >> f_out, "%s" % (bin_value)
