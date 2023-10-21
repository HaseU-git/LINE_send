# LINE一斉送信の自動化スクリプト

## 動作環境
* MacOS
* Alfred 4.6.2
* Python 3.9.7
* LINE ver 7.7.0.2698
* pyperclip 1.8.2
* PyAutoGUI 0.9.54

## 環境構築

```
pip install -r src/requirements.txt
```

## 座標設定
以下の座標を`send_message_on_line.py`にて設定する

### message_coordinate
<img width="1552" alt="message_coordinate" src="https://github.com/HaseU-git/LINE_send/assets/64348058/ff14d55c-3954-4768-9a50-0f0cc64b9c0c">


### friend_coordinate
<img width="1552" alt="friend_coordinate" src="https://github.com/HaseU-git/LINE_send/assets/64348058/d983a73a-de12-4bdb-b0a5-55fb324a9d67">


### profile_coordinate
<img width="1552" alt="profile_coordinate" src="https://github.com/HaseU-git/LINE_send/assets/64348058/3a3a1273-66a5-49fc-8e54-f22597353b92">


### search_coordinate
<img width="1552" alt="search_coordinate" src="https://github.com/HaseU-git/LINE_send/assets/64348058/d678bd18-21c0-4050-b82d-5837d8bba197">


### select_coordinate
<img width="1552" alt="select_coordinate" src="https://github.com/HaseU-git/LINE_send/assets/64348058/88163f07-aee2-4f29-a1f7-7d69c901b7f8">


### chat_coordinate
※ まだチャットしたことのない友達の場合のみ出てくる画面
<img width="1552" alt="chat_coordinate png" src="https://github.com/HaseU-git/LINE_send/assets/64348058/5ea2aa7d-530d-4e06-b746-d55f3a0675c9">


## スクリプト設定
`LINE一斉送信.command`の中の`path`をpythonスクリプトの格納されているフォルダに設定する

`chmod`で実行権限付与もする。また、設定からも実行権限付与が必要な場合がある。
<img width="827" alt="Screenshot 2023-10-22 at 0 58 24" src="https://github.com/HaseU-git/LINE_send/assets/64348058/8eff13ac-901f-4871-807b-1f0fb18768ee">


## 送信内容設定

改行文字を元にリストを作成しているので、エクセルで縦に並べたものをコピペしてくるイメージ。
<img width="395" alt="Screenshot 2023-10-22 at 1 03 26" src="https://github.com/HaseU-git/LINE_send/assets/64348058/e7c7f11b-7591-48eb-8ee9-40d3c58b9ffc">

なお、改行はエクセルの置換機能などで`\n`に変更しておくこと。また、写真を1人だけ送らないなどのために1人だけ空白にしたりするとエラーが起こるので空白のセルは含めないようにすること。


