# MAde By MnnaRDX
from faker import Faker
import random
fake = Faker('en_PK')
def zong():
    zongcode = ['+92310','+92311','+92312','+92313','+92314','+92315','+92316','+92317','+92318','+92319','+92370']
    return f'{(random.choice(zongcode))}{random.randrange(1000000,9999999)}'
def jazz():
    jazzcode = ['+92301','+92302','+92303','+92304','+92305','+92306','+92307','+92308','+92309','+92320','+92321','+92322','+92323','+92324','+92325','+92326','+92327','+92328','+92329']
    return f'{(random.choice(jazzcode))}{random.randrange(1000000,9999999)}'
def telenor():
    telenorcode = ['+92340','+92341','+92342','+92343','+92344','+92345','+92346','+92347','+92348','+92349']
    return f'{(random.choice(telenorcode))}{random.randrange(1000000,9999999)}'
def ufone():
    ufonecode = ['+92330','+92331','+92332','+92333','+92334','+92335','+92336','+92337','+92338','+92339']
    return f'{(random.choice(ufonecode))}{random.randrange(1000000,9999999)}'
choose = [zong,jazz,telenor,ufone]
def createvcf():
    print('BEGIN:VCARD')
    print('VERSION:3.0')
    print(f'FN:{fake.name()}')
    print(f"TEL;TYPE=CELL:{random.choice(choose)()}")
    print(f'EMAIL:{fake.free_email()}')
    print('END:VCARD')
def file():
    a = int(input(('Enter how much contacts you want :')))
    b = input('Enter the file name :')
    ex = '_munnardx.vcf'
    for _ in range(a):
        with open(f'{b}{ex}','a') as f:
            f.write(f'''BEGIN:VCARD
VERSION:3.0
FN:{fake.name()}
TEL;TYPE=CELL:{random.choice(choose)()}
EMAIL:{fake.ascii_email()}
END:VCARD

''')

file()
