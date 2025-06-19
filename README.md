# Learning Site

このプロジェクトは、Djangoで構築された学習サイトです。

## 開発環境のセットアップ

### 必要条件
- Python 3.x
- PostgreSQL（開発環境用）

### ローカル開発環境のセットアップ

1. リポジトリをクローン
```bash
git clone [リポジトリURL]
cd learning_site
```

2. 仮想環境を作成して有効化
```bash
python -m venv venv
source venv/bin/activate  # Linuxの場合
.\venv\Scripts\activate   # Windowsの場合
```

3. 依存パッケージをインストール
```bash
pip install -r requirements.txt
```

4. PostgreSQLデータベースを作成
```bash
createdb mysite  # PostgreSQLがインストールされている場合
```

5. 環境変数の設定
```bash
# Linuxの場合
export SECRET_KEY='your-secret-key'
export DATABASE_URL='postgresql://postgres:postgres@localhost:5432/mysite'

# Windowsの場合
set SECRET_KEY=your-secret-key
set DATABASE_URL=postgresql://postgres:postgres@localhost:5432/mysite
```

6. データベースのマイグレーション
```bash
python manage.py migrate
```

7. 開発サーバーの起動
```bash
python manage.py runserver
```

## Renderへのデプロイ方法

このプロジェクトは[Render](https://render.com)へのデプロイに対応しています。

### 方法1: Blueprintを使用したデプロイ（推奨）

1. GitHubにプロジェクトをプッシュ
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. Renderダッシュボードで以下の手順を実行:
   - [Blueprints](https://dashboard.render.com/blueprints)ページに移動
   - 「New Blueprint Instance」をクリック
   - GitHubリポジトリを選択して「Connect」をクリック
   - プロジェクト名を入力して「Apply」をクリック

### 方法2: 手動デプロイ

1. Renderダッシュボードで新しいPostgreSQLデータベースを作成:
   - [Dashboard](https://dashboard.render.com/) → New → PostgreSQL
   - 必要な情報を入力
   - 作成後、内部データベースURLをコピー

2. 新しいWebサービスを作成:
   - [Dashboard](https://dashboard.render.com/) → New → Web Service
   - GitHubリポジトリを連携
   - 以下の設定を行う:
     - Runtime: Python 3
     - Build Command: `./build.sh`
     - Start Command: `python -m gunicorn learning_site.asgi:application -k uvicorn.workers.UvicornWorker`
   - 環境変数を設定:
     - `DATABASE_URL`: コピーしたデータベースURL
     - `SECRET_KEY`: 安全な乱数値
     - `WEB_CONCURRENCY`: 4

### デプロイ後の設定

1. 管理者アカウントの作成:
   - Renderダッシュボードからシェルを開く
   - 以下のコマンドを実行:
     ```bash
     python manage.py createsuperuser
     ```
   - 指示に従って管理者アカウントを作成

## プロジェクト構成

```
learning_site/
  ├── learning_site/      # プロジェクト設定
  ├── lessons/            # レッスンアプリケーション
  ├── build.sh           # Renderビルドスクリプト
  ├── render.yaml        # Render設定ファイル
  └── requirements.txt   # Pythonパッケージ依存関係
```

## 技術スタック

- Django 5.2.3
- PostgreSQL（本番環境）
- Gunicorn + Uvicorn（WSGIサーバー）
- WhiteNoise（静的ファイル配信）

## 注意事項

- 本番環境では必ず`DEBUG=False`になっていることを確認してください
- `SECRET_KEY`は必ず環境変数で設定し、安全な値を使用してください
- データベースのバックアップを定期的に行うことを推奨します