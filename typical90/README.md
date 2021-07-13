[![oxide](https://img.shields.io/endpoint?url=https%3A%2F%2Fatcoder-badges.now.sh%2Fapi%2Fatcoder%2Fjson%2Foxide)](https://atcoder.jp/users/oxide)
![Twitter Follow](https://img.shields.io/twitter/follow/yu_9824?style=social)
![GitHub followers](https://img.shields.io/github/followers/yu9824?style=social)
# 競プロ典型90問
## このディレクトリは？
[競プロ典型90問](https://atcoder.jp/contests/typical90)のPythonでの解答です．

あくまで自分の解答なのでより良い回答があるかもしれません．  
現時点茶コーダーなので，星4以下を埋めていっています．


## 参考リンク
- 主催者様: [@e869120](https://twitter.com/e869120)
- [企画Twitterスレッド](https://twitter.com/e869120/status/1376089196100653060?s=20)
  - このスレッドに問題等・解説が投稿される．
- [企画Github](https://github.com/E869120/kyopro_educational_90)
  - C++の解答例や詳細な条件？等が記載．
- [AtCoderコンテストページ](https://atcoder.jp/contests/typical90)
  - 実際に提出できる．
- [「競プロ典型90問」非公式難易度表・ソースコード共有](https://docs.google.com/spreadsheets/d/1GG4Higis4n4GJBViVltjcbuNfyr31PzUY_ZY1zh2GuI/edit#gid=0)
  - 企画GithubにはC++だけなので，Pythonのコードを探すなどできる．

### 以下勉強メモ
#### 尺取り法

$O(n^2)$ → $O(n \mathrm{log}\ n)$
- [034.py](./034.py)

- キーワード
  - 広義単調増加関数．

> しゃくとり法は
> 
> - 「条件」を満たす区間 (連続する部分列) のうち、最小の長さを求める
> - 「条件」を満たす区間 (連続する部分列) のうち、最大の長さを求める
> - 「条件」を満たす区間 (連続する部分列) を数え上げる
> 
> といったことを効率良く実現できる手法ですが、「条件」というのが何> でもいいわけではないです。「条件を満たす区間」が以下のいずれかの構造になっている場合には、しゃくとり法を適用することができます:
> 
> - 区間 [left, right) が「条件」を満たすなら、それに含まれる区間> も「条件」を満たす
> - 区間 [left, right) が「条件」を満たすなら、それを含む区間も> 「条件」を満たす

参考: [しゃくとり法 (尺取り法) の解説と、それを用いる問題のまとめ - Qiita](https://qiita.com/drken/items/ecd1a472d3a0e7db8dce)