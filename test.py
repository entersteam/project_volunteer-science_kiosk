def rent_amount(item, student_id):
    user_db = user_collection.find_one({"student_id" : student_id})
    if item == 'motor':
        user_db = user_collection.find_one({"student_id" : student_id})
        amount = user_db['rent_0']
        return amount
    elif item == 'light_bulb':
        user_db = user_collection.find_one({"student_id" : student_id})
        amount = user_db['rent_1']
        return amount
    elif item == 'tape':
        user_db = user_collection.find_one({"student_id" : student_id})
        amount = user_db['rent_2']
        return amount
    elif item == 'wire':
        user_db = user_collection.find_one({"student_id" : student_id})
        amount = user_db['rent_0']
        return amount

  def no_item(student_id):
    user_db = user_collection.find_one({"student_id" : student_id})
    if user_db['rent_0'] == 0 and user_db['rent_1'] == 0 and user_db['rent_2'] == 0 and user_db['rent_3'] == 0:
        return False
    else:
        return True


def rent(student_id, item, amount):
    user_db = user_collection.find_one({"student_id" : student_id})
    item_db = items_collection.find_one({"item_name" : item})
    can_rent = item_db['can_rent']
    now_rent = item_db['now_rent']
    
    if item == 'motor':
        user_collection.update_one({'student_id': student_id }, {'$set' : {'rent_0' : now_rent + amount}})
        items_collection.update_one({"item_name" : item}, {"$set" : {"can_rent" : can_rent - amount , "now_rent" : now_rent + amount}})

    elif item == 'light_bulb':
        user_collection.update_one({'student_id': student_id }, {'$set' : {'rent_1' : now_rent + amount}})
        items_collection.update_one({"item_name" : item}, {"$set" : {"can_rent" : can_rent - amount , "now_rent" : now_rent + amount}})

    elif item == 'tape':
        user_collection.update_one({'student_id': student_id }, {'$set' : {'rent_2' : now_rent + amount}})
        items_collection.update_one({"item_name" : item}, {"$set" : {"can_rent" : can_rent - amount , "now_rent" : now_rent + amount}})

    elif item == 'wire':
        user_collection.update_one({'student_id': student_id }, {'$set' : {'rent_3' : now_rent + amount}})
        items_collection.update_one({"item_name" : item}, {"$set" : {"can_rent" : can_rent - amount , "now_rent" : now_rent + amount}})
