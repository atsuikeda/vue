# Node.jsの公式イメージをベースに使用
FROM node:20-alpine

# 作業ディレクトリを設定
WORKDIR /app

# package.jsonとpackage-lock.jsonをコピー
COPY package*.json ./

# 依存関係のインストール
RUN npm install

# ソースコードをコピー
COPY . .

# ビルド
RUN npm run build

# 開発サーバーのポートを公開
EXPOSE 5173

# 開発サーバーを起動
CMD ["npm", "run", "dev"] 