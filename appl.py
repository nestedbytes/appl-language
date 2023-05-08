import typer
import os
import linecache
from requests import get
import urllib.request

app = typer.Typer()

latestversion = get('https://raw.githubusercontent.com/shourdev/appl-language/main/version.txt').text
version = "1.0.0"




def sayfun():
    namepro = open(f"name.txt","r")
    
    extension = ".aple"
    projectvar = open(f"{namepro.read()}{extension}")
    with open(projectvar.name) as file_iterator:
     for line in file_iterator:
        if "say" in line:
            print(next(file_iterator))
 
    
   
       
  
@app.command()
def init(name: str):
    if (latestversion.strip() == version):
        print() 
        print(f"Creating new project by the name {name}")
        project = open(f"{name}.aple", "x")
        print(f" {name} has been created")
        with open(f"name.txt","w") as file:
           file.write(name)
    else:
        
     print("This version is outdated please update it from https://shourgamer2.tk/appl-language/")
   
    
@app.command()
def run():
    if (latestversion.strip() == version):
        print()
        namepro = open(f"name.txt","r")
    
        extension = ".aple"
        projectvar = open(f"{namepro.read()}{extension}")
        say = "say"
   
        readfile = projectvar.read()
        saylines_to_print = [2] 
  
# checking condition for string found or not
        if say in readfile: 
          sayfun()
        else:
            print() 
    else:
        print("This version is outdated please update it from https://shourgamer2.tk/appl-language/")
    
    
     
        
   
  
  
   

@app.command()
def about():
    if (latestversion.strip() == version):
         print("This is a simple programming language built in python.")
         
    else:
        print("This version is outdated please update it from https://shourgamer2.tk/appl-language/")
   




       

    
  

     
    
   
     
  
   

  

  

if __name__ == "__main__":
    app()
