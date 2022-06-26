command_and_number = input()
command_and_number_list = command_and_number.split("||")
fuel = int(input())
ammo = int(input())
for x in command_and_number_list:
    com_and_num_list = x.split(" ")
    if com_and_num_list[0] == "Travel":
        if fuel < int(com_and_num_list[1]):
            print("Mission failed.")
            break
        else:
            fuel -= int(com_and_num_list[1])
            print(f"The spaceship travelled {com_and_num_list[1]} light-years.")
            continue
    if com_and_num_list[0] == "Enemy":
        if ammo >= int(com_and_num_list[1]):
            ammo -= int(com_and_num_list[1])
            print(f"An enemy with {com_and_num_list[1]} armour is defeated.")
            continue
        elif ammo < int(com_and_num_list[1]):
            if fuel < int(com_and_num_list[1]) * 2:
                print("Mission failed.")
                break
            else:
                print(f"An enemy with {com_and_num_list[1]} armour is outmaneuvered.")
                fuel -= int(com_and_num_list[1]) * 2
                continue

    if com_and_num_list[0] == "Repair":
        fuel += int(com_and_num_list[1])
        ammo += int(com_and_num_list[1]) * 2
        print(f"Ammunitions added: {int(com_and_num_list[1]) * 2}.")
        print(f"Fuel added: {com_and_num_list[1]}.")
        continue
    if com_and_num_list[0] == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
