# miccle
## 概要
イベント出店者とイベント主催者をつなぐマッチングアプリ

| 役割      | 名称        |
|---------|-----------
| イベント出店者 | vendor    |
| イベント主催者 | organizer |
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

# TODO

- vendorがイベントに参加できる機能を追加
- ユーザアカウント情報の編集
    - OrganizerProfileとVendorProfileを編集できるようにする
- イベント参加者がイベントを編集、削除できる状態になっているので解消。
- accountsにvendorとorganizerを紐付けるのはわかるけど、イベント画面のときに現在どっちの役割として操作しているか確認する方法が必要
    - user.get_role()で取得できるようにする
    - 今は一つのアカウントで両方の役割を持てるが、それは管理する上では難しい気がする。
    - vendorとorganizerの両方の役割と持つ人がどれくらいいるのか
    - 方法１：アカウントは一つで、vendorとorganizerの役割を持つ場合、どちらの役割でログインしているかを判別するように機能を追加する
    - 方法２：アカウントを別にして、vendorとorganizerで別々のアカウントでログインしてもらう

- 出店申請して、確定処理を行う