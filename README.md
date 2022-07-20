<h1>Runaway Reactions Web Interface</h1>

Runaway Reactions are a type exothermic chemical reactions. When the heat generated by the chemical reaction exceeds the cooling capacity of the chemical plant, it may cause an explostion. This website contains a list of runaway reactions. You can add, modify or delete the reactions in this database using the django admin interface.


<h2>Getting Started</h2>

<ul>
<li>Download all files in the repository</li>
<li>Install Python</li>
<li>Install Pycharm</li>
<li>Install MySQL</li>
</ul>

<br><br>
Execute the following commands on command prompt:
<br>
<ul>
<li>pip install django</li>
<li>pip install mysql.connector</li>
<li>pip install mysqlclient</li>
<li>pip install openpyxl</li>
<li>pip install pymysql</li>
</ul><br>

Then, add mysql passwords in DatabaseGenerator.py line 14 and pyshop/settings.py line 85<br><br>

Open MySQL Command Line Client and execute the query:<br>
create database runawayreactions;

In python folder execute:
<ul>
<li>python manage.py makemigrations</li>
<li>python manage.py migrate</li>
</ul><br>

Next, Run the file DatabaseGenerator.py

Execute the query:<br>
python manage.py createsuperuser<br><br>
Follow the steps to create a superuser. This username and password will be used to login to the admin page<br><br>

Execute the query:<br>
python manage.py runserver<br><br>

Open your browser enter "localhost:8000"
