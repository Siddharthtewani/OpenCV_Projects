#%%
import cv2
import numpy as np 
import datetime
#%%
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
#%%
img_new=img=cv2.imread(r"C:\Users\siddh\Downloads\maxresdefault.jpg")
cv2.imshow("Image",img_new)
cv2.setMouseCallback("Image",clicked)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%