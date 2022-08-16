#!/bin/bash

cd /mnt/c/Users/16658/Desktop/X-NOTES
CURDIR=$(dirname)
if [ CURDIR = "/mnt/c/Users/16658/Desktop/X-NOTES" ]
then
    echo "####### 进入自己的项目 #######"
fi

make html

DATETIME=$(date "+%Y/%m/%d")

# 执行git命令
git add .
git commit -m "$DATETIME"
echo "####### commit #######"
git remote set-url origin https://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/Auroraol/notes-cookbook.git\
echo "####### 开始推送 #######"
git push

# 删除缓存
rm -rvf /usr/local/nginx/html/blog/runtime/cache

echo "####### 推送成功 #######"