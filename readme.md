<h1>無情的圈圈叉叉機械手</h1><br>
<h1><b>簡介：</b></h1>
  <h4>使用webcamera拍攝紙上的情況(玩家的圈圈)，經由raspberry pi辨識圈圈，並計算出要畫叉的位置，最後用機械手臂在紙上畫上叉叉。</h4><br>
<h2>動機</h2>
  <h4>因為這部<a target="_blank" href="https://www.youtube.com/shorts/E5FjkQiIyA8">OOXX迷因影片</a>讓我們想做一個無情的圈圈叉叉機器人。</h4>
<h2><b>硬體設備：</b></h2>
  <h4>Raspberry pi 3、<a target="_blank" href = "https://shopee.tw/product/4491023/2084598147?smtt=0.321393749-1672830414.4">便宜實惠的機械手臂(要自己組裝!!!)</a>、3顆sg90伺服馬達、<a href = "https://shopee.tw/product/139069730/6518867147" target="_blank">樹梅派專用伺服馬達驅動板</a> 、webcamera、墊webcamera的盒子(長 : 9.5cm，寬：7cm，高：14.5cm)、一張特殊規格的A4紙、一隻白板筆(頭不要太硬的筆都可以)</h4>
<h2><b>軟體套件：</b></h2>
  <h4>OpenCV、Adafruit Python PCA9685、python3、fswebcam</h4><br>
  <b>安裝教學：</b>
  <br/>
  <a target="_blank" href = "https://medium.com/ching-i/%E6%A8%B9%E8%8E%93%E6%B4%BE%E5%AE%89%E8%A3%9D-opencv-4-4-0-606900caf370">OpenCV</a>
  <br/>
  Adafruit Python PCA9685：
  <br/>
  
  ```
  git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
  cd Adafruit_Python_PCA9685
  sudo python setup.py install
  ```
  python3： `sudo apt install python3`
  <br/>
  fswebcam： `sudo apt-get install fswebcam`
<h2><b>硬體安裝<b></h2>
  0. <a target="_blank" href = "https://hackmd.io/@ncnu-opensource/book/https%3A%2F%2Fhackmd.io%2F2j1JjIi_Q4KFgzkRgCZclw%3Fboth">raspberry pi環境安裝</a>
  <br/>
  1. <a target="_blank" href = "https://www.youtube.com/watch?v=xlwTzrsWs48">組裝機器手</a>
  <br/>
  2. 把PCA插到raspberry pi上(不用太用力，因為不用插到最緊也可以用，但太小力根本插不進去)
  <br/>
  3. 3顆sg90馬達依照對應的顏色(黑G紅V黃S)插到PCA上的針腳
  <br/>
  4. 把筆固定在機械手前面的爪子上(我是用橡皮筋綁)
  <br/>
  5. 完成！
<h2><b>程式碼<b></h2>
sudo.py --辨識影像
execute.py --主要程式(判斷遊戲邏輯和結果)
robot.py --控制馬達移動機械手畫叉叉
<h2><b>繪製場地與擺放</b></h2>
  在一張A4的空白紙上照著<a target="_blank" href = "https://github.com/tommygood/Raspberry-ooxx_robot/blob/master/specification.jpg">規格圖</a>的規格繪製場地(一定要畫準，因為我們對精準度非常要求!)<br>
  繪製場地後，將機器手基座對準紙張左上角的點點、墊webcamera的盒子放在右下角"box"點點的右方3cm處，再把webcamera固定在盒子(<a href = "https://github.com/tommygood/Raspberry-ooxx_robot/blob/master/box_up.jpg">長、寬</a>和<a href = "https://github.com/tommygood/Raspberry-ooxx_robot/blob/master/box_side.jpg">高</a>)上
<h2><b>開始玩囉！</b></h2>
  執行程式碼：python3 execute.py
  <br/>
  實際遊玩結果：<a target="_blank" href = "https://drive.google.com/file/d/1t0BdfGBpunlJSryFt57lQvPnwV_Ga7O_/view?usp=sharing">遊玩影片</a>
  <br/>
<h2>遇到困難</h2>
  <b>1. 影像辨識</b>
  <br/>
  原本是要用 feature matching 的方式去抓圓形物體，且也有成功，不過前提是照片畫質要夠。所以當換成用 webcamera 拍照時，畫質不夠就偵測不太準。
  <br/>
  所以後來改成用 template matching 的方式，不過有個問題是因為 webcamera 放置的角度不是垂直地由上而下，所以用 template matching 會變成要用很多角度的模板。
  <br/>
  但是如果要用多個模板，就要把重複辨識的圓形過濾掉，理論上不難，但是那天半夜想了老半夜(天)。
  <br/>
  雖然想出來可以用多個模板解決不同角度的問題，不過我之後發現有一個神之模板，可以偵測到全角度的圈圈，所以目前是採用只用單一模板辨識圈圈。
  <br/>
  <b>2. 機械手臂</b>
  <br/>
  <b>2.1</b>
  <br/>
  一開始不知如何把馬達停下來，然後，就有一顆應該是因為這樣燒壞了。
  <br/>
  不過因為我們用不到爪子的引擎，所以就把原本裝在爪子的馬達拆掉，然後和壞掉的馬達互換。
  <br/>
  然後終於裝回去後，發現機械手臂用來栓螺絲的木板鬆掉，讓螺絲沒辦法很緊的鎖進去，所以就算馬達移動的是正確的，但是機械手臂的位置因為鬆鬆的所以會很不穩定，不過我看蝦皮上買此手臂的評價也滿多人反應此問題。
  <br/>
  <b>2.2</b>
  <br/>
  有一天早上我們要繼續做的時候，原本丈量好的機械手臂要畫叉叉的座標都跑掉了，且程式碼完全沒有動。
  <br/>
  然後當我們都準備好要全部重新量座標的時候，不小心讓馬達敲一下地板，就回到之前的狀態了，真是神奇。
  
<h2>工作分配</h2>
  <b>黃瑜楓</b>：圈叉演算法、手臂畫叉叉函式、材料購買、創意發想。
  <br/>
  <b>李維</b>：手臂組裝、維修、創意發想。
  <br/>
  <b>李恩榮</b>：手臂組裝、維修、創意發想。
  <br/>
  <b>蔣馥安</b>：手臂維修、創意發想、材料購買。
  <br/>
  <b>王冠權</b>：影像辨識、手臂畫叉叉函式、程式彙整。
<h2>參考資料</h2>
  <a target="_blank" href = "https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library/tree/master/examples">adafruit driver github</a>
  <br/>
  <a target="_blank" href = "https://www.youtube.com/watch?v=9jcEwn7GzNs&t=132s">驅動板安裝+install adafruit</a>
  <br/>
  <a target="_blank" href = "https://blog.gtwang.org/iot/raspberry-pi-usb-webcam/">fswebcam</a>
  <br/>
  <a target="_blank" href = "https://medium.com/linux-on-raspberry-pi4/raspberry-pi%E5%AE%89%E8%A3%9Dopencv-%E5%AE%89%E8%A3%9D%E7%AF%87-1e6e35051680">opencv</a>
  <br/>
  <a target="_blank" href = "https://docs.circuitpython.org/projects/pca9685/en/latest/api.html">adafruit 教學</a>
  

  
  
