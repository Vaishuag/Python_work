def function(a, b, *args, c=10, **kwargs):
    print(f"a: {a}, b: {b}, c: {c}")
    print(f"Additional positional arguments: {args}")
    print(f"Additional keyword arguments: {kwargs}")

function(1, 2, 3, 4, 5, c=20, name="Vaishnavi",
         age=23,course='MCA',City='Mandya')
