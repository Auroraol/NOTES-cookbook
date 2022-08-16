#!/bin/bash

cd /mnt/c/Users/16658/Desktop/X-NOTES

DATETIME=$(date "+%Y/%m/%d")

# 执行git命令
git add .
git commit -m "$DATETIME"
echo "$DATETIME"
git remote set-url origin https://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/Auroraol/notes-cookbook.git
git push

# 删除缓存
rm -rvf /usr/local/nginx/html/blog/runtime/cache


echo "备份成功"