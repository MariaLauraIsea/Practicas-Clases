from vehicle import Vehicle


def main():
    vehicle=Vehicle('toyota','yaris','green',2022)
    print(vehicle.color)
    print(vehicle.get_brand())


main()