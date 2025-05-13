# Node.jsの公式イメージをベースに使用
FROM node:20-alpine

# 作業ディレクトリを設定
WORKDIR /app

ADD ./frontend /app

# 依存関係のインストール
RUN npm install

# 開発サーバーを起動
CMD ["npm", "run", "dev"]