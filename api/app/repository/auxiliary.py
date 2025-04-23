def check_data_id(model, id):
    data = model.query.filter(model.id  == id).first()

    if data is None:
        raise ValueError('Not found')
    
    return data

def check_data_name(model, name):
      
    data = model.query.filter(model.name_task  == name).first()

    if data is None:
        raise ValueError('Not found')
    
    return data

def check_data_username(model, name):
    data = model.query.filter(model.username  == name).first()

    if data is None:
        raise ValueError('Not found')
    
    return data

def check_data_category_id(model, category_id):
    data = model.query.filter(model.category_id == category_id).all()

    if not data:
        raise ValueError('Not found')
    
    return data

def check_data_task_id(model, task_id):
    timer = model.query.filter(model.task_id == task_id).all()

    if not timer:
        raise ValueError('Not found')

def update_data(model, obj):
    for key, value, in obj.items():
                if hasattr(model, key):
                    setattr(model, key, value)

    return model