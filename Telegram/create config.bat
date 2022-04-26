@echo off

chcp 65001

set /p TOKEN="TOKEN: "

 
echo TOKEN = r'%TOKEN%' > config.py


