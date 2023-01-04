<h1>無情的圈圈叉叉機械手</h1><br>
  <h2><b>簡介：</b></h2>
  <h4>使用webcamera拍攝紙上的情況，經由raspberry pi辨識圈叉，並計算出要畫叉的位置，最後用機械手臂在紙上畫上叉叉</h4><br>
<h2><b>硬體設備：</b></h2>
  <h4>Raspberry pi 3、便宜實惠的機械手臂(要自己組裝!!!)、3顆sg90伺服馬達、PCA for raspberry pi 、webcamera、墊webcamera的盒子(長寬高)、一張特殊規格的A4紙、一隻水分和軟硬度適合的筆</h4><br>
<h2><b>軟體套件：</b></h2>
  <h4>opencv、adafruit、python3、</h4><br>
  安裝指令
  opencv: sudo apt install opencv
  adafruit: sudo apt install adafruit
  python3: sudo apt install python3 (3.9.2)
<h2><b>硬體安裝<b></h2>
  0. raspberry pi環境安裝
    影片
  1. 組裝機器手
    影片
  2. 把PCA插到raspberry pi上(用力!!!)
  3. 3顆sg90馬達依照對應的顏色(黑G紅V黃S)插到PCA上的針腳
  4. 把筆固定在機械手前面的爪子上
  5. 完成！
<h2><b>程式碼<b></h2>


<h2><b>繪製場地</b></h2>
  在一張A4的空白紙上照著下圖的規格繪製場地(一定要畫準，因為我們對精準度非常要求!)
  繪製場地後，將機器手基座對準紙張左上角的點點、墊webcamera的盒子放在右下角"box"點點的右方3cm處，再把webcamera固定在盒子上


執行程式碼: python3 execute.py
