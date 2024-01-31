# 幻兽帕鲁存档迁移 Palworld_save_migration
本代码可实现幻兽帕鲁存档的迁移(从linux到linux服务器)
# 请在迁移存档前务必做好备份！！！
步骤如下（以linux服务器之间为例）  
# 第一步，在新服务器上创建一个游戏，生成一个新的存档。  
# 第二步，将新服务器的存档复制到代码文件的target/Saved文件夹下如果没有这个文件夹，自己创建一个文件夹，注意大小写保持一致。 
 例：/home/steam/Steam/steamapps/common/PalServer/Pal/Saved/SaveGames/0/<save_id>/的内容
复制Players文件夹，Level.sav，LevelMeta.sav即可
# 第三步 按顺序将新旧存档写入source.txt和target.txt中每行一个存档名，不含扩展名
例子：fdafdasf 是旧存档下张三的角色文件，asasas是它的新文件。那么在source.txt和target.txt中， fdafdasf和asasas是在同一行的
# 第三步，将老存档（Players文件夹，Level.sav，LevelMeta.sav）复制到代码文件的source/Saved文件夹下  
# 第四步，按照文件顺序依次运行python程序。所有python程序运行完成后，会得到一个final文件夹  
# 第五步，将final文件夹里面的内容复制到新服务器的对应的存档位置中进行替换  
# 注意事项
假设旧服务器上有五人，新服务器上暂时只能三人创建存档，那么完成一次上述操作后，新服务器只会迁移这三个人的存档。第四、第五人迁移时需要完全重来

# 随时更新，如果有什么疑问，还请留言。我会尽力解决






Palworld Save Migration
This code can achieve  direction migration of Palworld save files (from a Linux server to another Linux server).

Please be sure to back up your save files before migrating!!!
Follow these steps (taking migration between Linux servers as an example):

Step 1: Create a new game on the new server to generate a new save file.
Step 2: Copy the new server's save files into the target/Saved folder of the code file directory. If this folder does not exist, create one, ensuring the case sensitivity is consistent.
Example: Contents of /home/steam/Steam/steamapps/common/PalServer/Pal/Saved/SaveGames/0/<save_id>/
Copy the Players folder, Level.sav, and LevelMeta.sav.

Step 3: Write the old and new save file names in order into source.txt and target.txt, one save name per line, without the extension.
Example: If fdafdasf is the old save file of a player named Zhang San, and asasas is its new file, then fdafdasf and asasas should be on the same line in both source.txt and target.txt.

Step 4: Copy the old save files (Players folder, Level.sav, LevelMeta.sav) into the source/Saved folder of the code file directory.
Step 5: Run the Python programs in the given order. After all Python programs have been executed, a final folder will be generated.
Step 6: Copy the contents of the final folder to the corresponding save file location on the new server for replacement.
Note
If there are five players on the old server, but only three can create save files on the new server temporarily, then only the save files of these three players will be migrated after completing the above operations once. For the fourth and fifth players, the migration needs to be completely redone.

Constantly updated. If you have any questions, please leave a message. I will try my best to solve them.

![image](https://github.com/shuai2955/Palworld_save_migration/blob/main/qqchat.png)
