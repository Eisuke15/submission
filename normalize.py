from sys import stdin,stdout
import pandas as pd
from itertools import product

#読み込み、書き出しが楽なのでpandasを用いた。
df = pd.read_table(stdin, header = None)

#新しいdf用。逐一dataframeにappendすると遅いのでとりあえずリストに格納しておく。
new_df = []

#dfの全ての行を取り出し、第一正規化したものをnew_dfに格納していく。itertuplesはタプルの先頭がインデックスになるため読み捨てている。
for _ , *row in df.itertuples(name = None):

	#取り出した行の要素のうち、コロンで区切られているものを分解している。
	row_elements = list(map(lambda x: str(x).split(':') if not pd.isnull(x) else [x], row))

	#デカルト積をとってリストに格納
	new_df += list(product(*row_elements))

# new_dfをデータフレームに変換し、セパレート文字をTabにして標準出力する。
pd.DataFrame(new_df).to_csv(stdout,sep = '\t',header = False, index = False)
