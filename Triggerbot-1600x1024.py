from os import name
import cv2
import numpy as np
import pyautogui
import keyboard
from pynput.mouse import Controller
from pynput.mouse import Button
from time import sleep, time
from rich import print



if __name__ == "__main__":
    print("""
.######..#####...######...####....####...######..#####...#####....####...######.
...##....##..##....##....##......##......##......##..##..##..##..##..##....##...
...##....#####.....##....##.###..##.###..####....#####...#####...##..##....##...
...##....##..##....##....##..##..##..##..##......##..##..##..##..##..##....##...
...##....##..##..######...####....####...######..##..##..#####....####.....##...
................................................................................
    """)
    
    mouse = Controller()
    
    f_enabled = False
    
    while True:
        
        img = pyautogui.screenshot(region=((795, 507, 4, 4)))
        # print("First IMG: ", img)
        
        img = np.array(img)
        frame = np.array(img).sum()
        
        tm = int(round(time() * 1000))
            
        # print("FRAME: ", frame)
        
         # * Fキーが押されていたら or WASDが押されていたら
        if keyboard.is_pressed("f"):
            print("F or WASDが押されました")
            # * Fキーが押されていてかつWASDが押されてないなら
            if keyboard.is_pressed("f") and not (keyboard.is_pressed("w") or keyboard.is_pressed("a") or keyboard.is_pressed("s") or keyboard.is_pressed("d")):
                print("Fのみが押されました。トリガーを有効にします")
                frame1 = np.array(img).sum()
                
                print("FRAME1: ", frame1)

                if f_enabled == True:
                    f_enabled = False
                else:
                    f_enabled = True
                    
                sleep(0.2)
            else:
                print("Fが押された後に移動したためトリガーを無効にします")
                f_enabled = False
            
        # Fキーが有効な場合 
        if f_enabled:
            # ? frameの色に500以上の変化があったら実行する
            if frame1 > (frame + 2500) or frame1 < (frame- 2500):
                for i in range(10):
                    mouse.click(Button.left)
                sleep(0.2)
                f_enabled = False
                print("トリガーが実行されたため、トリガーを無効にします")
                
            # ? frameの色の変化が50未満でほとんど変化がない場合
            if frame1 > (frame + 50) or frame1 < (frame - 50):
                frame1 = np.array(img).sum()
                
        # * 画像をスケールアップ
        r = 200 / img.shape[1]
        dim = (200, int(img.shape[0] * r))
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        # print("Scal-up IMG: ", img)
        
        # ? RGBに変換
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # print("Converted IMG: ", img)
        cv2.imshow("screenshot", img)
        if cv2.waitKey(1) == ord("q"):
            break
            cv2.destroyAllWindows()