import asyncio  # działania równoległe
import asyncpg


async def run():
    conn = await asyncpg.connect(
        user='',
        password='',
        database='',
        host='')

    await conn.fetch('''CREATE TABLE  IF NOT EXISTS users(id SERIAL PRIMARY KEY, name TEXT);''')
    await conn.execute('''
    INSERT INTO users (name) VALUES ($1)
    ''', 'RADEK')
    await conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
