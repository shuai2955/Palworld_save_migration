# 幻兽帕鲁存档迁移 Palworld_save_migration
本代码可实现幻兽帕鲁存档的任意方向迁移(从本地/服务器迁移到另一处本地/服务器，不限系统)
# 请在迁移存档前务必做好备份！！！
步骤如下（以linux）  
第一步，在新服务器上创建一个游戏，生成一个新的存档。  
第二步，将新服务器的存档复制到代码文件的target/Saved文件夹下（例：/home/steam/Steam/steamapps/common/PalServer/Pal/Saved/SaveGames/0/<save_id>/的内容）  
如果没有这个文件夹，自己创建一个文件夹，注意大小写保持一致。
第三步，将老存档复制到代码文件的source/Saved文件夹下  
第四步，按照文件顺序依次运行python程序。所有python程序运行完成后，会得到一个final文件夹  
第五步，将final文件夹里面的内容复制到新服务器的对应的存档位置中进行替换  
# 注意事项
假设旧服务器上有五人，新服务器上暂时只能三人创建存档，那么完成一次上述操作后，新服务器只会迁移这三个人的存档。第四、第五人迁移时需要将新服务器上的存档放进source和target中，然后执行上述五步。






You can migrate 'palword_save' from either Windows local, Windows server, or Linux server to any one of Windows local, Windows server, or Linux server.
