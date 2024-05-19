import webbrowser
import cv2 as cv
import numpy as np
import time,_thread,pyautogui

class nether_class:
    def image_devil(devil_path,threshold=0.8):
        img_rgb=cv.imread('Screenshot (82).png')
        template=cv.imread(devil_path, cv.IMREAD_GRAYSCALE)
        img_gray=cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        w, h=template.shape[::-1]
        res=cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
        loc=np.where( res >= threshold)
        loc_1,loc_2=loc[::-1]
        if len(loc_1)!=0 and len(loc_2)!=0:
            return int(loc_1[0]),int(loc_2[0])
        else:
            return None,None
    class angel_error():
        def truble_shout_1():
            devil_point_1=nether_class.image_devil(devil_path=r'image\Screenshot (87)l.png')
            if (type(devil_point_1[0])==int and type(devil_point_1[1])==int):
                return True
        def truble_shout_2():
            devil_points_1,devil_points_2=nether_class.image_devil(devil_path=r'image\Screenshot (87)w.png'),nether_class.image_devil(devil_path=r'image\Screenshot (87)s.png')
            if (type(devil_points_1[0])==int and type(devil_points_1[1])==int) or (type(devil_points_2[0])==int and type(devil_points_2[1])==int):
                return False
            return True
        
    def devil_truble_shout():
        if nether_class.angel_error.truble_shout_1()==True:
            return"please link your whatsapp with whatsapp web"
        elif nether_class.angel_error.truble_shout_2()==True:
            return "please make show that your browser window is open"
        else:
            return "your internet speed is slow"
    
def main(devil_address,devil_text,devil_count=0):
    #webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(r"Mozilla Firefox\firefox.exe"))
    webbrowser.get().open_new_tab(f"https://web.whatsapp.com/send?phone={devil_address}&text={devil_text}")
    time.sleep(2)
    while True:
        pyautogui.screenshot().save('Screenshot (82).png')
        x,y=nether_class.image_devil(r'image\Screenshot (82)w.png'),nether_class.image_devil(devil_path=r"image\Screenshot (82)b.png")
        time.sleep(1)
        if (type(x[0])==int and type(x[1])==int):
            pyautogui.click(x[0],x[1])
            return "sended.."  
        elif(type(y[0])==int and type(y[1])==int):
            pyautogui.click(y[0],y[1])
            return "sended.."   
        else:
            print("loading..")
            if devil_count>=5:
                print(nether_class.devil_truble_shout())
                devil_count=0
            devil_count+=1
        
if __name__=="__main__":
    print(main("phone_number","message"))
