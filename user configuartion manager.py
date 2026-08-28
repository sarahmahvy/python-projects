def add_setting(settings,pair):
    input_key=pair[0].lower()
    input_value=pair[1].lower()
    for key in settings:
        #key=key.lower()
        if input_key == key:
            found = True
            break
        else:
            found = False
        continue
    if found:
        return f"Setting '{input_key}' already exists! Cannot add a new setting with this name."
    if not found:
        new_setting={input_key:input_value}
        settings.update(new_setting)
        return f"Setting '{input_key}' added with value '{input_value}' successfully!"
        
        #print(settings)

def update_setting(settings,pair):
    input_key=pair[0].lower()
    input_value=pair[1].lower()
    for key in settings:
        #key=key.lower()
        if input_key == key:
            found = True
            break
        else:
            found = False
        continue
    if found:
        settings[input_key]=input_value
        return f"Setting '{input_key}' updated to '{input_value}' successfully!"
    if not found:
        
        return f"Setting '{input_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings,key):
    input_key=key.lower()
    for key in settings:
        #key=key.lower()
        if input_key == key:
            found = True
            break
        else:
            found = False
        continue
    if found:
        settings.pop(input_key)
        return f"Setting '{input_key}' deleted successfully!"
    if not found:
        return "Setting not found!"

def view_settings(settings):
    if settings == {}:
        return "No settings available."
    else:
        output = "Current User Settings:\n"
        #print("Current User Settings:")
        for setting, mode in settings.items():
            output += f"{setting.title()}: {mode}\n"
    return output


test_settings={
    'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'
}

User_input = ('background','blue')
add_setting(test_settings,User_input)
#print(test_settings)
add_setting(test_settings,User_input)
print(update_setting({'theme': 'light'},("theme","dark")))
#print(test_settings)
delete_setting(test_settings,'volume')
#print(test_settings)

print(view_settings(test_settings))