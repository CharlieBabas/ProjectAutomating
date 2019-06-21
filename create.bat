@ECHO OFF
cd C:\Users\
python create.py %1
cd C:\Users\cagui\Documents\Proyects\MyProjects\%1
git init
git remote add origin https://github.com/CharlieBabas/%1.git 
touch README.md
git add .
git commit -m "Initial commit"
git push -u origin master
code .
