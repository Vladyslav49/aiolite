### asyncsqlite3 - asynchronous driver for sqlite3.

Asynchronous interface with context managers for sqlite database:

```python
async with asyncsqlite3.connect(...) as conn:
    async with conn.execute("INSERT INTO some_table ..."):
        await conn.commit()

    async with conn.execute("SELECT * FROM some_table") as cursor:
        rows = await cursor.fetchall()
```

And without context managers:

```python
conn = await asyncsqlite3.connect(...)
cursor = await conn.execute("SELECT * FROM some_table")
rows = await cursor.fetchall()
await cursor.close()
await conn.close()
```

Connection pool and transaction:

```python
async with asyncsqlite3.create_pool(..., min_size=1, max_size=2) as pool:
    async with pool.acquire(timeout=1.5) as conn: # You can use a timeout when getting a connection from queue.
        async with conn.transaction():
            async with conn.execute("INSERT INTO some_table ..."):
                ...
    
    async with pool.acquire() as conn:
        async with conn.execute("SELECT id, name FROM some_table") as cursor:
            async for row in cursor:
                print(row) # <Record id=1 name='alex'>
                print(row[0], row["id"], row.get("id")) # 1 1 1
                print(dict(row)) # {'id': 1, 'name': 'alex'}
                print(tuple(row), list(row), set(row)) # (1, 'alex') [1, 'alex'] {1, 'alex'}
```

### Installation

asyncsqlite3 is compatible with Python 3.7 and newer. Use pip to install:

`$ pip install asyncsqlite3`

You can speed up asyncsqlite3 as follows:

`$ pip install asyncsqlite3[uvloop]`

### Details

How you see this module very look like [aiosqlite](https://github.com/omnilib/aiosqlite) and [asyncpg](https://github.com/MagicStack/asyncpg).

Implicit transactions are turned off, but you can use Connection method `transaction`.

### License

MIT
