#!/bin/zsh

echo "==============================="
echo "初始化 Git 仓库..."
git init

echo "==============================="
echo "创建 README 文件..."
echo "# Multi-Language-Task-Performance-Testing" > README.md

echo "==============================="
echo "添加所有文件..."
git add .

echo "==============================="
read "commit_msg?请输入提交信息（默认：first commit）："
if [ -z "$commit_msg" ]; then
  commit_msg="first commit"
fi

echo "提交中..."
git commit -m "$commit_msg"

echo "==============================="
echo "切换分支为 main..."
git branch -M main

echo "==============================="
echo "绑定远程仓库..."
git remote add origin https://github.com/WenBo-Xing/Multi-Language-Task-Performance-Testing.git

echo "==============================="
echo "正在推送到 GitHub..."
git push -u origin main

echo "==============================="
echo "✅ 上传完成！"
