list = ["book", "b", "philipines", "dragonfruit", "mango"]
print(f"Original list:{list}")
index = int(input("Enter index to update: "))
newitem = input("Enter new item: ")
slice1 = int(input("Enter slice range 1: "))
slice2 = int(input("Enter slice range 2: "))
item = input("Enter search item: ")
def additem(s,n,d):
    if item in list[s:n]:
        return(f"Sliced List:({s},{n}){list[s:n]}, Search result (from sliced array): {d} is found in sliced list")
    else:
        return(f"{d} is not found in list")
print(f"Index to update: {index}, new item: {newitem}")
searchedlist = additem(slice1, slice2, item)
print(searchedlist)
updatedlist = list.copy()
updatedlist[index] = newitem
print(f"Updated list: {updatedlist}")