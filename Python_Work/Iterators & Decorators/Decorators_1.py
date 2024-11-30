def greeting_custom(greeting, *names, **info):
    for name in names:
        print(greeting, name,"!")
    print("Additional Info:", info)

# Calling the function
greeting_custom("Hello", "Devaiah", "Dharshu",
                "Akash", city="Mysore", age=25)
