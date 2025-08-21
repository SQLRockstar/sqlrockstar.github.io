---
layout: post
title: The Seven Samurai of SQL Server Data Protection
date: '2018-01-23 14:17:39 +0000'
categories:
- Data Security and Privacy
- Database Design
- MSSQL
- SQL MVP
- SQL Server 2016
- SQL Server 2017
- SQL Server Performance
tags:
- Data
- encryption
- Microsoft SQL Server
- privacy
- security
---

<img class="aligncenter wp-image-18575 size-large" src="https://thomaslarock.com/wp-content/uploads/2018/01/samurai-sql-600x389.jpg" alt="The Seven Samurai of SQL Server Data Protection" width="600" height="389" />

I love movies. I don’t know if I qualify as a movie buff, but I know I have spent a good chunk of my lifetime watching films. One of my favorite films is <a href="http://www.imdb.com/title/tt0054047/" target="_blank" rel="noopener">The Magnificent Seven</a>. (We won’t talk about the awful remake; I like to pretend it never happened.)

The Magnificent Seven is based upon the <a href="http://www.imdb.com/title/tt0047478/" target="_blank" rel="noopener">Kurosawa masterpiece The Seven Samurai</a>. The two movies share the same plot: bad guys threaten a village, villagers hire good guys to protect them, bad guys come back, fighting ensues, and happy ending for most.

These days I can’t help but think of the parallels between that plot and the current struggle we face with data security. Consider that we have the bad guys (let’s call them adversaries). These adversaries want our data. It is up to us, the villagers (i.e., data professionals) to find and deploy proper data security measures to guard against data loss or theft. The adversaries come back, the good guys fight back, and there is a happy ending for most.

Today there seems to be a never-ending supply of data breaches and leaks. <a href="https://azure.microsoft.com/en-us/get-started" target="_blank" rel="noopener">It is trivial to build and deploy applications</a>. As a result, data security, privacy, and quality all come a distant second to building shiny new apps that upload pictures of cats or to <a href="https://itunes.apple.com/us/app/not-hotdog/id1212457521?mt=8" target="_blank" rel="noopener">help us identify a hot dog</a>.

I want to help in the struggle against the adversaries. I’ve identified seven data security measures you can use. These ‘Seven Samurai’ will protect against all three possible attack vectors: data at rest, data in use, and data in motion.

Let’s have a look at how the Seven Samurai protect us from each.

&nbsp;
<h2>Data at Rest</h2>
Data at rest refers to data stored in files on disk. Examples are database files, database backups, or applications such as Excel spreadsheets.

Protection for this data includes traditional methods of permissions, firewalls, and anti-virus programs. Those methods are not enough when it comes to physical database files. Should an adversary make their way past, they may be able to copy data files and backups to restore data on their own servers.

To protect data at rest we will use the following Samurai: Transparent Data Encryption (TDE), BitLocker, and Backup File Encryption.
<h4>Transparent Data Encryption (TDE)</h4>
<a href="https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption" target="_blank" rel="noopener">TDE allows for real-time I/O encryption and decryption</a> of both the data and transaction log files. Encryption happens at the database page level. The pages are encrypted before  written to disk, and decrypted when read back into memory. This method also means that the database backup file cannot be restored to a server unless you have the necessary certificate.
<h4>BitLocker</h4>
<a href="http://www.itprotoday.com/management-mobility/manage-bitlocker-enterprise" target="_blank" rel="noopener">BitLocker is a built-in tool to Windows</a> that allows for you to encrypt your data volumes even when Windows is not running. If an adversary was to gain access to your physical server or hard drives they would not be able to remove the disk and access the data by attaching it to a different server.
<h4>Backup Encryption</h4>
<a href="https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/backup-encryption" target="_blank" rel="noopener">Backup Encryption is a feature for SQL Server</a> that allows you to encrypt the contents of the backup file. This encryption does not need TDE enabled. Just as with TDE, if you don’t have the corresponding certificate you will not be able to restore from the backup file.

&nbsp;
<h2>Data in Use</h2>
Data in use refers to data accessed by those in need. Unfortunately, data in use is more vulnerable than data at rest because those that need the data often end up sharing that data with people that shouldn’t need it in any way. Social engineering is one method an adversary will use to access data in use. But an adversary can also access a spreadsheet on a USB drive that left behind on a bus.

To protect data in use we will use the following Samurai: Dynamic Data Masking (DDM) and Row Level Security (RLS).
<h4>Dynamic Data Masking (DDM)</h4>
<a href="https://docs.microsoft.com/en-us/sql/relational-databases/security/dynamic-data-masking" target="_blank" rel="noopener">DDM allows for you to limit exposure of sensitive data by applying a mask</a> to columns at the end of a query operation. The performance impact for applying the mask is minimal, because it happens at the end. DDM is a great way to help avoid issues that arise when users take their work home at night but forget a spreadsheet on the bus.
<h4>Row Level Security (RLS)</h4>
<a href="https://docs.microsoft.com/en-us/sql/relational-databases/security/row-level-security" target="_blank" rel="noopener">RLS allows for you to create security policies that will filter data</a> as it is returned from the underlying tables. The user has no knowledge that any filtering took place. When combined with DDM, RLS gives you the opportunity to reduce your risk that data in use will fall into the wrong hands.

&nbsp;
<h2>Data in Motion</h2>
Data in motion requires special protection. An adversary can use methods such as a man-in-the-middle attack to access your data in motion. The best way to protect data in motion is to use encryption methods for your sensitive data.

To protect data in motion we will use the following Samurai: Secure Sockets Layer (SSL) and Always Encrypted (AE).
<h4>Secure Socket Layers (SSL)</h4>
<a href="https://support.microsoft.com/en-us/help/316898/how-to-enable-ssl-encryption-for-an-instance-of-sql-server-by-using-mi" target="_blank" rel="noopener">SSL allows for you to encrypt data that is transmitted between a client and the database server</a>. SSL will force the client and the server to authenticate the identity of each other using a “handshake”. After the handshake, the connection becomes encrypted and data can be transmitted in a secure manner.
<h4>Always Encrypted (AE)</h4>
AE takes place at the column level, encrypting the data such that only the ciphertext is ever stored on disk or brought into memory. That means <a href="https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine" target="_blank" rel="noopener">AE will protect both data in motion *and* at rest, making AE my favorite Samurai</a>. Data encryption and decryption happens only at the client. The only data transmitted between the client and database server is ciphertext.

&nbsp;
<h2>Summary</h2>
Data is the most critical asset that any company owns, it’s time we treat it as such.

At any minute of the day, an adversary has opportunities to access your data. With each interaction your end users have, internally and externally, your surface area of attack increases. The process of accessing, using, storing, and sharing data must be made secure. Data security needs to be a primary focus for every person and company.

There you have it, the Seven Samurai of data security for SQL Server. Individually each has its own strength. Together they form a defense that is strong enough to defeat most any adversary that tries to access data that is not theirs to access.