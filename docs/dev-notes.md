# Design Philosophy

软件开发的核心问题是如何将实现复杂度始终控制在可控范围内。

控制复杂度的核心问题是寻找合适的抽象层次。
抽象层次太低，开发者要实现和管理的细节太多，随着功能的逐渐增加会越来越难以驾驭，
且重复造轮子，效果无法与专业工具相比。
抽象层次太高，软件开发变成了搭积木，软件的功能被各个积木的功能所定义和束缚，
难以达到理想的设计目标。

基于上述考虑，donno 不计划将所有笔记管理相关的操作都封装到自身内部。

避免抽象层次太低的场景包括：

* 配置远端代码库：用户需要手工创建远端代码库并 clone 到本地，配置 SSH 密钥等，
  donno 只执行 `git push` 或者 `git pull` 同步代码；

* 格式转换：markdown, mathjax 转换为 HTML 等转换类动作交给专门的转换工具
  （这里选择了 pandoc）处理；

避免抽象层次太高的场景包括：

* 发布 blog 功能没有使用 pelican 等 static site generator，
  保证这部分功能未来的发展有足够的灵活性；

# Publish Blog

## Workflow

如果有 blog local repo，说明已经和 remote repo 同步过，拿到 master branch of local repo 时间，
找出在此之后修改过的 markdown 文件，转换为 html 文件，在 blog local repo 里 commit and push.

如果没有 blog local repo，说明还没有创建 blog remote repo，
此时将所有 markdown 文件转换为 html，提示用户将 blog local repo push 到 remote。

两个主要功能：

* 转换器：将 markdown, mathjax 转换为基于一个可定制模板 (HTML, CSS) 的 HTML 文件；
* 发布到博客：`git push`

