# Created by saurav at 2019-05-01 in 10:21

__author__ = "Saurav Dahal"

def addToInventory(inventory, addedItems):
    emptyInventory = {}

    for i in addedItems:
        emptyInventory[str(i)] = addedItems.count(str(i))

    for k in emptyInventory.keys():
        if not k in inventory:
            inventory[str(k)] = emptyInventory.get(str(k))
        else:
            inventory[str(k)] = emptyInventory.get(str(k)) + inventory.get(str(k))

    return inventory



def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + '  ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))




inv = {'gold coin':42, 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)