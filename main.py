from Classes import staff,tables,menu,boss
import asyncio
Boss=boss.owner()
Vasya = staff.Staff()
t1 = tables.Table()
asyncio.run(Vasya.cook(t1,Boss))
Boss.stat()