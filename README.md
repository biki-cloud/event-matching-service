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
#### 1. パスワードを設定
password.txtにsuperuserのパスワードを設定

#### 2. DBのリセットスクリプトを実行
```bash
$ db_reset.sh
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