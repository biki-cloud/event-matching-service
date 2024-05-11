# miccle
## 概要
イベント出店者とイベント主催者をつなぐマッチングアプリ

| 役割      | 名称        |
|---------|-----------
| イベント主催者 | organizer |
| イベント出店者 | vendor    |
| イベント参加者 | customer  |

## 開発について

### アプリケーションの作成

```bash
$ python manage.py startapp <app name>
```

### マイグレーションについて

#### マイグレーションを作成

```bash
$ python manage.py makemigrations
```

#### マイグレーションを実行

```bash
$ python manage.py migrate
```

#### マイグレーションのスクリプト

```bash
$ ./migrations.sh
```

## DBについて

### sqliteにてテーブルを確認

```bash
$ sqlite3 db.sqlite3
# テーブル一覧を表示
sqlite> .tables

# テーブルの情報を表示
sqlite> select * from <table name>;

# テーブルを抜ける
sqlite> .exit
```

### DBのリセット

#### 環境変数をセット
```bash
# 以下のように環境変数をセット
$ cat .env
DJANGO_SUPERUSER_EMAIL=<アドミンユーザのemail>
DJANGO_SUPERUSER_PASSWORD=<アドミンユーザのパスワード>
ORIGIN_DOMAIN=<オリジンのドメイン>

# 環境変数を読み込む
$ source .env
```

#### 1. スーパユーザのemailとパスワードを設定

- secrets/admin_email.txtにemailを記載
- secrets/admin_password.txtにパスワードを記載
  ※作成されている場合は不要

#### 2. DBのリセットスクリプトを実行

```bash
$ ./db_reset.sh
```

### ブラウザアクセス

#### ホーム画面

http://127.0.0.1:8000

#### 管理サイトへログイン

http://127.0.0.1:8000/admin

# 参考ドキュメント

- [Djangoでカスタムユーザーを作ってみよう【AbstractBaseUser】](https://denno-sekai.com/django-customuser-abstractbaseuser/)
- [【Django】データベースを初期化する方法【リセット】 | アントレプレナー](https://kosuke-space.com/django-migration-reset)
- [Djangoでカスタムユーザーを作ってみよう【AbstractBaseUser】](https://denno-sekai.com/django-customuser-abstractbaseuser/)
- [Djangoでcreatesuperuserを自動化したいときに使えるオプション(--noinput) - delhi09の勉強日記](https://kamatimaru.hatenablog.com/entry/2021/02/28/030646)
- [18.Djangoアプリでログイン時だけ投稿・編集を可能にしてみよう](https://denno-sekai.com/django-loginrequiredmixin/)
- [【ソースコード付き】Django SNS アプリの作り方｜Shogo Saito](https://note.com/saito_pythonista/n/n6550f5c2a07b)
- [EC2 amazon linux2 rootにスイッチする方法を検証してみた #AWS - Qiita](https://qiita.com/gama1234/items/23b8397d66a890771866)
- [はじめてのDjango (7) 画像データの管理やページへの表示，アップロードの方法などについて知ろう #Python - Qiita](https://qiita.com/j54854/items/1f0560142e39d888251c)

# TODO

- 出店申請して、確定処理を行う
  - 新たなモデルとフォームが必要そう 
  - イベント参加確定者はみんなから見れる
  - イベント申請者はorganizerのみ見れるようにする
- event listで表示する内容
  - organizer
    - 進捗率(あれば, ここまで進んでますよみたいな)
    - 編集ボタン,削除ボタン(編集しつつ削除できる)
  - vendor
    - イベント申請ボタン
  - customer
    - 共有機能(Instagram, LINE, リンクコピー)
  - 共通
    - イベント名
    - 日付
    - 場所
    - イベントジャンル
