# Node.jsの公式イメージをベースに使用
FROM node:20-alpine

# 作業ディレクトリを設定
WORKDIR /app

# 必要なビルドツールをインストール
RUN apk add --no-cache python3 make g++

# package.jsonをコピー
COPY frontend/package.json ./

# クリーンインストールを実行
RUN rm -rf node_modules package-lock.json && \
    npm install --legacy-peer-deps

# ソースコードをコピー
COPY frontend/app ./

# 開発サーバーを起動（ホスト設定を追加）
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]