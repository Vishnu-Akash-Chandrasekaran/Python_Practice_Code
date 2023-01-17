with open("city_data.txt",'a') as f:
    f.write("Bangalore\n")
    f.write("Namakkal\n")
    f.write("Karur\n")
    print("Is file closed: ",f.closed)

print("Is file closed: ",f.closed)
