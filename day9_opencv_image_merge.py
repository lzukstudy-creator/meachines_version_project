#!usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Lizhe
# @Time: 2026/3/8 02:26


import cv2
import numpy as np
from PIL import Image
import pytesseract
from open_cv_basic_function import show_pic

class Stitcher:

    def __init__(self):
        pass

    def stitch(self,images,ratio=0.75,reprojThresh=4.0,showMatches=False):

        (imageA,imageB) = images
        (kpsA,featuresA) = self.detetAndDescribe(imageA)
        (kpsB, featuresB) = self.detetAndDescribe(imageB)
        M = self.matchKeypoints(kpsA,kpsB,featuresA,featuresB,ratio,reprojThresh)

        if M is None:
            return None

        (matches, H, status) = M
        result = cv2.warpPerspective(imageA,H,(imageA.shape[1]+imageB.shape[1],imageA.shape[0]))
        show_pic(result,"result")

        result[0:imageB.shape[0],0:imageB.shape[1]] = imageB
        show_pic(result,"result")

        if showMatches:
            vis = self.drawMatches(imageA,imageB,kpsA,kpsB,matches,status)

            return (result,vis)
        return (result,None)

    def drawMatches(self, imageA, imageB, kpsA, kpsB, matches, status):

        (hA, wA) = imageA.shape[:2]
        (hB, wB) = imageB.shape[:2]

        vis = np.zeros((max(hA, hB), wA + wB, 3), dtype="uint8")

        vis[0:hA, 0:wA] = imageA
        vis[0:hB, wA:] = imageB

        for ((trainIdx, queryIdx), s) in zip(matches, status):

            if s == 1:
                ptA = (int(kpsA[queryIdx][0]), int(kpsA[queryIdx][1]))
                ptB = (int(kpsB[trainIdx][0]) + wA, int(kpsB[trainIdx][1]))

                cv2.line(vis, ptA, ptB, (0, 255, 0), 1)

        return vis



    def detetAndDescribe(self,image):
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        descriptor = cv2.SIFT_create()
        (kps,features) = descriptor.detectAndCompute(image,None)

        kps = np.float32([kp.pt for kp in kps])

        return (kps,features)

    def matchKeypoints(self,kpsA,kpsB,featuresA,featuresB,ratio,reprojThresh):
        matcher = cv2.BFMatcher()
        rawMatches = matcher.knnMatch(featuresA,featuresB,2)
        matches = []
        for m in rawMatches:
            if len(m) == 2 and m[0].distance<m[1].distance*ratio:
                matches.append((m[0].trainIdx,m[0].queryIdx))
        if len(matches) >4:
            ptsA = np.float32([kpsA[i] for (_, i) in matches])
            ptsB = np.float32([kpsB[i] for (i, _) in matches])
            (H,status) = cv2.findHomography(ptsA,ptsB,cv2.RANSAC,reprojThresh)
            return (matches,H,status)














