# miccle

<a href="https://github.com/biki-cloud/miccle-django-app/actions?query=workflow%3ATest" target="_blank"><img src="https://github.com/biki-cloud/miccle-django-app/workflows/Test/badge.svg" alt="Test"></a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/biki-cloud/miccle-django-app" target="_blank"><img src="https://coverage-badge.samuelcolvin.workers.dev/biki-cloud/miccle-django-app.svg" alt="Coverage"></a>


## 概要
イベント出店者とイベント主催者をつなぐマッチングアプリ

| 役割      | 名称        |
|---------|-----------
| イベント主催者 | organizer |
| イベント出店者 | vendor    |
| イベント参加者 | customer  |

## 開発について

### DB情報のリセット
```bash
# 以下のように環境変数をセット
$ cat .env
DJANGO_SUPERUSER_EMAIL=<アドミンユーザのemail>
DJANGO_SUPERUSER_PASSWORD=<アドミンユーザのパスワード>
EMAIL_HOST=<xxxx>
EMAIL_HOST_USER=<xxxx>
EMAIL_HOST_PASSWORD=<xxxx>

# 環境変数を読み込む
$ source .env

# DBのリセットスクリプトを実行
$ ./scripts/db_reset.sh
```

#### EC2インスタンスで起動
```bash
# EC2インスタンスにログイン
$ ssh ec2
$ cd miccle-django-app
$ git stash -u
$ git pull origin main
$ docker-compose -f docker-compose-local.yaml down
$ docker-compose -f docker-compose-local.yaml up --build
$ docker exec -it miccle bash
# 正常に実行することを確認
$ ./reset_db.sh
# コンテナを抜ける
$ exit
# 正常に起動することを確認
$ docker-compose -f docker-compose-local.yaml up
# バックグラウンドで起動させておく
$ docker-compose -f docker-compose-local.yaml up -d
# ec2を抜ける
$ exit
```

### ブラウザアクセス

#### ホーム画面

http://127.0.0.1:8000/events

#### 管理サイトへログイン

http://127.0.0.1:8000/admin

## pre-commit
```bash
# .pre-commit-config.yamlをローカルリポジトリに読み込ませる。
# git commitすると自動で実行できるようになる。
$ pre-commit install
# 解除
$ pre-commit uninstall
```

## pytest E2E 事前準備 & テストコード作成
```bash
# ブラウザのインストール（chromium,firefox,webkit等）
$ playwright install

# Webサーバの起動（別ターミナルで）
$ python manage.py runser

# サンプルテストコードを作成
$ playwright codegen http://127.0.0.1:8000/ -o e2e/test_sample.py
```

## 環境構築
```bash
$ python3 -m venv venv
$ pip install -r requirements.txt
```
またはdockerコンテナを構築

# 参考ドキュメント

## Djangoについて
- [【Django】データベースを初期化する方法【リセット】 | アントレプレナー](https://kosuke-space.com/django-migration-reset)
- [Djangoでcreatesuperuserを自動化したいときに使えるオプション(--noinput) - delhi09の勉強日記](https://kamatimaru.hatenablog.com/entry/2021/02/28/030646)
- [18.Djangoアプリでログイン時だけ投稿・編集を可能にしてみよう](https://denno-sekai.com/django-loginrequiredmixin/)
- [【ソースコード付き】Django SNS アプリの作り方｜Shogo Saito](https://note.com/saito_pythonista/n/n6550f5c2a07b)
- [EC2 amazon linux2 rootにスイッチする方法を検証してみた #AWS - Qiita](https://qiita.com/gama1234/items/23b8397d66a890771866)
- [はじめてのDjango (7) 画像データの管理やページへの表示，アップロードの方法などについて知ろう #Python - Qiita](https://qiita.com/j54854/items/1f0560142e39d888251c)

## html/cssについて
- [codzsword/sidebar-bootstrap](https://github.com/codzsword/sidebar-bootstrap/tree/main)
- [Explore and Download 8400+ Essential SVG Icons - Line icons](https://lineicons.com/icons)

## 認証について(allauth)
- [Djangoでdjango-allauthとCustomUserを使った認証機能を作成](https://zenn.dev/kei_h74/articles/31faae563f7354)
- [Django Allauth: The complete django-allauth guide - DEV Community](https://dev.to/gajesh/the-complete-django-allauth-guide-la3)
  - [django-experiments/allauthdemo at master · gajeshbhat/django-experiments](https://github.com/gajeshbhat/django-experiments/tree/master/allauthdemo)
- allauthでhtmlをカスタムする際はvenv/allauth/templates/accountに配置されているhtmlを持ってきてbase.htmlを修正して配置する。もしくはこの辺: https://github.com/pennersr/django-allauth/blob/main/allauth/templates/account/logout.html

### メール送信
- [2024年最新版 - DjangoからGmailを送信 #Python - Qiita](https://qiita.com/OzWay_jon/items/cf16429cd7f64ff8670d)
- [[Django] Gmailを送信する設定](https://zenn.dev/wtkn25/articles/django-gmail)
- [Googleのアプリパスワード（App passwords）が見つからない時の対処法 #JavaScript - Qiita](https://qiita.com/morima/items/58c51f7a35af2ed80050)

## pre-commit
- [pre-commitでコミット時にコードの整形やチェックを行う](https://zenn.dev/yiskw713/articles/3c3b4022f3e3f22d276d)

## テスト
- [E2Eテスト（ブラウザ画面テスト）｜テストコードのすすめ（Django編）](https://zenn.dev/hideoamezawa/books/study_testcode/viewer/6_e2e_test)
- [Writing tests | Playwright Python](https://playwright.dev/python/docs/writing-tests)


# TODO
- バックアップ機能
- vendorやorganizerを検索するための機能作成
- 共有ボタン
- EDIT,detailするときにとりあえずかっこいい画面を設定したい。手軽に
- ソーシャルログイン機能
