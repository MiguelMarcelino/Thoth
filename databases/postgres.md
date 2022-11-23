# PostgreSQL

Postrges is a relational database management system.

## Installation
### Install PostgreSQL 12 on Ubuntu 20.04 LTS
```bash
sudo apt update
sudo apt install -y postgresql postgresql-contrib postgresql-client
sudo systemctl status postgresql.service
```

### Install / deploy Postgres on Kubernetes with Zalando Postgres Operator

Postgres is probably the database which is most common on Cloud platforms and also, running
on Kubernetes environments. There are several so called "Kubernetes Operators" which handle
the deployment of Postgres clusters for you. One of it is the [Postgres Operator by Zalando](https://github.com/zalando/postgres-operator).

You can find some tutorials regarding deployment of the operator and how to work with it,
in the link list below:

- [Deploy Zalando Postgres Operator on your Kubernetes cluster](https://thedatabaseme.de/2022/03/13/keep-the-elefants-in-line-deploy-zalando-operator-on-your-kubernetes-cluster/)
- [Configure Zalando Postgres Operator Backup with WAL-G](https://thedatabaseme.de/2022/03/26/backup-to-s3-configure-zalando-postgres-operator-backup-with-wal-g/)
- [Configure Zalando Postgres Operator Restore with WAL-G](https://thedatabaseme.de/2022/05/03/restore-and-clone-from-s3-configure-zalando-postgres-operator-restore-with-wal-g/)

## Initial database connection

A local connection (from the database server) can be done by the following command:

```bash
sudo -u postgres psql

psql (12.12 (Ubuntu 12.12-0ubuntu0.20.04.1))
Type "help" for help.

postgres=#
```

## Set password for postgres database user

* quickcommand `\password`
* `alter user postgres password 'Supersecret'`. 

A connection using the `postgres` user is still not possible from the "outside", hence to the default settings in the `pg_hba.conf`
	Client authentication is controlled by a configuration file, which traditionally is named `pg_hba.conf` and is stored in the database cluster's data directory.
	HBA stands for host-based authentication

### Update pg_hba.conf to allow postgres user connections with password

In order to allow connections of the `postgres` database user not using OS user
authentication, you have to update the `pg_hba.conf` which can be found under
`/etc/postgresql/12/main/pg_hba.conf`.

```
sudo vi /etc/postgresql/12/main/pg_hba.conf

...
local   all             postgres                                peer
...
```

Change the last section of the above line to `md5`.

```
local   all             postgres                                md5
```

A restart is required in order to apply the new configuration:

```bash
sudo systemctl restart postgresql
```

Now a connection from outside the database host is possible e.g.

```bash
psql -U postgres -d postgres -h databasehostname
```

## Creation of additional database users

A database user can be created by the following command:

```sql
create user myuser with encrypted password 'Supersecret';
```

## Creation of databases

One can create new Postgres databases within an instance. Therefore you can use the `psql`
command to login (see above).

```sql
CREATE DATABASE dbname OWNER myuser;
```

You can leave the `OWNER` section of the command, when doing so, the current user will become
owner of the newly created database.

To change the owner of an existing database later, you can use the following command:

```sql
postgres=# alter database dbname owner to myuser;
ALTER DATABASE
```

## Backup and Restore

### pg_dump / pg_dumpall

Using `pg_dump` or `pg_dumpall` enables you to extract / export a PostgreSQL database(s) into a (SQL) script file or a custom archive file.

#### pg_dump

The following command creates a custom archive file from a database specified with `-d`. 
Using the `--create` option will include the SQL commands in the dump script that will create the database before importing it later. The `-Z 9` option in this example compresses the SQL script created with the highest available compression rate (`0-9`).

```bash
pg_dump -h vmdocker -U awx -d awx --create -f -Z 9 /tmp/awx_dump.sql.gz
```

The following command creates a custom archive file from a database specified with `-d`. To export data in custom format, you have to specify so with the `-F c` option. Custom file dumps have the benefit, that they are compressed by default.

```bash
pg_dump -h <pg_host> -U <username> -d <database> -F c -f /pg_dump/dumpfile.dmp
```

Custom format files can only be restored by `pg_restore` (see below). A SQL dump can be restored by using `psql`.

```bash
psql -d newdb -f db.sql
```

A complete guide of `pg_dump` from the official documentation can be found [here](https://www.postgresql.org/docs/current/app-pgdump.html).

#### pg_dumpall

A full dump of all databases of a Postgres instance can be done by `pg_dumpall`. It will include also user creation information.
A difference to `pg_dump`, you cannot choose for different output formats. `pg_dumpall` will always create a SQL script as output.

```bash
pg_dumpall -h <pg_host> -U postgres > database.out
```

So importing a full dump is really easy by the following `psql` command:

```bash
psql -h <pg_host> -f databaseb.out -U postgres
```

A complete guide of `pg_dumpall` from the official documentation can be found [here](https://www.postgresql.org/docs/current/app-pg-dumpall.html).

### pg_restore

`pg_restore` can be used to restore custom file dumps created by `pg_dump`.

The following command will create the datbase (which has been dumped before).
```bash
pg_restore -h <pg_host> -U <pg_user> -d postgres --create -F c /tmp/db.dmp -v
```

A complete guide of `pg_restore` from the official documentation can be found [here](https://www.postgresql.org/docs/current/app-pgrestore.html).

<hr>

## Sources
* Shamelessly copied from Christian Lempa's [cheat sheets](https://github.com/christianlempa/cheat-sheets).

<hr>

Related to: [databases](databases)