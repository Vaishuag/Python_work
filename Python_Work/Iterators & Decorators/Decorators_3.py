def both_args_kwargs(*args, **kwargs):
    print(f"Positional arguments (args): {args}")
    print(f"Keyword arguments (kwargs): {kwargs}")

both_args_kwargs(41, 23, 13, name="Dev", age=24)
