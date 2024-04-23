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

### ブラウザアクセス
#### 管理サイトへログイン
http://127.0.0.1:8000/admin

# 最初のmigrationをする前にカスタムユーザを作成する必要がある。
https://denno-sekai.com/django-customuser-abstractbaseuser/