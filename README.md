# 処理内容

Opencvで取得した画像のフーリエ変換・逆変換をリアルタイムに行うことが目的である

まず取得した画像をnp.fft.fft2()でフーリエ変換し、np.fft.fftshift()で入れ替えを行った後、振幅スペクトルを計算する

左クリックが押されている間、先に定義しておいた関数getPos()でマウスの座標を取得し、その点の空間領域での波形を下段右側に、再構成した空間領域での画像を下段左側に表示する

下段中央のmaskには、すでに再構成された点が白、それ以外が黒い画像が表示される

再構成する際には、np.fft.fftshift()で入れ替えを行った後、np.fft.ifft2()で逆フーリエ変換したものを表示している

# 実行の仕方

Anaconda promptで python ft.py を実行

表示されるウィンドウの再構成したい部分を左クリックしながらなぞると、画像の再構成を実行する

# 依存ライブラリ

・cv2

・numpy

・matplotlib import pyplot

# バージョン

Python 3.7.3

# 参考

・フーリエ変換 - OpenCV-Python Tutorials 1 documentation

http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html

「Numpyを使ったフーリエ変換」で紹介されているプログラムを参考に、フーリエ変換・逆変換を実装

・OpenCVで表示した画像にマウスクリックした場所を取得する方法 (Python)

http://whitecat-student.hatenablog.com/entry/2016/11/09/225631

紹介されているプログラムを引用し、マウスの座標を取得する関数を実装

# 実行の様子

![実行の様子](https://github.com/gucci-999/digital2/blob/master/image.gif)

# 考察

本来は1画素ごとにスムーズに画像を再構成したかったのだが、プログラムが複雑なせいか動作が徐々に重くなり、再構成にとても時間がかかってしまう。

時間をかければ1画素ごとにでも再構成できたが、そのままだとgif動画の時間が長引いてサイズが大きくなってしまうため、マウスで指定した座標周辺の5×5画素を同時に再構成するようにプログラムしてある。

マウスの座標取得の方法や逆フーリエ変換の実装について、異なるプログラムを調べ動作が軽くなるように模索したが、期待していたほど軽くなるものが見つからなかった。

while文を2重で使ったことが動作が重くなった原因かもしれない。
