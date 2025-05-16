# MySQLの公式イメージをベースに使用
FROM mysql:8.0

# タイムゾーンの設定
ENV TZ=Asia/Tokyo

# データディレクトリの初期化
RUN mkdir -p /var/lib/mysql && \
    chown -R mysql:mysql /var/lib/mysql && \
    chmod 750 /var/lib/mysql

# 初期化スクリプトのコピーと権限設定
COPY containers/mysql/init/init.sql /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/init.sql