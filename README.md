# multiprocess-rendering-test

1動画に対して、シングルタスクでレンダリングを行った時の速度測定と
マルチタスクで行った場合について比較して行く。

# python2系について
詳しく書かれた２系の記事が見当たらなかったが、並列処理は、あまり得意ではなかったように思われる。
２系では、並列処理にはmultiprocessingで行われているとする。

# GILとは
Python(のReference ImplementationであるCPython)は、マルチスレッドに対応していますが、スレッドセーフティを確保するためにGIL(Global Interpretation Lock)が存在する。

multiprocessingではこの影響を強く受け、高速化に向いていない。

# concurrent.futures とは

GILによる弊害を考慮し、並列化をうまく行っているライブラリ
3.6あたりから登場したライブラリ。

# テスト
単純なループ、GILの影響を受けるマルチスレッドループ、
GILの影響を受けないで、そのまま流すループを行った