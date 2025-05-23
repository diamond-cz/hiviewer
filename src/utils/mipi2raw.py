# -*- coding: utf-8 -*-
import os
import time
import cv2
import numpy as np

global bayer_order_maps

bayer_order_maps = {
    'RGGB': cv2.COLOR_BayerRG2RGB,
    'BGGR': cv2.COLOR_BayerBG2RGB,
    'GRBG': cv2.COLOR_BayerGR2RGB,
    'GBRG': cv2.COLOR_BayerGB2RGB,
    "gray": 0,
}


def unpack_mipi_raw10(byte_buf):
    data = np.frombuffer(byte_buf, dtype=np.uint8)
    # 5 bytes contain 4 10-bit pixels (5x8 == 4x10)
    b1, b2, b3, b4, b5 = np.reshape(
        data, (data.shape[0]//5, 5)).astype(np.uint16).T
    p1 = (b1 << 2) + ((b5) & 0x3)
    p2 = (b2 << 2) + ((b5 >> 2) & 0x3)
    p3 = (b3 << 2) + ((b5 >> 4) & 0x3)
    p4 = (b4 << 2) + ((b5 >> 6) & 0x3)
    unpacked = np.reshape(np.concatenate(
        (p1[:, None], p2[:, None], p3[:, None], p4[:, None]), axis=1),  4*p1.shape[0])
    return unpacked


def unpack_mipi_raw12(byte_buf):
    data = np.frombuffer(byte_buf, dtype=np.uint8)
    # 3 bytes contain 2 12-bit pixels (3x8 == 2x12)
    b1, b2, b3 = np.reshape(
        data, (data.shape[0]//3, 3)).astype(np.uint16).T
    p1 = (b1 << 4) + ((b3) & 0xf)
    p2 = (b2 << 4) + ((b3 >> 4) & 0xf)
    unpacked = np.reshape(np.concatenate(
        (p1[:, None], p2[:, None]), axis=1),  2*p1.shape[0])
    return unpacked


def unpack_mipi_raw14(byte_buf):
    data = np.frombuffer(byte_buf, dtype=np.uint8)
    # 7 bytes contain 4 14-bit pixels (7x8 == 4x14)
    b1, b2, b3, b4, b5, b6, b7 = np.reshape(
        data, (data.shape[0]//7, 7)).astype(np.uint16).T
    p1 = (b1 << 6) + (b5 & 0x3f)
    p2 = (b2 << 6) + (b5 >> 6) + (b6 & 0xf)
    p3 = (b3 << 6) + (b6 >> 4) + (b7 & 0x3)
    p4 = (b4 << 6) + (b7 >> 2)
    unpacked = np.reshape(np.concatenate(
        (p1[:, None], p2[:, None], p3[:, None], p4[:, None]), axis=1),  4*p1.shape[0])
    return unpacked


def convertMipi2Raw(mipiFile, imgWidth, imgHeight, bitDeepth, bayer_order=cv2.COLOR_BayerBG2BGR):
    mipiData = np.fromfile(mipiFile, dtype='uint8')
    print("mipiraw file size:", mipiData.size)

    if bitDeepth == 8 or bitDeepth == 16:
        print("raw8 and raw16 no need to unpack")
        return
    elif bitDeepth == 10:
        # raw10
        bayerData = unpack_mipi_raw10(mipiData)
        img = bayerData >> 2
    elif bitDeepth == 12:
        # raw12
        bayerData = unpack_mipi_raw12(mipiData)
        img = bayerData >> 4
    elif bitDeepth == 14:
        # raw14
        bayerData = unpack_mipi_raw14(mipiData)
        img = bayerData >> 6
    else:
        print("unsupport bayer bitDeepth:", bitDeepth)

    bayerData.tofile(mipiFile[:-4]+'_unpack.raw')

    print("bayerData shape:", bayerData.shape)
    img = img.astype(np.uint8).reshape(imgHeight, imgWidth, 1)
    print("img shape:", img.shape)
    print("bayer_order:", bayer_order)
    try:
        rgbimg = cv2.cvtColor(img, bayer_order)
    except Exception as e:
        print("Error in cv2.cvtColor:", e)
        return

    try:
        cv2.imwrite(mipiFile[:-4]+'_unpack.jpg', rgbimg)
    except Exception as e:
        print("Error in cv2.imwrite:", e)


def ProcSingleFile(rawFile, img_width, img_height, rawDepth, bayer_order):
    # (path, rawFile) = os.path.split(raw_name)
    print("process ", rawFile, "...")
    start_time = time.monotonic_ns()
    convertMipi2Raw(rawFile, img_width, img_height, rawDepth, bayer_order)
    end_time = time.monotonic_ns()
    print("convertMipi2Raw cost:",
          (end_time - start_time) // 1000000, 'ms')


def ProcPath(path, img_width, img_height, rawDepth, bayer_order):
    print('procesing ', path)
    file_list = os.listdir(path)
    for f in file_list:
        f_lower = f.lower()
        if f_lower.endswith('.rawmipi'):
            raw_name = '%s\\%s' % (path, f)
            ProcSingleFile(raw_name, img_width, img_height,
                           rawDepth, bayer_order)


# if "__main__" == __name__:
#     parser = argparse.ArgumentParser()

#     parser.add_argument(
#         "--path", help="input raw path", required=False, type=str)
#     parser.add_argument(
#         "--file", help="input raw file name", required=False, type=str)
#     parser.add_argument("--width", help="raw image width",
#                         required=True, type=int)
#     parser.add_argument("--height", help="raw image height",
#                         required=True, type=int)
#     parser.add_argument(
#         "--depth", help="raw image depth [8, 10, 12, 14, 16]", required=True, type=int)
#     parser.add_argument(
#         "--bayer", help="bayer format [RGGB, BGGR, GRBG, GBRG]", required=True, type=str)

#     args = parser.parse_args()

#     rawPath = args.path
#     rawFile = args.file
#     img_width = args.width
#     img_height = args.height
#     rawDepth = args.depth
#     bayer = args.bayer
#     bayer_order = bayer_order_maps[bayer]
#     print(bayer_order)
#     if rawPath is not None:
#         ProcPath(rawPath, img_width, img_height, rawDepth, bayer_order)
#     elif rawFile is not None:
#         ProcSingleFile(rawFile, img_width, img_height, rawDepth, bayer_order)
#     else:
#         print("parameters wrong!!! no path or file")
