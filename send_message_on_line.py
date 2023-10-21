# -*- coding: UTF-8 -*-
import pyautogui
import pyperclip
import time


## -=-=-=-=-=-==-使用方法メモ-=-=-=-=-=-=-=-=-
## 改行をしたい場合には、\nへの変換が必要
## LINEの特有の文字を利用することはできないが、通常の絵文字であれば利用することができる
## 写真を送る場合には名前を「photo_to_send」などにして、拡張子も合わせる
## アルフレッドがインストールされている必要がある
## LINEとfinderは閉じておく

## 以下にLINEでの各座標を設定する
message_coordinate = [530, 797]
friend_coordinate = [31, 58]
profile_coordinate = [149, 106]
search_coordinate = [138, 54]
select_coordinate = [167, 138]
chat_coordinate = [896, 519]

## 以下に送信内容を設定する
friend_list = [
        "友達の名前1",
        "友達の名前2"
]

message_list = [
        "テストメッセージ1",
        "テストメッセージ2"
]

image_list = [
        "photo_to_send.jpeg",
        "photo_to_send.jpeg"
]


# 現在のマウスの座標を取得する
print(pyautogui.position())

def launch_line():
    # アルフレッドを呼び出す
    pyautogui.keyDown("command")
    pyautogui.keyDown("space")
    pyautogui.keyUp("space")
    pyautogui.keyUp("command")
    
    # LINEを起動する
    pyautogui.write("line")
    pyautogui.press("enter")
    
    # LINEの起動をまつ
    time.sleep(5)
    
    # 画面を最大化
    pyautogui.keyDown("command")
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("option")
    pyautogui.keyDown("m")
    pyautogui.keyUp("m")
    pyautogui.keyUp("option")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("command")
    

def send_photo(person_name: str, photo_to_send: str):
    # 友達欄をクリック
    pyautogui.moveTo(friend_coordinate[0], friend_coordinate[1])
    pyautogui.click()
    
    # 検索欄をクリック
    pyautogui.moveTo(search_coordinate[0], search_coordinate[1])
    pyautogui.click()
    
    # メッセージを送りたい人の文字列を入力
    pyperclip.copy(person_name)
    pyautogui.hotkey('command', 'v')
    
    # メッセージを送りたい人を選択
    pyautogui.moveTo(select_coordinate[0], select_coordinate[1])
    pyautogui.click()
    
    # 喋ったことがない場合には、"chat"のボタンをクリック、喋ったことがある場合は何もない場所をクリック
    pyautogui.moveTo(chat_coordinate[0], chat_coordinate[1])
    pyautogui.click()
    
    # アルフレッドを呼び出す
    pyautogui.keyDown("command")
    pyautogui.keyDown("space")
    pyautogui.keyUp("space")
    pyautogui.keyUp("command")
    
    # 送りたい写真をfinderで呼び出す
    pyautogui.write("\'" + photo_to_send)
    time.sleep(0.5)
    pyautogui.hotkey('command', 'enter')

    time.sleep(0.1)

    # 送りたい写真をクリップボードにコピーする
    pyautogui.hotkey('command', 'c')

    # finderを閉じる
    pyautogui.hotkey('command', 'w')

    # メッセージ入力欄をクリック
    pyautogui.moveTo(message_coordinate[0], message_coordinate[1])
    pyautogui.click()

    # 写真を送信
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    pyautogui.press("enter")

    # 友達欄をクリック
    pyautogui.moveTo(friend_coordinate[0], friend_coordinate[1])
    pyautogui.click()
    
    # 自分のプロフィールをクリック（名前が誤っていた場合に誤送信をしないようにするため）
    pyautogui.moveTo(prifile_coordinate[0], prifile_coordinate[1])
    pyautogui.click()




def send_message(person_name: str, message_to_send:str):
    # 友達欄をクリック
    pyautogui.moveTo(friend_coordinate[0], friend_coordinate[1])
    pyautogui.click()
    
    # 検索欄をクリック
    pyautogui.moveTo(search_coordinate[0], search_coordinate[1])
    pyautogui.click()
    
    # メッセージを送りたい人の文字列を入力
    pyperclip.copy(person_name)
    pyautogui.hotkey('command', 'v')
    
    # メッセージを送りたい人を選択
    pyautogui.moveTo(select_coordinate[0], select_coordinate[1])
    pyautogui.click()
    
    # 喋ったことがない場合には、"chat"のボタンをクリック、喋ったことがある場合は何もない場所をクリック
    pyautogui.moveTo(chat_coordinate[0], chat_coordinate[1])
    pyautogui.click()
    
    # メッセージ入力欄をクリック
    pyautogui.moveTo(message_coordinate[0], message_coordinate[1])
    pyautogui.click()
    
    # メッセージ内容を送信
    pyperclip.copy(message_to_send)
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")

    # 友達欄をクリック
    pyautogui.moveTo(friend_coordinate[0], friend_coordinate[1])
    pyautogui.click()
    
    # 自分のプロフィールをクリック（名前が誤っていた場合に誤送信をしないようにするため）
    pyautogui.moveTo(profile_coordinate[0], profile_coordinate[1])
    pyautogui.click()




## 以下に友達の名前とメッセージの内容を記載する（基本的には、エクセルからのコピペを想定している）

launch_line()

 
index = 0 
while index < len(friend_list):
    send_message(friend_list[index], message_list[index])
    send_photo(friend_list[index], image_list[index])
    index = index + 1
