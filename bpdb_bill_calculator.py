
def life_line(units):
    # Unit 0 to 50 --> price 4.63
    total_bill = units * 4.63
    return total_bill


def step1(units):
    # Unit up to 50 --> price 5.26
    total_bill = units * 5.26
    return total_bill


def step2(units):
    # Unit up to 75 --> price 8.50
    total_bill = (units - 75) * 8.5 + step1(75)
    return total_bill


def step3(units):
    # Unit up to 200 --> price 9.10
    total_bill = (units - 200) * 9.1 + step2(200)
    return total_bill


def step4(units):
    # Unit up to 300 --> price 9.62
    total_bill = (units - 300) * 9.62 + step3(300)
    return total_bill


def step5(units):
    # Unit up to 400 --> price 15.01
    total_bill = (units - 400) * 15.01 + step4(400)
    return total_bill


def step6(units):
    # Unit up to 600 --> price 17.35
    total_bill = (units - 600) * 17.35 + step5(600)
    return total_bill


def main():
    try:
        # User Input
        total_units = float(input("Total Units: "))
        if total_units < 0:
            raise Exception("Negative Units! Unit can't be negative.")
        demand_load = int(input("Demand Load in KW(Its generally 1 or 2 in LT-A): "))
        if demand_load < 0:
            raise Exception("Invalid Demand Load!")
    except ValueError:
        print("Invalid number!")
    except Exception as e:
        print(e)

    else:
        # Output variable
        total_bill = 0
        demand_charge = demand_load * 42
        vat = 0
        payable_amount = 0

        if total_units > 600:
            total_bill = step6(total_units)

        elif total_units > 400:
            total_bill = step5(total_units)

        elif total_units > 300:
            total_bill = step4(total_units)

        elif total_units > 200:
            total_bill = step3(total_units)

        elif total_units > 75:
            total_bill = step2(total_units)

        elif total_units > 50:
            total_bill = step1(total_units)
        else:
            total_bill = life_line(total_units)


        vat = total_bill * (5/100)
        payable_amount = total_bill + demand_charge + vat
        payable_amount_with_meter_rent = payable_amount + 40

        # final output
        print("="*40)
        print("\tElectricity Bill")
        print("="*40)
        print(f"\nTotal Units: {total_units}\nDemand Load: {demand_load} KW\nEnergy Charge: {total_bill: .2f} Tk\nDemand Charge: {demand_charge} Tk\nVat: {vat: .2f}")
        print("-"*40)
        print(f"Total Amount: {payable_amount: .2f} Tk")
        print(f"Total Amount: {payable_amount_with_meter_rent: .2f} Tk(Include Meter rent)\n")
        print("="*40)
    



main()




