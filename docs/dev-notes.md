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

# Backup/Restore with Patch File

donno 默认使用 git 库进行多个实例间的同步，但有些非常细微的改动，
不希望出现在版本历史中，或者由于网络原因暂时不能 pull from remote repo，
这时 backup to patch file 提供了一种解决方案。

实现机制是将源实例库（这里记为 S）中未提交的文件打包到 patch file 里，
拷贝/发送到目标实例上，导入到donno repo（这里记为 T）里。

这种同步方式要求S 和 T的 HEAD 必须是同一版本，
为了实现这一点，patch file 的文件名格式为：

donno-<hash>.patch

在 T 上导入 patch 文件时，检查该 patch 文件的 hash 是否与 HEAD 版本的 hash 一致，
如果一致则将 patch 解压到 working tree 上，否则检查 hash 是否为历史版本，
如果是历史版本，说明 S 需要首先同步最新版本库，再创建 patch 文件；
如果 hash 未出现在版本历史中，说明 T 需要首先同步到最新版本，再解压 patch。

前一种情况，提示用户更新 S 库 (pull in S)，
后一种情况，提示用户更新 T 库 (pull in T)。

为了方便用户完成上述操作，donno 提供了 `git` 子命令，
所有 `git` 子命令都是在 donno git repo 中执行。
也就是说，任何 `don git <p1, p2, p3 ...>` 等效于：
```
cd ~/.donno/repo
git <<p1, p2, p3 ...>
```

这种第一种情况下用户在 S 主机上执行：
```
don git stash
don git pull
don git stash pop
don backup-patch
```

第二种情况用户在 T 主机上执行：
```
don git pull
don restore-patch
```

