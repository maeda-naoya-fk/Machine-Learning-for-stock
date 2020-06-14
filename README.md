# 株価予測のための機械学習

# Description
目的株価(target_number)を説明変数(prepare_number)を用いて、次の日の株価が上がるか下がるかを予想する。機械学習には決定木を用いている。  
また、単に予想するだけではなく、テスト用と学習用の正解率、それらの説明変数がどれくらい予想に影響しているか(coefficint)、データ数を出せる。  
**どの組み合わせが一番よい結果が出せたか調べて教えてください。**

# Usage

config.iniをいじれば単に次のコードを打てばオーケー。  　　
  
`python3 main.py`　　
  
 jupyter入れてるならexample.ipynbをつかってみてください。　　

# Explain config.ini

- start:いつからの株価を取得するか
- finish:いつまでの株価を取得するか
- target_number:予測したい株価
- prepare_number:説明変数
- hedears:ヘッダーの取得方法はここのサイトを見てください(https://note.nkmk.me/python-beautiful-soup-scraping-yahoo/)
- model_k:株価の次の日の値が上下何%で変動するか
- max_depth:機械学習をする際にどのくらいの階層まで掘り下げるか
- test_size:テスト用と学習用でどのくらいの比率で分けるか

# Requirement

pythonのversionは3.7.7で書いてます。３以降だったら動くはずです。　　
- numpy(=1.18.1)
- sklearn(=0.22.1)
- pandas(=1.0.3)
- requests(=2.23.0)
- bs4(=4.8.2)
- json(=2.0.9)

