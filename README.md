# 処理内容

Opencvで取得した画像のフーリエ変換・逆変換をリアルタイムに行う

まず取得した画像をnp.fft.fft2()でフーリエ変換し、np.fft.fftshift()で入れ替えを行った後、振幅スペクトルを計算

左クリックが押されている間マウスの座標を取得し、その点の空間領域での波形を下段右側に、再構成した空間領域での画像を下段左側に表示している

# 実行の仕方

Anaconda promptで python capture.py を実行


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

スムーズに再構成するために、マウスで指定した座標周辺の3×3画素を同時に再構成するようにしてある。

何種類か別のプログラムを考え動作が軽くなるように模索したが、期待していたほど軽くなるものが見つからなかった。
