#!/usr/bin/env bash

# 必要なパッケージをインストール（←これが超重要）
pip install --upgrade pip
pip install -r requirements.txt

# マイグレーション処理
python manage.py makemigrations
python manage.py migrate

# 初期データ投入 ← ここを修正！
python manage.py load_initial_data

# 静的ファイルを収集
python manage.py collectstatic --no-input
