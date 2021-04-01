#%%
import cv2
import numpy as np
import datetime
print("Done")
# %%
img=cv2.imread(r"C:\Users\siddh\Downloads\maxresdefault.jpg")
cv2.imshow("Logo",img)
cv2.waitKey()

cv2.destroyAllWindows()
# %%
vid=cv2.VideoCapture(0)
vid.set(3,640)
vid.set(4,480)

while True:
    success,img=vid.read()
    print(success)
    img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video",img)
    cv2.imshow("Video",img_grey)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

vid.release()
cv2.waitKey()
cv2.destroyAllWindows()
# %%
vid.release()
cv2.destroyAllWindows()
# %%
impcann=cv2.Canny(img,0,40)
cv2.imshow("Logo",impcann)
cv2.waitKey()
cv2.destroyAllWindows()
# %%
width,heigth=250,300
pts=np.float32([[111,230],[200,120],[154,428],[352,440]])
pts2=np.float32([[0,0],[width,0],[0,heigth],[width,heigth]])
matrix=cv2.getPerspectiveTransform(pts,pts2)
imgout=cv2.warpPerspective(img,matrix,(width,heigth))
cv2.imshow("Logo",imgout)
cv2.imshow("Logo",img)
cv2.waitKey()
cv2.destroyAllWindows()

# %%
# %%

cv2.namedWindow("Tracker")


# %%

cv2.line(img,(0,0),(450,450),(0,0,255),5)
cv2.circle(img,(250,340),240,(0,0,255))
cv2.rectangle(img,(15,25),(800,650),(0,0,255),5)
pts=np.array([[11,11],[320,330],[3000,330]],np.int32)

cv2.polylines(img,[pts],True,(255,0,255),10)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# %%

events= [i for i in dir (cv2) if 'EVENT' in i ]
print (events)
# %%
def clicked (event,x,y, flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        print("x-->",x,"y-->",y)
        strg=str(x)
        font=cv2.FONT_HERSHEY_DUPLEX
        cv2.circle(img_new,(x,y),1,(0,255,255),3)
        cv2.putText(img_new,strg,(x+100,y+100),font,2,(0,255,0),2)
        cv2.imshow("Image",img_new)
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img_new[x,y,0]
        green=img_new[x,y,1]
        red=img_new[x,y,2]
        font=cv2.FONT_HERSHEY_DUPLEX
        strr=str(blue)+","+str(green)+","+str(red)
        cv2.putText(img_new,strr,(x,y),font,2,(0,255,0),2)
        cv2.imshow("Image",img_new)

img_new=img=cv2.imread(r"C:\Users\siddh\Downloads\maxresdefault.jpg")
cv2.imshow("Image",img_new)
cv2.setMouseCallback("Image",clicked)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
def clicked_line (event,x,y, flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        start=(x,y)
        points.append((x,y))     
        # if event==cv2.EVENT_RBUTTONDOWN:
        #     end=(x,y)       
        
img_new1=img=cv2.imread(r"C:\Users\siddh\Downloads\maxresdefault.jpg")
points=[]
cv2.imshow("Image_new",img_new1)
cv2.setMouseCallback("Image_new",clicked_line)

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
