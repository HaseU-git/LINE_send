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
message_coordinate = [643, 876]
friend_coordinate = [350, 31]
profile_coordinate = [89, 430]
search_coordinate = [111, 134]
select_coordinate = [184, 248]

# 現在のマウスの座標を取得する
print(pyautogui.position())

def launch_whatsapp():
    # アルフレッドを呼び出す
    pyautogui.keyDown("command")
    pyautogui.keyDown("space")
    pyautogui.keyUp("space")
    pyautogui.keyUp("command")
    
    # Whatsappを起動する
    pyperclip.copy("whatsapp")
    pyautogui.hotkey('command', 'v')
    pyautogui.press("enter")
    
    # Whatsapp起動をまつ
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
    # 新規チャット欄（友達欄）をクリック
    pyautogui.moveTo(friend_coordinate[0], friend_coordinate[1])
    pyautogui.click()
    time.sleep(0.2)
    
    # 検索欄をクリック
    pyautogui.moveTo(search_coordinate[0], search_coordinate[1])
    pyautogui.click()
    
    # メッセージを送りたい人の文字列を入力
    pyperclip.copy(person_name)
    pyautogui.hotkey('command', 'v')
    
    # メッセージを送りたい人を選択
    pyautogui.moveTo(select_coordinate[0], select_coordinate[1])
    pyautogui.click()
    
    # アルフレッドを呼び出す
    pyautogui.keyDown("command")
    pyautogui.keyDown("space")
    pyautogui.keyUp("space")
    pyautogui.keyUp("command")
    
    # 送りたい写真をfinderで呼び出す
    pyperclip.copy("\'" + photo_to_send)
    pyautogui.hotkey('command', 'v')
    time.sleep(1)
    pyautogui.hotkey('command', 'enter')

    time.sleep(1)

    # 送りたい写真をクリップボードにコピーする
    pyautogui.hotkey('command', 'c')

    # finderを閉じる
    pyautogui.hotkey('command', 'w')

    # メッセージ入力欄をクリック
    pyautogui.moveTo(message_coordinate[0], message_coordinate[1])
    pyautogui.click()

    # 写真を送信
    pyautogui.hotkey('command', 'v')
    time.sleep(1)
    pyautogui.press("enter")
    pyautogui.press("enter")

    # 友達欄をクリック
    pyautogui.moveTo(friend_coordinate[0], friend_coordinate[1])
    pyautogui.click()
    time.sleep(0.2)
    
    # 自分のプロフィールをクリック（名前が誤っていた場合に誤送信をしないようにするため）
    pyautogui.moveTo(profile_coordinate[0], profile_coordinate[1])
    pyautogui.click()




def send_message(person_name: str, message_to_send:str):
    # 友達欄をクリック
    pyautogui.moveTo(friend_coordinate[0], friend_coordinate[1])
    pyautogui.click()
    time.sleep(0.2)
    
    # 検索欄をクリック
    pyautogui.moveTo(search_coordinate[0], search_coordinate[1])
    pyautogui.click()
    
    # メッセージを送りたい人の文字列を入力
    pyperclip.copy(person_name)
    pyautogui.hotkey('command', 'v')
    
    # メッセージを送りたい人を選択
    pyautogui.moveTo(select_coordinate[0], select_coordinate[1])
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
    time.sleep(0.2)
    
    # 自分のプロフィールをクリック（名前が誤っていた場合に誤送信をしないようにするため）
    pyautogui.moveTo(profile_coordinate[0], profile_coordinate[1])
    pyautogui.click()
