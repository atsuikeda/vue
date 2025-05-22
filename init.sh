#!/bin/sh

# ホスト側のバインド先が存在しない場合は作る
mkdir -p /home/libretranslate/.local/share/libretranslate
mkdir -p /home/libretranslate/.local/share/argos-translate/packages

# 権限も明示（mac環境のbind mountでは重要）
chmod -R 777 /home/libretranslate/.local/share

# LibreTranslate を起動
exec /app/venv/bin/libretranslate --host 0.0.0.0 --port 5000