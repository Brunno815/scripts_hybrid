from os import system
import os

#videos = [["BasketballDrive_1920x1080_50","50"],["Jockey_3840x2160","120"]]
#videos = [["Jockey_3840x2160","120"],["Cactus_1920x1080_50","50"],["ShakeNDry_3840x2160","120"]]

#videos = [["BasketballDrive_1920x1080_50","15"],["Jockey_3840x2160","15"],["Cactus_1920x1080_50","15"],["ShakeNDry_3840x2160","15"]]
videos = [["HoneyBee_3840x2160","15"],["Kimono1_1920x1080_24","15"],["ParkScene_1920x1080_24","15"],["BQTerrace_1920x1080_60","15"],["BasketballDrive_1920x1080_50","15"],["Jockey_3840x2160","15"],["Cactus_1920x1080_50","15"],["ShakeNDry_3840x2160","15"]]
qps = ["22","27","32","37"]


for video in videos:
	for qp in qps:
		com_codec = ""
		com_gprof = ""

		split_video_name = video[0].split("_")[0]

		com_codec = "./TAppEncoderStatic -c ~/HM-16.7_extractSAD/cfg/encoder_lowdelay_main.cfg -c ~/HM-16.7_extractSAD/cfg/per-sequence/%s.cfg  -i ~/origCfP/%s.yuv -f %s --QP=%s --PrintQuant=1 --PrintDequant=1 --RDOQ=0" % (split_video_name, video[0], video[1], qp)
	
		print com_codec
		system(com_codec)
