## 'xlrd' Package Lab

This lab provides some practice working with library code in Python: 
* creating a virtual environment (a package-level namespace you can manage seperately from your global set of packages) 
* using the packages `xlrd` for reading and writing Microsoft Excel spreadsheets and `statistics` to describe the data you read.

<hr>

#### Step-by-step to get started

* On the Linux lab machines, clone this repo (and remove the `.git` directory if you've cloned it inside your grading repo).

* Inside this repo, create a python3 virtual environment named `venv` using the tool `virtualenv`.    
```virtualenv -p python3 venv ```

* Activate the `venv` virtual environment.
```source venv/bin/activate```

* Use `pip3` to install the packages `xlrd` and `statistics` into this virtual environment.     
```pip3 install xlrd```    
```pip3 install statistics```    

* Follow the instructions inside `main.py` to complete the lab. You're welcome to change the code however you'd like, but you should only need to add code in the sections marked `[FILL IN HERE]`.

* Deactivate your virtual environment.    
```deactivate```
