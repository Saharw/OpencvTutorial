# -*- coding=GBK -*-

"""
@Time �� 2019/12/1 23:10
@Auth �� WJJ
@File ��opencv_numpy_img.py
@IDE ��PyCharm
@Motto��Don't forget what you started out with and stick to it(Always Be Coding)

"""

"""
    pythonʵ��opencv: numpy�����������ͼƬ
"""

import cv2 as cv
import numpy as np

def access_pixles(image):
    """
    numpy �������
    :param image:
    :return:
    """

    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]

    print("width: {}, height: {}, channel: {}".format(width, height, channel))

    for row in range(height):
        for col in range(width):
            for c in range(channel):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("edit", image)

# if __name__ == '__main__':
#     src = cv.imread(r"D:\project\OpencvTutorial\images\panda.jpg")
#     cv.imshow("befor", src)
#     t1 = cv.getTickCount() # ���뼶�ļ�ʱ����, û��¼��ϵͳ����������ʱ�����
#     access_pixles(src)
#     t2 = cv.getTickCount()
#     time = (t2 - t1)*1000/cv.getTickFrequency() # getTickFrequency ���ڷ���CPU��Ƶ��, ��������ļ�ʱ��������
#     print("time: {}".format(time))  # �������ʱ��
#     cv.waitKey(0)
#     cv.destroyAllWindows()


def create_image_zeros():
    """
        �Զ���һ�Ŷ�ͨ����ͼƬ
        �õ�����: zeros ��ones
    """
    img = np.zeros([400, 400, 3], np.uint8) # zeros: double�������, ����400*400 3��ͨ���ľ���ͼ��,
                                            # ������classname Ϊuint8
    img[:, :, 0] = np.ones([400, 400])*255  # ones([400, 400]) �Ǵ���һ��400*400��ȫ1����, *255��ȫ255����,
                                            # ������������ֵ����img�ĵ�һά
    img[:, :, 1] = np.ones([400, 400])*255  # �ڶ�άȫ��255
    img[:, :, 2] = np.ones([400, 400])*255  # ����άȫ��255
    cv.imshow("my_image", img)            # ���һ��400*400�İ�ɫͼƬ(255, 255, 255): ��(B), ��(G), ��(R)


# if __name__ == '__main__':
#     create_image_zeros()
#     cv.waitKey(0)
#     cv.destroyAllWindows()


def create_image_ones():
    """
        �Զ���һ�ŵ�ͨ����ͼƬ
    """

    img = np.ones([400, 400, 1], np.uint8)
    img = img * 127
    cv.imshow("my_image", img)

# if __name__ == '__main__':
#     create_image_ones()
#     cv.waitKey(0)
#     cv.destroyAllWindows()


def inverse(image):
    """
    ���ÿ⺯��ʵ������ȡ�� ,����bitwise_not��������ʱ��ǳ���
    :param image:
    :return:
    """

    dst = cv.bitwise_not(image)
    cv.imshow("inverse", dst)

if __name__ == '__main__':
    src = cv.imread(r"D:\project\OpencvTutorial\images\panda.jpg")
    cv.namedWindow("befor", cv.WINDOW_NORMAL)
    cv.imshow("befor", src)
    t1 = cv.getTickCount()
    inverse(src)
    t2 = cv.getTickCount()
    time = (t2 - t1)*1000/cv.getTickFrequency()
    print("time: {}".format(time))
    cv.waitKey(0)
    cv.destroyAllWindows()