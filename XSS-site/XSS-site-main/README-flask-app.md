# web-tech-to-flask-convertor
A setup to add raw html, css and javascript, with php backend into a flask app  

## Warnings  
Anything in the static folder is temporary! It will be deleted when you run the flask app each time!
Your php and html files CANNOT be named the same! - If they are, php will be rendered everytime. This due to the url's being the same as you send /test for test.html, or test.php. This is to prettify the urls a bit.

## usage  
Either fork, or download the source code via the Code button, then Download ZIP  
put your html, css, and javascript files into the raw-files directory  
The URL routes are just ip_address/filename  
Even if your files are in directories the url is the just the filename  
for php and html files, the file ending is added in  
e.g.  
serving index.html or html/index.html  
url is: ip_address/index  

index.html is served as root by default

## running  
1. Activate a virtual environment  
2. ```pip install -r requirements.txt```
if using php backend:  
3. ```sh start.sh```
else:  
3. ```python app.py```

## formatting  
Either have all html, css, and javascript files in a flat structure with no directories or sub directories 
OR
have four directories (case in-sensitive):  
html  
css  
javascript  
php    

