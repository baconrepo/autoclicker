import pyautogui as pg

##GET SCREEN SIZE
print(pg.size())

##MOVE MOUSE TO POSITION
pg.click()
pg.moveTo(1320,660,duration=4)

##CLICK THE MOUSE
i=1
while i<1000:
    pg.click(1320,711)
    i=i+1
