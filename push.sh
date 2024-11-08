#!/bin/bash

# 获取当前日期
current_date=$(date +%Y-%m-%d)

# 如果 $1 为空，则使用当前日期作为默认值
commit_message=${1:-$current_date}

# 执行 git 命令
git add .
git commit -m "$commit_message"
git push
