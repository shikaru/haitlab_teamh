# haitlab_teamh

## 環境設定

[openvino のインストール方法](https://qiita.com/ammo0613/items/a9bb3b7f20dc02a8d758)

[インテルの学習済みモデルを使った顔検出](https://jellyware.jp/openvino/#04)

[openvino での補足設定](https://jellyware.jp/kurage/openvino/c07_ie_emotion.html)

[openvino での補足設定](https://jellyware.jp/kurage/openvino/c08_face_detection.html)

これらのサイトの通りに openvino というソフトをインストールすれば、基本的には動作します。

## 使用方法

ダウンロードしたディレクトリで以下を実行する

```
python app.py
```

localhost:8000 もしくは、ターミナル上で表示された URL に飛ぶとホームページに移動する。

ホームページの左上の Processing から自動モザイク処理のページに移動し、モザイク処理をしたいファイルを選択する。

ファイルの選択を終え、モザイク処理ボタンを押すと、瞬時にモザイク処理が完了する。
