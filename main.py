import asyncio

async def water(temp):
    print(f"Заповнення водою з температурою {temp}")
    await asyncio.sleep(1)
    print("Вода заповнена")

async def wash(spin_speed):
    print(f"Прання з швидкістю {spin_speed} об/хв")
    await asyncio.sleep(1)
    print("Прання завершено")

async def rinse():
    print("Полоскання")
    await asyncio.sleep(1)
    print("Полоскання завершено")

async def spin():
    print("Віджимання")
    await asyncio.sleep(1)
    print("Віджимання завершено")

async def dry():
    print("Сушка")
    await asyncio.sleep(1)
    print("Сушка завершена")

async def iron():
    print("Прасування")
    await asyncio.sleep(1)
    print("Прасування завершено")

async def washing_machine(temp, spin_speed, need_dry, need_iron):
    await water(temp)
    await wash(spin_speed)
    await rinse()
    await spin()

    if need_dry:
        await dry()
    if need_iron:
        await iron()

def machine_temperature():
    while True:
        try:
            temp = int(input("Введіть температуру води від 0 до 100: "))
            if 0 <= temp <= 100:
                return temp
            else:
                print("Введіть температуру в діапазоні від 0 до 100 ще раз")
        except ValueError:
            print("Введіть число ще раз")

def machine_spin_speed():
    while True:
        try:
            spin_speed = int(input("Введіть кількість обертів об/хв від 400 до 1600: "))
            if 400 <= spin_speed <= 1600:
                return spin_speed
            else:
                print("Введіть швидкість в діапазоні від 400 до 1600 об/хв ще раз")
        except ValueError:
            print("Введіть число ще раз")

def ask_yes_no(question):
    while True:
        answer = input(f"{question} (так/ні): ").lower()
        if answer in ['так', 'ні']:
            return answer == 'так'
        print("Введіть 'так' або 'ні'")

async def main():
    temp = machine_temperature()
    spin_speed = machine_spin_speed()
    need_dry = ask_yes_no("Чи потрібно сушити речі?")
    need_iron = ask_yes_no("Чи потрібно прасувати речі?")

    print("Слава Україні!")
    await washing_machine(temp, spin_speed, need_dry, need_iron)
    print("Прання завершено (Україна переможе!)")

asyncio.run(main())