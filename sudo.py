import cv2
import numpy as np
from imutils.object_detection import non_max_suppression
import argparse
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
# load the image, clone it for output, and then convert it to grayscale
img = cv2.imread(args["image"])
x_row = [[600,850], [851,1080], [1081,1350]]
y_row = [[300,450], [451,570], [571,850]]

# Reading the image and the template
#img = cv2.imread('sta_circle.jpg')
#temp = cv2.imread('o_template_1.png')

# save the image dimensions


# Define a minimum threshold
thresh = 0.4
total_box = []
global color_index
color_index = 0
def circleBox(temp, color_index) :
    W, H = temp.shape[:2]
    # Converting them to grayscale
    img_gray = cv2.cvtColor(img,
                            cv2.COLOR_BGR2GRAY)
    temp_gray = cv2.cvtColor(temp,
                            cv2.COLOR_BGR2GRAY)
    # Passing the image to matchTemplate method
    match = cv2.matchTemplate(
        image=img_gray, templ=temp_gray,
    method=cv2.TM_CCOEFF_NORMED)

    # Select rectangles with
    # confidence greater than threshold
    (y_points, x_points) = np.where(match >= thresh)

    # initialize our list of rectangles
    boxes = list()

    # loop over the starting (x, y)-coordinates again
    for (x, y) in zip(x_points, y_points):
        
        # update our list of rectangles
        boxes.append((x, y, x + W, y + H))

    # apply non-maxima suppression to the rectangles
    # this will create a single bounding box
    boxes = non_max_suppression(np.array(boxes))
    # loop over the final bounding boxes
    #print(boxes)
    #print(len(boxes))
    index = 0
    no_lap = 0
    for (x1, y1, x2, y2) in boxes:
        #cv2.rectangle(img, (x1-50, y1-50), (x2-50, y2-50),
        #                (255, color_index * 63, 0), 1)
        #print("x = " + str((x1+x2)/2),end = '')
        #print("y = " + str((y1+y2)/2))
        total_box.append([x1, y1, x2, y2])
        cv2.rectangle(img, (x1-50, y1-50), (x2-50, y2-50),
                    (255, color_index * 63, 0), 1)
        #print([x1, y1, x2, y2])
        #print(img)
        """if checkInclude(boxes[index], index, total_box) :
            #cv2.rectangle(img, (x1-50, y1-50), (x2-50, y2-50),
            #            (255, color_index * 63, 0), 1)
            #total_box.append([x1, y1, x2, y2])
            index += 1
            continue
        else :
            print(boxes[index])
            no_lap += 1"""
        # draw the bounding box on the image
        index = index + 1
    cv2.imwrite(args['image'], img)
    #print("總共偵測到 %d 個圓形" %index)

def checkInclude(check_list, index, boxes) :
    n_index = 0
    #if len(boxes) == 0 :
    #    return False
    for (x1, y1, x2, y2) in boxes:
        if index > n_index : # 比要檢查的還要前面，所以要檢查
            if (x2 >= check_list[0] and x1 <= check_list[0]) and (y2 >= check_list[1] and y1 <= check_list[1]) : # 檢查 x0
                return True
            if (x2 >= check_list[2] and x1 <= check_list[2]) and (y2 >= check_list[3] and y1 <= check_list[3]) : # 檢查 x0
                return True
            if (x2 >= check_list[2] and x1 <= check_list[2]) and (y2 >= check_list[1] and y1 <= check_list[1]):
                return True
            if (x2 >= check_list[0] and x1 <= check_list[0]) and (y2 >= check_list[3] and y1 <= check_list[3]):
                return True
            if (x1 >= check_list[0] and x2 <= check_list[2]) and (y1 >= check_list[1] and y2 <= check_list[3]):
                return True
            
           # n_index += 1
       # else : # 比要檢查的還要後面，所以不要檢查
           # n_index += 1
            #continue
        """while index > n_index:
            if check_list[0] < x1 and check_list[2] > x1:
                return True
            if check_list[0] < x2 and check_list[2] > x2:
                return True
            if check_list[1] < y1 and check_list[3] > y1:
                return True
            if check_list[1] < y2 and check_list[3] > y2:
                return True
            if check_list[0] < x1 and check_list[2] > x2:
                return True
            if check_list[1] < y1 and check_list[3] > y2:
                return True

            n_index += 1"""
        """if index > n_index : # 比要檢查的還要前面，所以要檢查
            if x2 >= check_list[0] and x1 <= check_list[0] : # 檢查 x1
                return True
            if x2 >= check_list[2] and x1 <= check_list[2] : # 檢查 x2
                return True
            if y2 >= check_list[1] and y1 <= check_list[1] : # 檢查 x0
                return True
            if y2 >= check_list[3] and y1 <= check_list[3] : # 檢查 x0
                return True"""
        n_index += 1
    #print(img)
    cv2.rectangle(img, (check_list[0]-50, check_list[1]-50), (check_list[2]-50, check_list[3]-50),
                    (255, color_index * 63, 0), 1)
    return False

#circleBox(cv2.imread('o_template_1.png'))
#circleBox(cv2.imread('x_template_1.png'))
#circleBox(cv2.imread('x_template_2.jpg'))
#circleBox(cv2.imread('circle_test_6.jpg'))


#color_index += 1
#circleBox(cv2.imread('templates/5_5_temp_4.jpg'), color_index)
#color_index += 1
#circleBox(cv2.imread('templates/5_5_temp_7.jpg'), color_index)
#color_index += 1
#circleBox(cv2.imread('templates/5_5_temp_8.jpg'), color_index)
color_index += 1
circleBox(cv2.imread('templates/5_5_temp_9.jpg'), color_index)

"""###

for i in range(1,len(new_total_box)):
    for j in range(i,len(new_total_box)):

###"""

nn = 0
#print("總共有 " + str(len(total_box)))
for i in total_box :
    nn += 1
    center_x = (i[2]+i[0])/2
    center_y = (i[1]+i[3])/2
    x_index = 0
    #print(str(nn) + "號。範圍 " + str(i) + ", 中心 : " + str((i[2]+i[0])/2) + ", " + str((i[3] + i[1])/2))
    for start_x, end_x in x_row :
        y_index = 0
        for start_y, end_y in y_row :
            if (start_x < center_x and end_x > center_x) and (start_y < center_y and end_y > center_y) :
                #print("此圓形在 (" + str(x_index) + ", " + str(y_index) + ")")
                print(str(x_index) + "," + str(y_index) + "$", end ='')
            y_index += 1
        x_index += 1

    #print(str(nn) + "號。範圍 " + str(i) + ", 中心 : " + str((i[2]+i[0])/2) + ", " + str((i[3] + i[1])/2))
new_total_box = []
index_n = 0
for i in total_box :
    #cv2.rectangle(img, (x1-50, y1-50), (x2-50, y2-50),
    #                (255, color_index * 63, 0), 1)
    if not checkInclude(i, index_n, total_box) :
        #print(i)
        #cv2.rectangle(img, (i[0], i[1]), (i[2], i[3]),(255, 255, 0), 1)
        new_total_box.append(i)
    index_n += 1
cv2.imwrite(args['image'], img)
#print((new_total_box))
#print(len(new_total_box))
#circleBox(cv2.imread('circle_game_temp1.jpg'))

# Show the template and the final output
#cv2.imshow("Template", temp)
#cv2.namedWindow("After NMS",0); #创建窗口
#cv2.imshow("After NMS", img)
#cv2.waitKey(0)

# destroy all the windows
# manually to be on the safe side
cv2.destroyAllWindows()
