#!/bin/bash

cd /mnt/c/Users/16658/Desktop/X-NOTES

DATETIME=$(date "+%Y/%m/%d")

# 执行git命令
git add .
git commit -m "$DATETIME"
git remote set-url origin https://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@github.com/Auroraol/notes-cookbook.git
git push

# 删除缓存
rm -rvf /usr/local/nginx/html/blog/runtime/cache