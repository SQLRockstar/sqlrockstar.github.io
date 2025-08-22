---
layout: post
title: Restoring SQL Server Database on Linux Using SQL Operations Studio
date: '2017-11-22 16:50:42 +0000'
categories:
- MSSQL
- SQL MVP
tags:
- backup
- Docker
- iMac
- Linux
- restore
- sql server
---

I've had a busy few months of travel. This has cut into my blogging time as well as time to play with new things. One of those things was getting started on restoring a SQL Server database on Linux using SQL Operations Studio.

With the short Thanksgiving week, I set aside a few hours to configure and document how to get SQL Server running in a Docker container on my iMac, connect using SQL Operations Studio, and restoring a SQL Server database.

In order to see this magical unicorn for yourself, you need two things: Docker and SQL Operations Studio. You can <a href="https://www.docker.com/docker-mac" target="_blank" rel="noopener">download Docker for Mac here</a>, and you can download <a href="https://github.com/Microsoft/sqlopsstudio" target="_blank" rel="noopener">SQL Operations Studio for Mac here</a>. I will leave the installation of each as an exercise for the reader.

With those tools installed, let's get started.
<h2>Running SQL Server inside Docker on iMac</h2>
After Docker is installed you need to configure it to use at least 4GB of memory, like this:

<img class="aligncenter wp-image-18188 size-full" src="https://thomaslarock.com/wp-content/uploads/2017/11/docker_memory_settings.jpg" alt="Configure Docker memory settings" width="380" height="508" />

You also need at least 4GB of available disk space. And don't forget any of the other requirements for <a href="https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup#system" target="_blank" rel="noopener">running SQL Server on Linux</a>.

The next step is to pull the latest version of SQL Server from the Docker Hub. We can do this with a simple bash command:
<pre lang="bash">sudo docker pull microsoft/mssql-server-linux:latest</pre>
You can also use Powershell. The commands for both are <a href="https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker" target="_blank" rel="noopener">on this page</a>, in case you wanted to see them. I'm going to use the default Terminal app on my iMac:

<img class="aligncenter size-full wp-image-18189" src="https://thomaslarock.com/wp-content/uploads/2017/11/pulling_docker_image.jpg" alt="pulling latest SQL Server Docker container image" width="552" height="193" />

When that is complete I will be able to start the instance with the following command:
<pre lang="bash">sudo docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=yourStrong(!)Password' 
-p 1433:1433 -d microsoft/mssql-server-linux:latest</pre>
For a full list of Docker run commands, <a href="https://docs.docker.com/engine/reference/commandline/run/" target="_blank" rel="noopener">go here</a>. And for more information on the the Docker repository image for SQL Server on Linux, <a href="https://hub.docker.com/r/microsoft/mssql-server-linux/" target="_blank" rel="noopener">go here</a>.

Lastly, we can verify that the instance is running with the following command:
<pre lang="bash">sudo docker ps -a</pre>
You want the status to show as "Up". If it shows anything else then you will want to <a href="https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-configure-docker#troubleshooting" target="_blank" rel="noopener">check out the troubleshooting guide here</a>.  This command also shows that our Docker container has a name. We could have set the name upon startup, but we didn't. So, we will rename it now, using this command, where we replace CONTAINERID with the actual container id:
<pre lang="bash">sudo docker rename CONTAINERID 'PANCETTA'</pre>
OK, the instance is up and running, with a name of PANCETTA. Next, we will copy a database backup file into the container. FIrst, I will create our own directory for backup files using one line:
<pre lang="bash">sudo docker exec -it PANCETTA mkdir /var/opt/mssql/backups</pre>
I will navigate to a directory where I have a backup file, and then I can do the copy again with one line of code:
<pre lang="bash">sudo docker cp AdventureWorks2016CTP3.bak PANCETTA:/var/opt/mssql/backups</pre>
Next, let's connect to the instance and restore that backup.
<h2>Restoring SQL Server Database on Linux in SQL Operations Studio</h2>
First, we need to connect to the instance. We will start SQL Operations Studio and connect like this:

<img class="aligncenter wp-image-18190 size-full" src="https://thomaslarock.com/wp-content/uploads/2017/11/sql_operations_studio_connect_docker.jpg" alt="SQL Operaions Studio connect to docker linux" width="483" height="433" />

Once connected, we click on the 'Restore' icon on the dashboard to arrive at the Restore Database screen. There we will navigate to the directory where we have placed our backup file:

<img class="aligncenter size-medium wp-image-18191" src="https://thomaslarock.com/wp-content/uploads/2017/11/backup_file-490x315.jpg" alt="copy sql server backup file to docker container" width="490" height="315" />

Click OK, and the main screen will look like this:

<img class="aligncenter wp-image-18192 size-full" src="https://thomaslarock.com/wp-content/uploads/2017/11/restore_database_linux.jpg" alt="Restoring SQL Server Database on Linux in docker container" width="970" height="744" />

We can start the restore right away or generate a script. The script should look familiar:
<pre lang="tsql">USE [master]
RESTORE DATABASE [AdventureWorks2016CTP3]
FROMDISK= N'/var/opt/mssql/backups/AdventureWorks2016CTP3.bak'
WITH FILE = 1, MOVE N'AdventureWorks2016CTP3_Data' TO N'/var/opt/mssql/data/AdventureWorks2016CTP3_Data.mdf',
MOVE N'AdventureWorks2016CTP3_Log' TO N'/var/opt/mssql/data/AdventureWorks2016CTP3_Log.ldf',
MOVE N'AdventureWorks2016CTP3_mod' TO N'/var/opt/mssql/data/AdventureWorks2016CTP3_mod',
NOUNLOAD, STATS = 5</pre>
When the restore is complete, we can then navigate to the AdventureWorks2016 database:

<img class="aligncenter size-large wp-image-18193" src="https://thomaslarock.com/wp-content/uploads/2017/11/connect_to_sql_on_linux-354x600.jpg" alt="connect to sql server on linux" width="354" height="600" />

You are looking at SQL Server, running on Linux, in a Docker container, on my iMac, connected through SQL Operations Studio. Yes, it's as awesome as it looks.

And we could script all of this out, making it a repeatable process. I could configure a handful of containers with different configurations, spin them up, test some code, and spin them down with a push of a button.
<h2>Summary</h2>
I love living in the future. I love it so much, I may never leave.