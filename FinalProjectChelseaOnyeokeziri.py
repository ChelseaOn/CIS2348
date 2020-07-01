#Chelsea Onyeokeziri 1570698
import csv
import operator
from datetime import datetime


with open ('C:\\Users\\hcogu\\Desktop\\ManufacturerList.csv', 'r') as ManufacturerList_input:
    read_list = csv.reader(ManufacturerList_input)
    for row in read_list:
        manufacturer_item_id=row[0]
        manufacturer_name=row[1]
        item_type = row[2]
        damaged = row[3]


with open ('C:\\Users\\hcogu\\Desktop\\ServiceDatesList.csv', 'r') as ServiceDate_input:
    read_date = csv.reader(ServiceDate_input)
    for i in read_date:
        service_item_id = i[0]
        service_date = i[1]

with open ('C:\\Users\\hcogu\\Desktop\\PriceList.csv','r') as PriceList_input:
    read_price = csv.reader(PriceList_input)
    for yes in read_price:
        price_item_id = yes[0]
        price_item = yes[1]

with open ('C:\\Users\\hcogu\\Desktop\\FullInventory.csv', 'w') as csv_file:
    write_inventory=csv.writer(csv_file, dialect='excel')
for inventory in write_inventory:
    if manufacturer_item_id==service_item_id==price_item_id:
        manufacturer_item_id = inventory[0]
        manufacturer_name = inventory[1]
        item_type = inventory [2]
        price_item = inventory [3]
        service_date = inventory [4]
        damaged= inventory [5]
        full_inventory = inventory
        full = sorted(full_inventory, key=operator.itemgetter(2))
        write_inventory.writerow(full)









with open ('C:\\Users\\hcogu\\Desktop\\LaptopInventory.csv', 'w') as LaptopInventory_file:
    write_laptop = csv.writer(LaptopInventory_file)
    with write_laptop:
        if item_type == 'laptop' and manufacturer_item_id==service_item_id==price_item_id:
            laptop_id =manufacturer_item_id==service_item_id==price_item_id [0]
            laptop_manufacturer = manufacturer_name [1]
            laptop_price = price_item [2]
            laptop_service_date = service_date [3]
            laptop_damaged = damaged [4]
            laptop_inventory = laptop_id,laptop_manufacturer,laptop_price, laptop_service_date, laptop_damaged
            sorted_laptop_inventory = sorted(laptop_inventory, key=operator.itemgetter(0))
            write_laptop.writerow([sorted_laptop_inventory])



with open ('C:\\Users\\hcogu\\Desktop\\PhoneInventory.csv', 'w') as PhoneInventory_file:
    write_phone = csv.writer(PhoneInventory_file)
    with write_phone:
        if item_type == 'phone' and manufacturer_item_id==service_item_id==price_item_id:
            phone_id = manufacturer_item_id==service_item_id==price_item_id, [0]
            phone_manufacturer = manufacturer_name [1]
            phone_price = price_item [2]
            phone_service_date = service_date [3]
            phone_damaged = damaged [4]
            phone_inventory = phone_id,phone_manufacturer,phone_price,phone_service_date, phone_damaged
            sorted_phone_inventory = sorted(phone_inventory, key=operator.itemgetter(0))
            write_phone.writerow([sorted_phone_inventory])



TowerInventory_file = open ('C:\\Users\\hcogu\\Desktop\\TowerInventory.csv', 'w')
with TowerInventory_file:
    write_tower = csv.writer(TowerInventory_file)
    if item_type == 'tower' and manufacturer_item_id==service_item_id==price_item_id:
        tower_id = manufacturer_item_id==service_item_id==price_item_id, [0]
        tower_manufacturer = manufacturer_name [1]
        tower_price = price_item [2]
        tower_service_date = service_date [3]
        tower_damaged = damaged [4]
        tower_inventory = phone_id,phone_manufacturer,phone_price,phone_service_date, phone_damaged
        sorted_tower_inventory = sorted(tower_inventory, key=operator.itemgetter(0))
        write_tower.writerow([sorted_tower_inventory])

with open ('C:\\Users\\hcogu\\Desktop\\PastServiceDateInventory.csv', 'w') as PastService_file:
    write_past = csv.writer(PastService_file)

    dates = datetime.strptime (service_date,"%m/%d/%Y")

    if dates <= datetime.now() and manufacturer_item_id==service_item_id==price_item_id:
        past_id = manufacturer_item_id==service_item_id==price_item_id [0]
        past_manufacturer = manufacturer_name [1]
        past_type = item_type [2]
        past_price = price_item [3]
        past_service = service_date [4]
        past_damaged = damaged [5]
        past_date = past_id,past_manufacturer,past_type, past_price, past_service, past_damaged


with open ('C:\\Users\\hcogu\\Desktop\\DamagedInventory.csv', 'w') as DamagedInventory_file:
    write_damaged = csv.writer(DamagedInventory_file)

    with write_damaged:
        if damaged == "damaged" and manufacturer_item_id==service_item_id==price_item_id:
            damaged_id = manufacturer_item_id == service_item_id == price_item_id [0]
            damaged_manufacturer = manufacturer_name [1]
            damaged_type = item_type [2]
            damaged_price = price_item [3]
            damaged_service = service_date [4]
            damaged_list = damaged_id, damaged_manufacturer, damaged_price, damaged_service
            sorted_damaged_list = sorted(damaged_list, key=operator.itemgetter(3), reverse=True )






