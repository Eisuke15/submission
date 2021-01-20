from sys import stdin,stdout
import pandas as pd

#読み込み、書き出しが楽なのでpandasを用いた。
df = pd.read_table(stdin, header = None)

#inが速いので辞書型を用いる。keyが一列目、valueが二列目。
new_df = {}

#dfの全ての行を取り出し、一行目をkeyとしてnew_dfに格納していく。itertuplesはタプルの先頭がインデックスになるため読み捨てている。
for _ , key, value in df.itertuples(name = None):

	#欠損値の場合、空文字列にする。
	if pd.isnull(value): value = ''

	#keyが辞書にない場合、valueを追加
	if key not in new_df:
		new_df[key] = value

	#辞書にある場合、コロンで区切ってvalueを追加
	else:
		new_df[key] += ':'+value

# new_dfをデータフレームに変換し、セパレート文字をTabにして標準出力する。
pd.DataFrame(new_df.items()).to_csv(stdout,sep = '\t',header = False, index = False)
