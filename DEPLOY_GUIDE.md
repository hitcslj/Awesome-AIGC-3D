# GitHub Pages 部署指南

## 1. 配置 GitHub Pages

### 步骤

1. 用有权限的 GitHub 账号打开仓库设置页面：
   **https://github.com/hitcslj/Awesome-AIGC-3D/settings/pages**

2. 在 **"Build and deployment"** 区域：
   - **Source**: 选择 `Deploy from a branch`
   - **Branch**: 选择 `v2`
   - **Folder**: 选择 `/docs`
   - 点击 **Save**

3. 等待 1-2 分钟，GitHub Actions 会自动构建并部署

4. 部署完成后，网站地址为：
   **https://hitcslj.github.io/Awesome-AIGC-3D/**

### 验证

- 打开上面的 URL，检查页面是否正常显示
- 检查导航栏滚动效果、Tab 切换、BibTeX 复制按钮是否正常
- 检查所有图片是否加载成功

## 2. 设置默认分支（可选但推荐）

将默认分支从 `main` 改为 `v2`，让访客看到新版 README：

1. 打开 **https://github.com/hitcslj/Awesome-AIGC-3D/settings**
2. 找到 **"Default branch"** 区域
3. 点击切换按钮，选择 `v2`
4. 确认切换

> 注意：`main` 分支保留了学长 v1 的原始 awesome list，不会被删除。

## 3. 更新论文 arXiv 链接（投稿后）

论文上传到 arXiv 后，需要更新两个地方：

### README.md (第 3 行)
```
[![arXiv](https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg)](https://arxiv.org/abs/XXXX.XXXXX)
```

### docs/index.html
- Hero 区域的 Paper 按钮 href（搜索 `href="#" target="_blank" title="Paper (arXiv)"`）
- 将 `href="#"` 替换为 `href="https://arxiv.org/abs/XXXX.XXXXX"`

## 4. 本地预览

在推送前，可以本地预览网页：
- 直接用浏览器打开 `docs/index.html`
- 或启动本地服务器：`python -m http.server 8000 -d docs/`，然后访问 `http://localhost:8000`

## 5. 日常更新流程

```bash
# 确保在 v2 分支
cd "D:\Material_for _All\PEILab\3D_Gen_for_Game_Survey\Awesome-AIGC-3D"
git checkout v2

# 编辑文件后
git add <修改的文件>
git commit -m "更新说明"
git push origin v2

# GitHub Pages 会自动重新部署（约 1-2 分钟）
```

## 6. 文件结构速查

```
docs/
├── index.html              ← 网页主体
└── static/
    ├── css/index.css        ← 样式
    └── images/
        ├── fig1_pipeline.jpg    ← 论文 Fig 1
        ├── fig2_taxonomy.png    ← 分类树图
        ├── fig_open_closed.png  ← 开源vs闭源对比
        └── fig_characters.png   ← 角色方法展示
```
