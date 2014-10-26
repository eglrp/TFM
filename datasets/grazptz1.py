#!/usr/bin/env python

from datasets import variables
from datasets import Camera


def loaddataset():

    setglobalvariables()
    loadcameras()
    return getcameras()


def setglobalvariables():

    variables.current_dataset_path = variables.datasets_path + '/grazptz/set1'
    variables.current_video_path = variables.current_dataset_path + '/videos'


def loadcameras():

    global cam1_g1
    global cam2_g1
    global cam3_g1

    cam1_g1 = Camera()
    cam2_g1 = Camera()
    cam3_g1 = Camera()

    cam1_g1.video.readvideo(variables.current_video_path + '/cam-131.avi')
    cam2_g1.video.readvideo(variables.current_video_path + '/cam-132.avi')
    cam3_g1.video.readvideo(variables.current_video_path + '/cam-133.avi')

    cam1_str = variables.current_dataset_path + '/cameracalib/camera001.cfg'
    cam2_str = variables.current_dataset_path + '/cameracalib/camera002.cfg'
    cam3_str = variables.current_dataset_path + '/cameracalib/camera003.cfg'

    cam1_g1.readconfigfile(cam1_str)
    cam2_g1.readconfigfile(cam2_str)
    cam3_g1.readconfigfile(cam3_str)


def getcam1():

    return cam1_g1


def getcam2():

    return cam2_g1


def getcam3():

    return cam3_g1


def getcameras():

    cam1 = getcam1()
    cam2 = getcam2()
    cam3 = getcam3()

    cam1.printcamerainfo()
    cam2.printcamerainfo()
    cam3.printcamerainfo()

    return [cam1, cam2, cam3]


def printcamerainfo():

    cam1_g1.printcamerainfo()
    cam2_g1.printcamerainfo()
    cam3_g1.printcamerainfo()
