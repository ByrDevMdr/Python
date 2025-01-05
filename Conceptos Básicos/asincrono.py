import asyncio

async def tarea1():
    print("Tarea 1 comenzando...")
    await asyncio.sleep(1)  # Espera 1 segundo
    print("Tarea 1 terminada!")

async def tarea2():
    print("Tarea 2 comenzando...")
    await asyncio.sleep(2)  # Espera 2 segundos
    print("Tarea 2 terminada!")

async def main():
    tarea_1 = asyncio.create_task(tarea1())
    tarea_2 = asyncio.create_task(tarea2())

    await tarea_1  # Espera a que la tarea 1 finalice.
    await tarea_2  # Espera a que la tarea 2 finalice.

asyncio.run(main())  # Ejecuta el main.