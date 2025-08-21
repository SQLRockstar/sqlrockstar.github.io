---
layout: post
title: Adding Python Packages to SQL Server 2017
date: '2018-05-16 08:44:26 +0000'
categories:
- Data Analytics
- MSSQL
- SQL MVP
- SQL Server 2017
tags:
- python
- sql server
- sql server 2017
---

SQL Server 2017 allows for the use of Python scripts called as an external script. SQL Server comes with some Python packages by default. Today I wanted to talk about adding Python packages to SQL Server 2017.

To get started with Python in SQL Server 2017 we must enable the use of external scripts.

&nbsp;
<h2>Enable SQL Server for Python Scripts</h2>
You run Python "inside" of SQL Server through the use of the sp_execute_external_script system stored procedure. To use this procedure you must enable your instance to allow for remote script execution. That's an easy configuration change:
<pre lang="tsql">EXEC sp_configure 'external scripts enabled', 1
RECONFIGURE WITH OVERRIDE
</pre>
Here's a diagram that better helps to explain what happens when you call this external procedure (full article located at <a href="https://docs.microsoft.com/en-us/sql/advanced-analytics/python/new-components-in-sql-server-to-support-python-integration?view=sql-server-2017" target="_blank" rel="noopener">Components in SQL Server to support Python integration</a>):

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/python-sql.png"><img class="aligncenter size-full wp-image-19112" src="https://thomaslarock.com/wp-content/uploads/2018/05/python-sql.png" alt="Python SQL Server" width="565" height="243" /></a>

&nbsp;

You'll note the use of Launchpad.exe. If that service is not running you will see an error:
<pre lang="tsql">Msg 39011, Level 16, State 1, Line 4
SQL Server was unable to communicate with the LaunchPad service. 
Please verify the configuration of the service.</pre>
If you are using SQL Server for R and Python, it's a good idea to set the Launchpad service to automatic startup.

Now we are ready to execute a script. Let's take a look at the Python packages installed by default.

&nbsp;
<h2>Find All Python Packages Installed in SQL Server 2017</h2>
This is easy with a script such as this one:
<pre lang="tsql">EXEC sp_execute_external_script
@language = N'Python',
@script = N'
import pip
import pandas as pd
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
df = pd.DataFrame(installed_packages_list)
OutputDataSet = df
'
WITH RESULT SETS (( PackageVersion nvarchar (150) ))</pre>
This returns 128 rows, here's a quick look:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/python-sql-server-package-list.jpg"><img class="aligncenter size-large wp-image-19113" src="https://thomaslarock.com/wp-content/uploads/2018/05/python-sql-server-package-list-319x600.jpg" alt="Python SQL Server package list" width="319" height="600" /></a>

&nbsp;
<h2>Find Specific Python Package Installed in SQL Server 2017</h2>
There's a way to search for one package, too. We just filter for a specific package name, like this:
<pre lang="tsql">EXECUTE sp_execute_external_script
  @language = N'Python',
  @script = N'
import pip
import pkg_resources
pckg_name = "revoscalepy"
pckgs = pandas.DataFrame([(i.key) for i in pip.get_installed_distributions()], columns = ["key"])
installed_pckg = pckgs.query(''key == @pckg_name'')
print("Package", pckg_name, "is", "not" if installed_pckg.empty else "", "installed")'
</pre>
This is what the result looks like:

&nbsp;

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/python-sql-server-find-specific-package.jpg"><img class="aligncenter size-large wp-image-19114" src="https://thomaslarock.com/wp-content/uploads/2018/05/python-sql-server-find-specific-package-600x150.jpg" alt="Python SQL Server installed packages" width="600" height="150" /></a>

&nbsp;

One word of warning here, Python is *very* particular about indents. If you are going to be using Python scripts with SQL Server, my advice is to use a true Python editor, like VS Code, and not rely on using SSMS. If your indents are incorrect you will see an error message similar to this:
<pre lang="tsql">Msg 39004, Level 16, State 20, Line 24
A 'Python' script error occurred during execution of 'sp_execute_external_script' with HRESULT 0x80004004.
Msg 39019, Level 16, State 2, Line 24
An external script error occurred: 

Error in execution.  Check the output for more information.
Traceback (most recent call last):
  File "", line 3, in 
    import pip
    ^
IndentationError: unexpected indent

SqlSatelliteCall error: Error in execution.  Check the output for more information.
</pre>
The error is clear - "unexpected indent". The error message also points to the exact spot. But you could have many such errors in your script. That's why using VS Code would be handy, and you can then cut and paste the script into your procedure.

OK, so what if our package can't be found? Not a problem, we can install new ones using pip.

&nbsp;
<h2>Adding Python Packages to SQL Server 2017</h2>
To add a Python package to your instance of SQL Server you need to use either a command line or Visual Studio using the Python Environments window. I will use the command line for this example.

The first thing we must know is the location of packages used by Python for SQL Server. If SQL Server was installed with default settings, the directory will be similar to this:

C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\PYTHON_SERVICES

If you need to manually find this directory, here's the Python command to return the information:
<pre lang="tsql">EXEC sp_execute_external_script
  @language =N'Python',
  @script=N'import sys; print("\n".join(sys.path))'
</pre>
Now that we know which directory the Python.exe resides, we can open a command line there and use pip. I have two warnings for you. First, you must be running the command line as an account with sufficient permissions to write to this directory. Second, you want to be using the pip.exe found in the /Scripts directory. If you just call pip you will use whatever pip is defined in your PATH from <a href="https://xkcd.com/1987/" target="_blank" rel="noopener">previous Python installations</a>.

So, to install the Keras package, I navigated to the /Scripts directory and execute this command:

&gt;pip.exe install keras

<a href="https://thomaslarock.com/wp-content/uploads/2018/05/python-sql-server-install-keras.jpg"><img class="aligncenter size-large wp-image-19115" src="https://thomaslarock.com/wp-content/uploads/2018/05/python-sql-server-install-keras-600x338.jpg" alt="Python SQL Server install Keras package" width="600" height="338" /></a>

&nbsp;

And, I can run the script above to verify that Keras is now installed.

&nbsp;
<h2>Summary</h2>
Using Python from SQL Server is easy. It's as simple as configuring your instance to allow for external scripts, and then calling an external script with a stored procedure.

The caveat I have with using Python and SQL Server is that this gives you YAPI (Yet Another Python Install). It can be difficult keeping track of your Python environment.

But if you have a need to use Python and interact with relational storage, then SQL Server is now an option. I could see scenarios where you might take advantage of SQL Server in a container, storing temporary results, letting Python focus on the data science stuff. For someone that lives inside of Visual Studio, this is probably an ideal scenario to blend Python and SQL Server storage.
<pre></pre>