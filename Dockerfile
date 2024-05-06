# python:3.12.0の公式 image をベースの image として設定
FROM python:3.12.0

# 作業ディレクトリの作成
RUN mkdir /app

# 作業ディレクトリの設定（以後の RUN は WORKDIR で実行）
WORKDIR /app

# カレントディレクトリにある資産をコンテナ上の指定のディレクトリにコピーする
COPY . /app

# pipでrequirements.txtに指定されているパッケージを追加する
RUN pip install -r requirements.txt