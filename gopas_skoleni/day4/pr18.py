import asyncio

async def citac(id):
    c = 1
    while True:
        print(f":Citac ID: {id} - {c}")
        c +=1
        # await asyncio.sleep(1)
        x=await asyncio.sleep(1) # muzu to klidne priradit nakemu 

loop = asyncio.get_event_loop()
loop.create_task(citac(1)) #zaregistruj spravci novou funkci
loop.create_task(citac(2))

loop.run_forever()
loop.close()
