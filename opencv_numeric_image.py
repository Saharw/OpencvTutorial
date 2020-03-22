# -*- coding=GBK -*-
import cv2 as cv
import numpy as np



def numeric_image(src11, src22):
    """
        һ�� ��ֵ����
        opencv�Դ�ͼƬɫ�صĴ�������
        ��ӣ� add()
        ����� subtract()
        ��ˣ� numltiply()
        ����� divide()
        ԭ��: ͨ����ȡ���ţ�һ��ֻ�����ţ���ͼƬ��ͬһ��λ�õ�ɫ��ֵ��ʵ������
        �����Ҫ�� ����ͼƬ��shapeҪһ��
    """

    src = cv.add(src11, src22)  #���
    cv.imshow("add", src)

    src = cv.subtract(src11, src22)
    cv.imshow("subtract", src)

    src = cv.multiply(src11, src22)
    cv.imshow("multiply", src)

    src = cv.divide(src11, src22)
    cv.imshow("divide", src)



def logicl_image(src11, src22):
    """
    �߼����㣺 ���ǵĲ���
    :param src11:
    :param src22:
    :return:
    """
    src = cv.bitwise_and(src11, src22)    #��  ����ͼƬͬһλ�õ�ɫ������ֵ����Ϊ��ĲŻ������
    cv.imshow("and", src)

    src = cv.bitwise_or(src11, src22)     #��   ����ͼƬͬһλ�õ�ɫ������ֵ��ȫΪ��ĲŻ����
    cv.imshow("or", src)

    src = cv.bitwise_not(src11, src22)    #��    ��һ��ͼƬ����  ȡ��
    cv.imshow("not", src)
src1 = cv.imread("./imgs/linux.jpg")
src2 = cv.imread("./imgs/window.jpg")
cv.imshow("origrinal1", src1)
cv.imshow("origrinal2", src2)

# numeric_image(src1, src2)   # ��ֵ����
logicl_image(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()