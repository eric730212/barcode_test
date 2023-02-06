import cv2
import pyzbar.pyzbar as pyzbar
import numpy as np


def decodeDisplay(image):
    barcodes = pyzbar.decode(image)
    rects_list = []
    polygon_points_list = []
    QR_info = []

    # 这里循环，因为画面中可能有多个二维码
    for barcode in barcodes:
        # 提取条形码的边界框的位置
        # 画出图像中条形码的边界框
        (x, y, w, h) = barcode.rect
        rects_list.append((x, y, w, h))
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        polygon_points = barcode.polygon
        # print(f"polygon_points: {polygon_points}")  # polygon_points: [Point(x=217, y=174), Point(x=257, y=353), Point(x=433, y=316), Point(x=394, y=140)]
        # print(f"polygon_points: {polygon_points[0]}")  # polygon_points: Point(x=217, y=174)
        point_x, point_y = polygon_points[0]
        # print(f"point_x, point_y: {point_x, point_y}")  # point_x, point_y: (217, 174)

        extract_polygon_points = np.zeros((4, 2), dtype=np.int)
        for idx, points in enumerate(polygon_points):
            point_x, point_y = points  # 默认得到的point_x, point_y是float64类型
            extract_polygon_points[idx] = [point_x, point_y]

        print(extract_polygon_points.shape)  # (4, 2)

        # 不reshape成 (4,1 2)也是可以的
        extract_polygon_points = extract_polygon_points.reshape((-1, 1, 2))
        polygon_points_list.append(extract_polygon_points)

        # 要加上中括号，否则只会绘制四个点
        # cv2.polylines(image, extract_polygon_points, isClosed=True, color=(255, 0, 255), thickness=2)

        # 绘制多边形
        cv2.polylines(image, [extract_polygon_points], isClosed=True, color=(255, 0, 255), thickness=2,
                      lineType=cv2.LINE_AA)

        # 条形码数据为字节对象，所以如果我们想在输出图像上画出来，就需要先将它转换成字符串
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # 绘出图像上条形码的数据和条形码类型
        text = "{} ({})".format(barcodeData, barcodeType)
        QR_info.append(text)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    .5, (0, 0, 125), 2)

        # 向终端打印条形码数据和条形码类型
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    return image, rects_list, polygon_points_list, QR_info


def detect():
    cap = cv2.VideoCapture(1)

    while True:
        # 读取当前帧
        ret, frame = cap.read()
        # frame = cv2.resize(frame,(1920,1080))
        # 转换为灰度图是为了检测到二维码，如果是BGR图很大概率是检测不到二维码
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        im, rects_list, polygon_points_list, QR_info = decodeDisplay(gray)

        # 把检测到二维码的信息再绘制到BGR彩色图像上
        for data in zip(rects_list, polygon_points_list, QR_info):
            print(f"data: {data}")
            x, y, w, h = data[0]
            polygon_points = data[1]
            text = data[2]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.polylines(frame, [polygon_points], isClosed=True, color=(255, 0, 255), thickness=2,
                          lineType=cv2.LINE_AA)
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        .5, (0, 0, 125), 2)

        # 因为一个是单通道的灰度图，一个是BGR三通道的彩色图，因此不能够拼接在一起显示，这里就用两个窗口显示
        cv2.imshow("camera", im)
        cv2.imshow("frame", frame)

        # 按q键退出画面显示
        k = cv2.waitKey(1)
        if k == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    detect()

