def display(**n):
    print("Record Info:")
    for k,v in n.items():
        print(k,"...........",v)

display(name="Cisco",devicetype="Router")
display(name="Checkpoint",Firewall="YES")
display(name="F5",ADC="True",LoadBalancer="YES")
