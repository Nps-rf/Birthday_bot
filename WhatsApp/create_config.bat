@echo off

chcp 65001

set /p APIUrl="APIUrl: "
set /p TOKEN="TOKEN: "

 
echo TOKEN = r'%token%' > env.py


