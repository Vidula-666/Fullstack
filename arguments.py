def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('apt')}")
shipping_label("Dr.","spongebob","squarepants","IIT",
               street="hghb",
               apt="bhg")
