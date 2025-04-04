#!/bin/zsh

# 设置 Git 用户信息（如果没配置）
git config user.name >/dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "🛠️ 检测到未配置 Git 用户信息，正在设置..."
  git config --global user.name "Wenbo Xing"
  git config --global user.email "wenboxing364@gmail.com"
fi

echo "==============================="
echo "📂 添加所有更改..."
git add .

echo "==============================="
read "commit_msg?📝 请输入提交信息（默认：更新）："
if [ -z "$commit_msg" ]; then
  commit_msg="更新"
fi

echo "📤 提交中..."
git commit -m "$commit_msg"

echo "==============================="
echo "🌐 正在通过 SSH 推送到 GitHub..."

# 设置远程仓库为 SSH 地址（防止忘记）
git remote set-url origin git@github.com:WenBo-Xing/Multi-Language-Task-Performance-Testing.git

# 自动判断是否需要设置 upstream 分支
branch=$(git symbolic-ref --short HEAD)
git push --set-upstream origin "$branch" 2>/dev/null || git push

if [ $? -eq 0 ]; then
  echo "==============================="
  echo "✅ 推送成功！你可以去 GitHub 上查看更新啦！"
else
  echo "==============================="
  echo "❌ 推送失败，请检查网络或远程仓库设置。"
fi
