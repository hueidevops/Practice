# 安裝Python

Python目前主要分為兩個版本：Python 2與Python 3。

本教學針對Python 3做教學

## Windows環境
1. 到Python官網(www.python.org)下載Windows版的[安裝程式](https://www.python.org/downloads/)，可依自己的作業系統選擇下載32位元或64位元

2. 下載後請執行安裝程式，在安裝畫面中要勾選「Add Python 3.7 to PATH」，安裝程式會正確的設定好環境變數

3. 啟動Python終端對話

    * 安裝Python時，若有勾選「Add Python 3.7 to PATH」，系統就會自動設定好環境變數，這時直接打開命令視窗(cmd)並輸入python，就會出現以下畫面
    
    ![Command](/chapter.1/images/python_cmd.jpg）
    
    * 若輸出以下畫面，代表環境變數沒有設定好
    ```'
    python' 不是內部或外部命令，可執行的程式或批次檔
    ```
4. 在Python終端對話中執行Python程式

在終端對話中輸入以下指令，並確定有看到輸出「Hello World!」

```buildoutcfg
print("Hello World!)
```



## Linux環境