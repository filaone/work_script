#!/usr/bin/bash

# 首先执行 lsbom 命令
lsbom -f -l -s -pf /var/db/receipts/org.nodejs.pkg.bom | while read f; do sudo rm /usr/local/${f}; done

//删掉/usr/local/中的各个模块
rm -rf /usr/local/lib/node
rm -rf /usr/local/lib/node_modules
rm -rf /var/db/receipts/org.nodejs.*

rm -rf /usr/local/lib/node*
rm -rf /usr/local/include/node*

rm -rf /usr/local/bin/npm
rm -rf /usr/local/bin/node

rm -rf /usr/local/share/man/man1/node.1
rm -rf /usr/local/lib/dtrace/node.d
rm -rf /usr/local/share/systemtap/tapset/node.stp
rm -rf /usr/local/share/doc/node/

// 删除当前用户路径下的npm模块
rm -rf ~/.npm
rm -rf ~/.npmrc

echo "NodeJs has been moved!"
