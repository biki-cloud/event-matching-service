#!/usr/bin/env bash

set -e
set -x

# 単体テスト & カバレッジ取得
coverage run manage.py test
coverage html -d .coverage_report

# e2eテスト
pytest e2e
