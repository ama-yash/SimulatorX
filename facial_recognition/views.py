import glob
import os

import cv2
import numpy as np
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render
from keras.models import load_model

from .scripts.counts import *


def uploadImages(request):
    images = request.FILES.getlist("images")
    for i in images:
        default_storage.save("img.jpg", ContentFile(i.read()))
    items = glob.glob(settings.MEDIA_ROOT + "/*")
    img_arr = []
    path_list = []
    for item in items:
        if item.endswith(".jpg") or item.endswith(".jpeg") or item.endswith(".JPG"):
            image = cv2.imread(item)
            image = cv2.resize(image, (96, 96))
            img_arr.append(image)
            path_list.append(item)
    img_arr = np.asarray(img_arr)
    img_arr = img_arr / 255.0
    eth_path = settings.STATIC_ROOT + "/eth-model.h5"
    gen_path = settings.STATIC_ROOT + "/gen-model.h5"
    age_path = settings.STATIC_ROOT + "/age-model.h5"
    eth_model = load_model(eth_path)
    gen_model = load_model(gen_path)
    age_model = load_model(age_path)
    eth_pred = eth_model.predict(img_arr)
    gen_pred = gen_model.predict(img_arr)
    age_pred = age_model.predict(img_arr)
    eth_list = np.argmax(eth_pred, axis=1)
    gen_list = np.argmax(gen_pred, axis=1)
    age_list = np.argmax(age_pred, axis=1)
    data = count(eth_list, gen_list, age_list)
    for item in items:
        if item.endswith(".jpg") or item.endswith(".jpeg") or item.endswith(".JPG"):
            os.remove(item)
    data = {
        "N": data["N"],
        "white": round(data["white"], 2),
        "black": round(data["black"], 2),
        "asian": round(data["asian"], 2),
        "other": round(data["other"], 2),
        "male": round(data["male"], 2),
        "female": round(data["female"], 2),
        "child": round(data["child"], 2),
        "adult": round(data["adult"], 2),
        "senior": round(data["senior"], 2),
    }
    return JsonResponse(data)


def predictImage(request):
    images = request.FILES.getlist("imagee")
    for i in images:
        default_storage.save("img.jpg", ContentFile(i.read()))
    items = glob.glob(settings.MEDIA_ROOT + "/*")
    img_arr = []
    path_list = []
    for item in items:
        if item.endswith(".jpg") or item.endswith(".jpeg") or item.endswith(".JPG"):
            image = cv2.imread(item)
            image = cv2.resize(image, (96, 96))
            img_arr.append(image)
            path_list.append(item)
    img_arr = np.asarray(img_arr)
    img_arr = img_arr / 255.0
    eth_path = settings.STATIC_ROOT + "/eth-model.h5"
    gen_path = settings.STATIC_ROOT + "/gen-model.h5"
    age_path = settings.STATIC_ROOT + "/age-model.h5"
    eth_model = load_model(eth_path)
    gen_model = load_model(gen_path)
    age_model = load_model(age_path)
    eth_pred = eth_model.predict(img_arr)
    gen_pred = gen_model.predict(img_arr)
    age_pred = age_model.predict(img_arr)
    eth_list = np.argmax(eth_pred, axis=1)
    gen_list = np.argmax(gen_pred, axis=1)
    age_list = np.argmax(age_pred, axis=1)
    data = {"eth": int(eth_list[0]), "gen": int(gen_list[0]), "age": int(age_list[0])}
    for item in items:
        if item.endswith(".jpg") or item.endswith(".jpeg") or item.endswith(".JPG"):
            os.remove(item)
    return JsonResponse(data)
