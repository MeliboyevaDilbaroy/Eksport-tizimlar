# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18Z9ojHTL39wDfMNToxugt2Pg8Is79rDs
"""

rom google.colab.patches import  cv2_imshow
 import cv2
 def kitob(nomi):
  if nomi=="Saodat asri qissalari":
    rasm=cv2.imred("1.jfif")
    cv2_imshow(rasm)
    return "narxi 300.000"
    elif nomi=="Bir olima qiz bor edi":
      rasm=cv2.imred("2.jfif")
      cv2_imshow(rasm)
     return "narxi 60.000"
     else:
      return " kitoblar haqida ma'lumot kerak bo'lsa bizga murojat qiling"
nomi=input("kitob nomini kiriting:")
natija=kitob (nomi)
print(natija)



from google.colab.patches import cv2_imshow
import cv2

def kitob(nomi):
    if nomi == "Saodat asri qissalari":
        rasm = cv2.imread("1.jfif")
        cv2_imshow(rasm)
        return "narxi 300.000"
    elif nomi == "Bir olima qiz bor edi":
        rasm = cv2.imread("2.jfif")
        cv2_imshow(rasm)
        return "narxi 60.000"
    else:
        return "kitoblar haqida ma'lumot kerak bo'lsa bizga murojat qiling"

nomi = input("kitob nomini kiriting: ")
natija = kitob(nomi)
print(natija)

from google.colab.patches import cv2_imshow
import cv2

def kitob(nomi):
    if nomi == "Saodat asri qissalari":
        rasm = cv2.imread("1.jfif")
        cv2_imshow(rasm)
        return "narxi 300.000"
    elif nomi == "Bir olima qiz bor edi":
        rasm = cv2.imread("2.jfif")
        cv2_imshow(rasm)
        return "narxi 60.000"
    else nomi=="O'tgan kunlar":
      rasm = cv_2.imread("3.jfif")
      cv2_imshow(rasm)
        return "narxi 50.000"
    else nomi=="Mehrobdan Chayon":
      rasm = cv_2.imread("4.jfif")
      cv2_imshow(rasm)
        return "narxi 55.000"
     else nomi=="Ikki eshik orasi":
      rasm = cv_2.imread("5.jfif")
      cv2_imshow(rasm)
        return "narxi 65.000"

        else:

  return "kitoblar haqida ma'lumot kerak bo'lsa bizga murojat qiling"

nomi = input("kitob nomini kiriting: ")
natija = kitob(nomi)
print(natija)

from google.colab.patches import cv2_imshow
import cv2

def kitob(nomi):
    if nomi == "Saodat asri qissalari":
        rasm = cv2.imread("1.jfif")
        cv2_imshow(rasm)
        return "narxi 300.000"
    elif nomi == "Bir olima qiz bor edi":
        rasm = cv2.imread("2.jfif")
        cv2_imshow(rasm)
        return "narxi 60.000"
    elif nomi == "O'tgan kunlar":
        rasm = cv2.imread("3.jfif")
        cv2_imshow(rasm)
        return "narxi 50.000"
    elif nomi == "Mehrobdan Chayon":
        rasm = cv2.imread("4.jfif")
        cv2_imshow(rasm)
        return "narxi 55.000"
    elif nomi == "Ikki eshik orasi":
        rasm = cv2.imread("5.jfif")
        cv2_imshow(rasm)
        return "narxi 65.000"
    elif nomi == "Men":
        rasm = cv2.imread("6.jfif")
        cv2_imshow(rasm)
        return "narxi 45.000"
    elif nomi == "Payg'ambarlar tarixi":
        rasm = cv2.imread("7.jfif")
        cv2_imshow(rasm)
        return "narxi 269.000"
    elif nomi == "Ulamolar nazdida vaqtning qadri":
        rasm = cv2.imread("8.jfif")
        cv2_imshow(rasm)
        return "narxi 45.000"
    elif nomi == "Atom odatlari":
        rasm = cv2.imread("9.jfif")
        cv2_imshow(rasm)
        return "narxi 50.000"
    elif nomi == "Af et Allohim":
        rasm = cv2.imread("10.jfif")
        cv2_imshow(rasm)
        return "narxi 62.000"


    else:
        return "kitoblar haqida ma'lumot kerak bo'lsa bizga murojat qiling"

nomi = input("kitob nomini kiriting: ")
natija = kitob(nomi)
print(natija)