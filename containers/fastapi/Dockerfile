FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# 必要なパッケージのインストール
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# ソースコードをコピー
COPY backend/app /app/

# Poetry のインストール
RUN pip install --no-cache-dir poetry==1.8.4

# 仮想環境をプロジェクトディレクトリ内に作成するように設定
RUN poetry config virtualenvs.in-project true

# pyproject.tomlのみ先にコピー
COPY backend/app/pyproject.toml ./

# Poetry による依存関係インストール
RUN poetry install --no-root


# 開発サーバーを起動
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]