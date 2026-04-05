# AtCoder Algorithm Rating

![AtCoder Algo Rating](https://atcoder-disp-graph.tra.earth/disp-rate/hasiyuto?contest-type=algo&graph-type=status)
![AtCoder Algo Graph](https://atcoder-disp-graph.tra.earth/disp-rate/hasiyuto?contest-type=algo&graph-type=graph)

# AtCoder workspace

VSCode + Python + atcoder-cli(acc) + online-judge-tools(oj) 環境

# ディレクトリ構成
```
Atcoder/
├── .venv/        # Python仮想環境
├── abc/          # ABCコンテスト
├── arc/          # ARCコンテスト
└── practice/     # Daily Training / 典型問題 / 過去問
```

# よく使うコマンド

仮想環境
```
source .venv/bin/activate
```
コンテスト作成
```
acc new コンテストID
```
問題追加
```
acc add a
```
テスト
```
oj t -c "python main.py"
```
提出
```
acc submit
```


# AtCoder CLI workflow

Python + acc + oj

# 作業開始
```
cd ~/workbench/Atcoder
source .venv/bin/activate
```
# コンテストを解く

① コンテストIDを確認（URLの最後）

例
https://atcoder.jp/contests/abc350
→ abc350

② コンテストフォルダ作成
```
acc new abc350
cd abc350
```
③ 問題Aを準備
```
acc add a
cd a
```
④ コードを書く

main.py を編集

⑤ テスト
```
oj t -c "python main.py"
```
⑥ 提出
```
acc submit
```
# 次の問題
```
cd ..
acc add b
cd b

oj t -c "python main.py"
acc submit
```
# Daily Training（練習問題）

practice に保存
```
cd ~/workbench/Atcoder/practice

acc new adt_easy_20260326_2
cd adt_easy_20260326_2

acc add a
```

# ファイル

main.py
解答を書く

tests/
サンプル入力・出力
