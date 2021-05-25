import cv2
camdev = cv2.VideoCapture(0)

def  drawSight( x, y):
    img[y,x-1]=[0,0,255]
    img[y,x+1]=[0,0,255]
    img[y-1,x]=[0,0,255]
    img[y+1,x]=[0,0,255]
    
def dscColor(bgr):
    thr = 1.5
    if bgr[0] > (bgr[1] * thr) and bgr[0] > (bgr[1] * thr):

        print("red")
    elif bgr[1] > (bgr[2] * thr) and bgr[1] > (bgr[0] * thr):

        print("green")
    elif bgr[2] > (bgr[1] * thr) and bgr[2] > (bgr[0] * thr):
   
        print("green")
    else:
        print("muzi")
        
while True:
    ret, img = camdev.read() 
    y=230
    x=300  
    bgr = img[ y, x]#たて、よこ
 
    drawSight( x, y)
    cv2.imshow( 'Image View', img)
    keycode = cv2.waitKey(1)

    if keycode == 27: #Escキーで終了
        break
    elif keycode==32: #スペースキーでＲＧｂを表示
        cv2.imwrite( 'test.jpg', img)
        print(bgr[2], bgr[1], bgr[0])
        dscColor(bgr)


camdev.release()
cv2.destroyAllWindows()