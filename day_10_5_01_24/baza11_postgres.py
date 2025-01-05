import asyncio  # działania równoległe
import asyncpg


async def fetch_data():
    conn = await asyncpg.connect(
        user='',
        password='',
        database='',
        host='')

    try:
        rows = await conn.fetch('SELECT * FROM users;')
        for row in rows:
            print(row)

        # pojedynczy wiersz
        single_row = await conn.fetchrow("SELECT * FROM users WHERE id=$1;", 1)
        if single_row:
            print(f"Single Row -> ID: {single_row['id']}")
    finally:
        await conn.close()


asyncio.run(fetch_data())
# <Record id=1 name='John'>
# <Record id=2 name='John'>
# <Record id=3 name='John'>
# <Record id=4 name='JohnPau'>
# <Record id=5 name='John'>
# <Record id=6 name='John2'>
# <Record id=7 name='John'>
# <Record id=8 name='John'>
# <Record id=9 name='John'>
# <Record id=10 name='John'>
# <Record id=11 name='John'>
# <Record id=12 name='RADEK'>
# <Record id=13 name='RADEK'>
# <Record id=14 name='SEBEK'>
# <Record id=15 name='RADEK'>
# <Record id=16 name='RADEK'>
# Single Row -> ID: 1
