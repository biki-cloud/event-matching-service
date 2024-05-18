#!/usr/bin/env bash

# スクリプトの実行を中断する条件:
# エラーが発生した場合はスクリプトを終了
set -e
# 各コマンドを実行する際にそのコマンドを表示する
set -x

# 型チェックを実行 (mypy)
mypy .

# Ruffを使用して静的解析と自動修正を実行
ruff check . --fix

# Ruffを使用してコードフォーマットをチェック
ruff format .

# 再度各コマンドを表示する設定 (冗長だがデバッグ目的)
set -x

# autoflakeを使用して未使用のインポートと変数を削除
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place . --exclude=__init__.py

# blackを使用してコードをフォーマット
black .

# isortを使用してインポートをソート (一括で適用)
isort .

# isortを使用してインポートをソート (単一行に強制)
isort --force-single-line-imports .
