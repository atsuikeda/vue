# MySQLの公式イメージをベースに使用
FROM mysql:8.0

# タイムゾーンの設定
ENV TZ=Asia/Tokyo

# カスタム設定ファイルをコピー
COPY ./mysql/conf.d/my.cnf /etc/mysql/conf.d/

# 初期化SQLをコピー
COPY ./mysql/init/ /docker-entrypoint-initdb.d/

# 必要なパッケージのインストール（必要な場合）
RUN apt-get update && apt-get install -y \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# 権限の設定
RUN chown -R mysql:mysql /var/lib/mysql

# ポートを公開
EXPOSE 3306

# ヘルスチェック
HEALTHCHECK --interval=10s --timeout=5s --retries=5 \
    CMD mysqladmin ping -h localhost -u root -ppassword || exit 1