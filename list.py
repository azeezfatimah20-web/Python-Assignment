# a = 10
# b = a

# print(id(a))
# print(id(b))

# b = b + 1
# print(b)
# print(id(b))

# # For List
# a = [10, 'idris', 20, 30, 50]
# print(a)
# print(type(a))
# print(a[0])
# print(a[-1])
# print(a[2])


# # to create an empty list
# a = []
# a.append(20)
# a.append(50)
# a.append(30)
# print(a)

# print(a[2])
# a.remove(20)
# print(a)

# # mutable collection
# b = [10, 20, 30, 40]
# print(b)
# print(id(b))
# # lets perform some changes in list
# b[0] = 60
# print(b)
# print(id(b))

# b[3] = 80
# print(b)
# print(id(b))

tools = ["Nmap", "Wireshark", "Burp Suite"]
print(tools)
tools.append("Metasploit")
print(tools)
print(tools[0])
tools.insert(0, "bug bounty")
print(tools)
