# -*- coding: utf-8 -*-
import math


def deg2grad(stopnie):
    grady = (stopnie * 10) / 9
    return grady

def grad2deg(grady):
    stopnie = (grady * 9) / 10
    return stopnie

def grad2rad(grady):
    radiany = (grady * math.pi) / 200

    return radiany


def rad2grad(radiany):
    grady = (radiany * 200) / math.pi

    return grady


# ======================== for 3


def decimal_deg2rad(decimal_deg):
    radiany = (decimal_deg * math.pi) / 180

    return radiany


def rad2decimal_deg(radiany):
    dec = (radiany * 180) / math.pi

    return dec



# ======================== for 4

def decimal_deg2dms_deg(decimal_deg):
    min, sek = divmod(decimal_deg * 3600, 60)
    stopnie, min = divmod(min, 60)

    return stopnie, min, sek


def dms_deg2decimal_deg(dms_deg):
    decimal_deg = float(dms_deg[0]) + float(dms_deg[1]) / 60 + float(dms_deg[2]) / 3600

    return decimal_deg

# ======================== for 5
