#!/usr/bin/env bash

set -e
set -x

# フォーマットチェック
mypy .

# フォーマットチェック
ruff check . --fix

# フォーマット自動修正
ruff format . 