<h1>無情的圈圈叉叉機械手 Heartless ooxx machine</h1><br>
<h2>動機發想 (Concept Development) </h2>
  <h4>看了網路上的<a target="_blank" href="https://www.youtube.com/shorts/E5FjkQiIyA8">OOXX迷因影片</a>這部影片後，我們這組想做一個無情的圈圈叉叉機器人。玩家在紙上畫圈圈後，這個機器人會使用webcamera拍攝紙上的情況(玩家的圈圈)，再經由raspberry pi辨識圈圈，然後計算該把叉叉下在哪裡才更有機會贏玩家，最後機械手臂會在紙上畫上叉叉，一來一往完成比賽。
 </h4>
  
<h2><b>硬體設備 (Implementation Resources) </b></h2>
<ul>
  <li><h4>Raspberry pi 3</h4></li>
  <li><h4><a target="_blank" href = "https://shopee.tw/product/4491023/2084598147?smtt=0.321393749-1672830414.4">便宜實惠的機械手臂(要自己組裝!!!)</a></h4></li>
  <li><h4>3顆sg90伺服馬達</h4></li>
  <li><h4><a href = "https://shopee.tw/product/139069730/6518867147" target="_blank">樹梅派專用伺服馬達驅動板</a> </h4></li>
  <li><h4>webcamera </h4></li>
  <li><h4>用來墊webcamera的紙盒(長 : 9.5cm，<a href = "https://github.com/tommygood/Raspberry-ooxx_robot/blob/master/box_up.jpg">寬</a>：7cm，<a href = "https://github.com/tommygood/Raspberry-ooxx_robot/blob/master/box_side.jpg">高</a>：14.5cm) </h4></li>
  <li><h4>一張特殊規格的A4紙 </h4></li>
  <li><h4>一隻黑色奇異筆和一隻紅色白板筆 (頭不要太硬的筆都可以) </h4></li>
  <li><h4>很多橡皮筋 </h4></li>
</ul>

<h2><b>軟體架構 (Existing Library/Software)</b></h2>
<ul>
  <li><h4>OpenCV</h4></li>
  <li><h4>Adafruit Python PCA9685</h4></li>
  <li><h4>python3</h4></li>
  <li><h4>fswebcam</h4></li>
</ul>

<h2><b>前置下載 (Installation) </b></h2>
  <br/>
  1. <a target="_blank" href = "https://medium.com/ching-i/%E6%A8%B9%E8%8E%93%E6%B4%BE%E5%AE%89%E8%A3%9D-opencv-4-4-0-606900caf370">OpenCV</a>
  <br/>
  2. Adafruit Python PCA9685：
  <br/>
  
  ```
  git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
  cd Adafruit_Python_PCA9685
  sudo python setup.py install
  ```
  
  python3： `sudo apt install python3`
  
  <br/>
  
  fswebcam： `sudo apt-get install fswebcam`
  

<h2><b>執行過程 (Implementation Process)<b></h2>
<ul>
  <li><h3>程式碼</h3></li>
  <ul>
  <li><h4>sudo.py --辨識影像</h4></li>
  <li><h4>execute.py --主要程式(判斷遊戲邏輯和結果)</h4></li>
  <li><h4>robot.py --控制馬達移動機械手畫叉叉</h4></li>
  </ul>
  
  <li><h3>硬體準備</h3></li>
  <ol>
  <li><a target="_blank" href = "https://hackmd.io/@ncnu-opensource/book/https%3A%2F%2Fhackmd.io%2F2j1JjIi_Q4KFgzkRgCZclw%3Fboth">raspberry pi環境安裝</a></li>
  <li><a target="_blank" href = "https://www.youtube.com/watch?v=xlwTzrsWs48">組裝機器手</a></li>
  <li>把PCA插到raspberry pi上(太小力根本插不進去!但也不用太用力，因為不用插到最緊就可以使用了。)</li>
  <li>把3顆sg90馬達依照對應的顏色(黑G、紅V、黃S)插到PCA上的針腳</li>
  <li>用橡皮筋把筆固定在機械手前面的爪子上(橡皮筋固定筆時要綁緊，因為機器手臂在紙上操作的頗大力，不綁緊的話筆會歪掉，不便操作)</li>
  <li>-> 完成！</li>
  </ol>
  
  <li><h3>場地布置</h3></li>
  <ul>
  <li><h4>在一張A4的空白紙上照著<a target="_blank" href = "https://github.com/tommygood/Raspberry-ooxx_robot/blob/master/specification.jpg">規格圖</a>的規格繪製場地(一定要畫準，因為我們對精準度非常要求!)</h4></li>
  <li><h4>繪製場地後，將機器手基座對準紙張左上角的點點、墊webcamera的盒子放在右下角"box"點點的右方3cm處，再把webcamera固定在盒子(<a href = "https://github.com/tommygood/Raspberry-ooxx_robot/blob/master/box_up.jpg">長、寬</a>和<a href = "https://github.com/tommygood/Raspberry-ooxx_robot/blob/master/box_side.jpg">高</a>)上
</h4></li>
  </ul>
</ul>


<h2><b>開始玩囉！ (Usage)</b></h2>
  執行程式碼：
  
  `python3 execute.py`
  <br/>
  實際遊玩結果：<a target="_blank" href = "https://www.youtube.com/watch?v=LlVConbf5Gc">遊玩影片</a>
  <br/>
  
<h2>心得反饋&遇到的困難</h2>
<ol>
  <li><h4>影像辨識</h4>
  <br/>
  原本是要用 feature matching 的方式去抓圓形物體，且也有成功，不過前提是照片畫質要夠。所以當換成用 webcamera 拍照時，畫質不夠或是沒對焦到就偵測得不太準。
  <br/>
  所以後來改成用 template matching 的方式，不過有個問題是因為 webcamera 放置的角度不是垂直地由上而下，所以用 template matching 會變成要用很多角度的模板。
  <br/>
  但是如果要用多個模板，就要把重複辨識的圓形過濾掉，理論上不難，但是那天半夜想了老半夜(天)。
  <br/>
  雖然想出來可以用多個模板解決不同角度的問題，不過我之後發現有一個神之模板，可以偵測到全角度的圈圈，所以目前是採用只用單一模板辨識圈圈。
  <br/></li>
  <li><h4>機械手臂</h4></li>
  <ol>
  <li>一開始不知如何把馬達停下來，再加上原本 adafruit 給的頻率太高(它的註解上寫 good for server motor)，不過可能是因為我們是用樹梅派供電，然後，就有一顆應該是因為這樣燒壞了。
  <br/>
  不過因為我們用不到爪子的引擎，所以就把原本裝在爪子的馬達拆掉，然後和壞掉的馬達互換。(材料給了4顆馬達，但我們只會用到3顆)
  <br/>
  然後終於裝回去後，發現機械手臂用來栓螺絲的木板孔鬆掉，讓螺絲沒辦法很緊地鎖進去，所以就算馬達移動位置的是正確的，但是機械手臂的實際位置因為鬆鬆的所以會很不穩定。</li>
  <li>有一天早上我們要繼續做的時候，原本丈量好的機械手臂要畫叉叉的座標都跑掉了，且程式碼完全沒有動。
  <br/>
  然後當我們都準備好要全部重新量座標的時候，不小心讓馬達敲一下地板，就回到之前的狀態了，真是神奇。</li>
  <li>又有一顆馬達卡死，我們把馬達的電都拔掉還是一樣。把馬達拆下來看後，發現它裡面有一帶動大齒輪的小齒輪卡死。
  <br/>
  最大可能的原因是上面提到，一開始我們亂操馬達，可能就有一點秀斗了，所以就算後來正常跑也是會壞掉。</li>
  <li>在更換馬達時，因為機械手臂結構幾乎都是連貫的，需拆解多部份零件，才能找到角度去更換。</li>
  <li>馬達在長時間測試、運作下，功能開始異常，最終導致燒壞卡死。所以我們得出一結論，要避免馬達在高溫情況下運作太久，並且要注意使用壽命。</li>
  </ol>
  <li><h4>程式碼整合</h4>
  影像辨識和遊戲程式在整合時，因為雙方的程式都寫得蠻醜的(尤其是某人寫的函數和變數名稱!!!)，所以整合和debug時弄得非常辛苦QQ，以後合作的話要寫好看點嘿<br/></li>
</ol>
  
<h2>工作分配 (Job Assignment)</h2>
<ul>
  <li><b>黃瑜楓</b>：</li>
  <ul>
  <li>圈叉演算法、手臂畫叉叉函式、材料購買、創意發想。</li>
  </ul>
  <li><b>王冠權</b>：</li>
  <ul>
  <li>影像辨識、手臂畫叉叉函式、程式彙整。</li>
  </ul>
  <li><b>蔣馥安</b>：</li>
  <ul>
  <li>程式彙整、手臂維修、材料購買、創意發想。</li>
  </ul>
  <li><b>李維</b>：</li>
  <ul>
  <li>手臂組裝、維修、創意發想。</li>
  </ul>
  <li><b>李恩榮</b>：</li>
  <ul>
  <li>手臂組裝、維修、創意發想。</li>
  </ul>
</ul>

<h2><b>善用所學 (Knowledge from Lecture) </b></h2>
<ul>
  <li>linux系統基本指令</li>
</ul>
  
<h2>參考資料 (References)</h2>
<ul>
  <li><a target="_blank" href = "https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library/tree/master/examples">adafruit driver github</a></li>
  <li><a target="_blank" href = "https://www.youtube.com/watch?v=9jcEwn7GzNs&t=132s">驅動板安裝+install adafruit</a></li>
  <li><a target="_blank" href = "https://blog.gtwang.org/iot/raspberry-pi-usb-webcam/">fswebcam</a></li>
  <li><a target="_blank" href = "https://medium.com/linux-on-raspberry-pi4/raspberry-pi%E5%AE%89%E8%A3%9Dopencv-%E5%AE%89%E8%A3%9D%E7%AF%87-1e6e35051680">opencv</a></li>
  <li><a target="_blank" href = "https://docs.circuitpython.org/projects/pca9685/en/latest/api.html">adafruit 教學</a></li> 
</ul>
  

  
  
