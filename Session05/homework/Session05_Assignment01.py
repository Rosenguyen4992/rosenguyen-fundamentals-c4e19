inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dragger', 'bedroll', 'bread loaf']
}

# Add a key to inventory called 'pocket'then Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print (inventory)

# Then .remove('dagger') from the list of items stored under the 'backpack' key
inventory['backpack'].remove('dragger')
print (inventory)

# Add 50 to the number stored under the 'gold' key 
update_gold = inventory['gold'] + 50
inventory['gold'] = update_gold
print (inventory)
