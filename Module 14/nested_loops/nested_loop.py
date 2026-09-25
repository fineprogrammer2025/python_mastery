network_carrier = ['MTN', 'GLO', 'AIRTEL']
devices = ['5g_router', '5g_mifi', '4g_mifi']
for carrier in network_carrier:
    for device in devices:
        print(carrier, device)
    print("\n")
print("------------")

numbers = [1, 2, 3]
letters = ["a", "b", "c"]
for x in numbers:
    print(x)
    for y in letters:
        print(y)
    print("\n")
print("------------")