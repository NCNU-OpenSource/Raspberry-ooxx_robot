from subprocess import call, PIPE, run
from time import ctime
from copy import deepcopy
import time

def main() :
    #limit = 18
    limit = 100
    current = 0
    interrupt = 8 # 間隔時間
    each_resolution = [320,240] # 預設解析度
    size = 3
    data = [[0 for i in range(size)]for j in range(size)] # game
    while True :
        resolution = str(each_resolution[0] + (80 * (current-1))) + "x" + str(each_resolution[1] + (80 * (current-1)))
        resolution = "1920x1080"
        print("開始拍攝當前照片，解析度為%s。" %resolution)
        pic_path = mkTxtName() + ".jpg" # make txt name with now time
        call(["fswebcam", "-d", "/dev/video0", "-r", resolution, "--no-banner", "./upload/cam/%s" % pic_path])
        print("開始偵測照片 %s" %pic_path)
        #call(["python3", "opencv_feature.py", "--image", "./upload/cam/" + pic_path])
        #call(["python3", "opencv_feature.py", "--image", "./game2.jpg"])
        #call(["python3", "sudo.py", "--image", "./upload/cam/" + pic_path])
        #call(["python3", "sudo.py", "--image", "./sta_circle.jpg"])
        result = run(["python3", "sudo.py", "--image", "./upload/cam/" + pic_path], stdout=PIPE, stderr=PIPE, universal_newlines=True)
        print("結束偵測當前照片")
        #print(result.stdout)
        result_list = result.stdout.split('$')[:-1]
        #print(result_list)
        data = putResultInData(result_list, data)
        game_result, botplay = playGame(deepcopy(data))
        data = putBotData(data, botplay)
        print(data)
        if game_result == 3 :
            print("平手，遊戲結束")
            break
        elif game_result == 2 :
            print("玩家贏，遊戲結束")
            break
        elif game_result == 1 :
            print("電腦贏，遊戲結束")
            call(["python3", "../Adafruit_Python_PCA9685/examples/robot.py", "-n", str(87)])
            break
        input('是否準備好了？')
        #print("暫停 %d 秒後，繼續偵測" %interrupt)
        #time.sleep(interrupt)

def putBotData(data, botplay) :
    print("電腦要下的布 " + str(botplay))
    if len(botplay) == 0 :
        return ''
    r,c = botplay[0],botplay[1]
    data[r][c] = 1
    if r==0 and c==0:
        function_num = 8
    elif r==0 and c==1:
        function_num = 5
    elif r==0 and c==2:
        function_num = 2
    elif r==1 and c==0:
        function_num = 7
    elif r==1 and c==1:
        function_num = 4
    elif r==1 and c==2:
        function_num = 1
    elif r==2 and c==0:
        function_num = 6
    elif r==2 and c==1:
        function_num = 3
    elif r==2 and c==2:
        function_num=0
    print("執行第 " + str(function_num) + "個cha")
    # 執行畫線
    call(["python3", "../Adafruit_Python_PCA9685/examples/robot.py", "-n", str(function_num)])
    return data

def putResultInData(result_list, data) :
    for i in result_list :
        y =int(i[0])
        x =int(i[2])
        data[x][y] = 2
    return data
    
def mkTxtName() :
    content = ''
    index = 1
    for i in ctime().split(' ') :
        i = i.replace(':', '-') # can not use : as file name
        if (index >= len(ctime().split(' '))) : # last index not add the _
            content += i
            break
        else :
            content += (i + "_") # replace space with _
            index += 1
    return content

def endGame(data):
    for i in range(3): # 判斷橫線
        if data[i][0] != 0 and data[i][0] == data[i][1] == data[i][2]:
            if data[i][0] == 1: # 自己
                return 1
            else: # 對手
                return 2
    for j in range(3): # 判斷直線
        if data[0][j] != 0 and data[0][j] == data[1][j] == data[2][j]:
            if data[0][j] == 1: # 自己
                return 1
            else: # 對手
                return 2
    if data[0][0] != 0 and data[0][0] == data[1][1] == data[2][2]: # 判斷右下斜
        if data[0][0] == 1: # 自己
            return 1
        else: # 對手
            return 2
    if data[2][0] != 0 and data[2][0] == data[1][1] == data[0][2]: # 判斷右上斜
        if data[2][0] == 1: # 自己
            return 1
        else: # 對手
            return 2 
    for i in range(3):
        for j in range(3):
            if data[i][j] == 0:
                return 0 # 還沒結束
    return 3 # 平手

def findSol(size,data):
    # 判斷遊戲結果
    result = endGame(data)
    if result != 0:
        return result,"",data
    emptyPos = []
    myPos = []
    playerPos = []
    for i in range(size): # 先判斷空的位置
        for j in range(size):
            if data[i][j] == 0: # 空的
                emptyPos.append([i,j])
            elif data[i][j] == 1: # 我的
                myPos.append([i,j])
            else: # 對手的
                playerPos.append([i,j])
    myChoose = []
    # 下哪個可以讓自己贏或讓對手贏
    winPos = []
    lossPos = []
    for i in range(len(emptyPos)):
        data1 = deepcopy(data)
        data2 = deepcopy(data)
        data1[emptyPos[i][0]][emptyPos[i][1]] = 1 # 假設我下這裡
        data2[emptyPos[i][0]][emptyPos[i][1]] = 2 # 假設對手下這裡
        if endGame(data1) == 1:
            winPos.append(emptyPos[i])
        if endGame(data2) == 2:
            lossPos.append(emptyPos[i])
    if len(winPos) > 0: # 有可以贏的
        myChoose = [winPos[0][0],winPos[0][1]]
        data[winPos[0][0]][winPos[0][1]] = 1
    elif len(lossPos) > 0: # 不下這裡會讓自己輸
        myChoose = [lossPos[0][0],lossPos[0][1]]
        data[lossPos[0][0]][lossPos[0][1]] = 1
    elif len(myPos) != 0: # 不是第一次下
        # 過濾被擋住的線
        line = [True for i in range(8)]
        line = [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],[[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],[[0,0],[1,1],[2,2]],[[2,0],[1,1],[0,2]]]
        for i in range(len(playerPos)):
            r = playerPos[i][0]
            c = playerPos[i][1]
            if r == c == 1:
                line[1] = line[4] = line[6] = line[7] = False
            if r == c == 0:
                line[0] = line[3] = line[6] = False
            if r == 0 and c == 2:
                line[0] = line[5] = line[7] = False
            if r == 2 and c == 0:
                line[2] = line[3] = line[7] = False
            if r == 2 and c == 2:
                line[2] = line[5] = line[6] = False
            if r == 0 and c == 1:
                line[0] = line[4]  = False
            if r == 2 and c == 1:
                line[2] = line[4]  = False
            if r == 1 and c == 0:
                line[1] = line[3]  = False
            if r == 1 and c == 2:
                line[1] = line[5]  = False
        found = False
        for i in range(len(line)):
            if found == False:
                if line[i] != False: # 有不被擋住的線
                    for j in range(len(line[i])):
                        if line[i][j] in emptyPos:
                            data[line[i][j][0]][line[i][j][1]] = 1
                            myChoose = line[i][j][0],line[i][j][1]
                            found = True
                            break
        if found == False:
            # 剩下隨便選
            myChoose = [emptyPos[0][0],emptyPos[0][1]]
            data[emptyPos[0][0]][emptyPos[0][1]] = 1
    else: # 第一次下
        if data[1][1] == 0:
            data[1][1] = 1
            myChoose = [1,1]
        else:
            myChoose = [emptyPos[0][0],emptyPos[0][1]]
            data[emptyPos[0][0]][emptyPos[0][1]] = 1
    # 判斷遊戲結果
    result = endGame(data)
    return result,myChoose,data

def playGame(data):
    size = 3
    #data = [[0 for i in range(size)]for j in range(size)]
    
    #x = int(input())
    #y = int(input())
    #player = [x,y]
    #data[player[0]][player[1]] = 2 # 寫上對手座標

    result,myChoose,data = findSol(size,data)
    print("------------------")
    for i in range(3):
        for j in range(3):
            if data[i][j] == 2:
                print("O",end=" ")
            elif data[i][j] == 1:
                print("X",end=" ")
            else:
                print(" ",end=" ")
        print()
    print("------------------")
    return result, myChoose
    # 0沒結束, 1機器人贏, 2玩家贏, 3平手

main()
