import numpy as np
import cv2
from matplotlib import pyplot as plt

class mouseParam:
    def __init__(self, input_img_name):
        #マウス入力用のパラメータ
        self.mouseEvent = {"x":None, "y":None, "event":None, "flags":None}
        #マウス入力の設定
        cv2.setMouseCallback(input_img_name, self.__CallBackFunc, None)
    
    #コールバック関数
    def __CallBackFunc(self, eventType, x, y, flags, userdata):
        
        self.mouseEvent["x"] = x
        self.mouseEvent["y"] = y
        self.mouseEvent["event"] = eventType    
        self.mouseEvent["flags"] = flags    
    
    #マウスイベントを返す関数
    def getEvent(self):
        return self.mouseEvent["event"]                  

    #xとyの座標を返す関数
    def getPos(self):
        return (self.mouseEvent["x"], self.mouseEvent["y"])
       

img = cv2.imread('animal.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

f = np.fft.fft2(img_gray)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

rows, cols = img_gray.shape
crow,ccol = rows//2 , cols//2 

img_back = np.zeros((rows,cols),np.float64)
img_back2 = np.zeros((rows,cols),np.float64)

mask = np.zeros((rows,cols),np.uint8)
mask2 = np.zeros((rows,cols),np.uint8)
mask3 = np.zeros((rows,cols),np.uint8)

fshift1 = np.zeros((rows,cols),np.uint8)
fshift2 = np.zeros((rows,cols),np.uint8)

if __name__ == "__main__":

    
    #表示するWindow名
    window_name = "input window"

    plt.ion()

    plt.subplot(231)
    plt.imshow(img_gray, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(232)
    plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

    plt.subplot(234)
    plt.imshow(img_back, cmap = 'gray')
    plt.title('Reconstructed Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(235)
    plt.imshow(mask, cmap = 'gray')
    cv2.imshow(window_name, mask)
    mouseData = mouseParam(window_name)
    plt.title(window_name), plt.xticks([]), plt.yticks([])

    plt.subplot(236)
    plt.imshow(img_back2, cmap = 'gray')
    plt.title('Wave'), plt.xticks([]), plt.yticks([])

    plt.draw()
    
    while 1:
        cv2.waitKey(1)
        #左クリックがあったら表示
        if mouseData.getEvent() == cv2.EVENT_LBUTTONDOWN:
            while 1:
                mx, my = mouseData.getPos()

                fx = -(mx-ccol)
                fy = -(-my+crow)

                mx2 = fx+ccol
                my2 = -fy+crow

                mask[my-2:my+2,mx-2:mx+2] = 1

                mask2[my-2:my+2,mx-2:mx+2] = 1
                mask2[my2-2:my2+2,mx2-2:mx2+2] = 1 

                mask3[my,mx] = 1
                mask3[my2,mx2] = 1         

                fshift1 = fshift*mask2
                f_ishift1 = np.fft.ifftshift(fshift1)
                img_back = np.fft.ifft2(f_ishift1)
                img_back = np.abs(img_back)

                fshift2 = fshift*mask3
                f_ishift2 = np.fft.ifftshift(fshift2)
                img_back2 = np.fft.ifft2(f_ishift2)
                img_back2 = np.abs(img_back2)

                mask3[my,mx] = 0
                mask3[my2,mx2] = 0

                plt.subplot(234)
                plt.imshow(img_back, cmap = 'gray')
                plt.title('Reconstructed Image'), plt.xticks([]), plt.yticks([])

                plt.subplot(235)
                plt.imshow(mask, cmap='gray')
                plt.title('mask'), plt.xticks([]), plt.yticks([])

                plt.subplot(236)
                plt.imshow(img_back2, cmap = 'gray')
                plt.title('Wave'), plt.xticks([]), plt.yticks([])
                plt.draw()

                cv2.waitKey(10)

                if mouseData.getEvent() == cv2.EVENT_LBUTTONUP:
                    break;

        
        cv2.waitKey(10)
        #右クリックがあったら終了
        if mouseData.getEvent() == cv2.EVENT_RBUTTONDOWN:
            break;
            
    cv2.destroyAllWindows()