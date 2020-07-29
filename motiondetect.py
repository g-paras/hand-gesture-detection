import cv2
import math
import pyautogui
cap=cv2.VideoCapture(0)
hand_cascade=cv2.CascadeClassifier("rpalm.xml")
a1,b1 = 0,0
p,q=639,479
while True:
	ret,frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	hands=hand_cascade.detectMultiScale(gray,1.2,5)
	#cv2.rectangle(frame,(0,0),(639,479),(0,255,0),2)
	for x,y,w,h in hands:
		a, b = (x+w//2,y+h//2)
		dis = math.sqrt((a-a1)**2 + (b-b1)**2)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)     
		cv2.circle(frame,(a, b),2,(225,0,0),2)
		if dis>80:
			if a<639*3/8:
				print('left')
			elif a>339:
				print('right')
			elif b<479*3/4.4:
				print('jump')
			elif b>149:
				print('scroll')
		a1,b1=a,b
	'''	diff_x,diff_y=((next_x-prev_x),(next_y-prev_y))
		if diff_x>30:
			print("left")
			pyautogui.press('left')
		elif diff_x<-30:
			print("right")
			pyautogui.press('right')
		if diff_y>30:
			print("down")
			pyautogui.press('down')
		elif diff_y<-30:
			print("up")
			pyautogui.press('up')'''
	cv2.imshow("Frame",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

