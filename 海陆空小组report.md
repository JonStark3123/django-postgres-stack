# custom scripts

## Project Description 

To allow user running custom scripts, not just the default read-write/read-only tests!

![图片 1](media/15833156303321/%E5%9B%BE%E7%89%87%201.png)

# Getting Started
1. set up custom script root folder 
 modify const `SCRIPTS_DIR` in `client/setting.py` to indicate custom script root path 
1. put some custom sql files under  `SCRIPTS_DIR` folder，
![](media/15833156303321/15833192351768.jpg)

1. start service `python3 manage.py runserver`
2. start client `python3 perffarm-client.py`
3. the bgbench result and all the sql file under your `SCRIPTS_DIR`  gonna automatly save to  `pgperffarm-db` 


## Implementation Details

###[client/collectors/scripts.py](https://github.com/chouchouyu/django-postgres-stack/blob/wsm/client/collectors/scripts.py) 

`scripts.py` is the main class for collecting scripts , run cmd and generate upload json.


|method   | result  | description|
| --- | --- | --- |
| hasScript | Ture/False | if custom script dir exist and with sql file in it return true,or else return false |
| run_custem_script | return run_cmd result | run bgbench cmd like  "pgbench -f a.sql -f b.sql -f … dbname" | scripts collect with some method use for scriptcollection and jsonFormat.
|getScriptListJson|json|perpare custome script information json 

###upload json 
we add a `customeScript` JsonObject to descrip custem scriptt result.

![-w635](media/15833156303321/15833213432675.jpg)
* if with no custem script situation,the `customeScript` is a empty JsonObject.

### service part 
1. add `customeScript` type  in `testCategory` table.
![](media/15833156303321/15833221918648.jpg)
1. upload result in db(6 indicate is a customeScript type)
![](media/15833156303321/15833222762576.jpg)

1. script file save in db. 
 ![-w973](media/15833156303321/15833223950597.jpg)




# Future work
add GUI for command line environment setups.

# PR summary
1. how to debugge in project and fix it.
2. To know what tps is.
3. pgbench simple usetage.
4. how to upload file and save by django.