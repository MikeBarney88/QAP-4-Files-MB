# Description: One Stop Insurance Co.
# Author: Michael Barney
# Date(s): Nov 18, 24.


# Define required libraries.
import datetime
import FormatValues as FV


# Define program constants.

CUR_DATE = datetime.datetime.now()
BASE_PREM = 869.00
ADD_CAR_DSC = .75
EXT_LIAB = 130.00
GLASS_COV = 86.00
LOAN_COV = 58.00
HST_RATE = .15
PROCESS_FEE = 39.99


# Define program functions.

# Gather customer info.

def CustInfo():
    
    CustFirst = input("Enter the customer first name: ").title()
    CustLast = input("Enter the customer last name: ").title()
    StAdd = input("Enter the street address: ").capitalize()
    City = input("Enter the city: ").title()

    PROV_LST = ["NS", "NB", "NL", "QP", "ON", "PE", "AB", "SK", "BC", "MB", "NT", "NU", "YK"]
    while True:
        Prov = input("Enter the province (XX): ").upper()
        if Prov == "":
            print("   Data Entry Error - Province cannot be blank.")
        elif len(Prov) != 2:
            print("   Data Entry Error - Province is a 2 character code only.")
        elif Prov not in PROV_LST:
            print("   Data Entry Error - Province is not valid.")
        else:
            break

    Postal = input("Enter the postal code(A1A1A1): ").upper()
    PhoneNum = input("Enter the phone number(0000000000): ")
    print()

    return CustFirst, CustLast, StAdd, City, Prov, Postal, PhoneNum

# Calculate insurance premiums.

def CalcPrem (NumCars):

   BasePrem = BASE_PREM
   AddCars = ((NumCars - 1) * BASE_PREM) * ADD_CAR_DSC
   TotPrem = BasePrem + AddCars

   return TotPrem 

# Claims list function.

def ClaimsInfo():
    Claims = []
    while True:

        ClaimNum = input("Enter the claim number(00000): ")

        ClaimDate = input("Enter the claim date(YYYY-MM-DD): ")

        ClaimAmt = input("Claim amount of previous claim: ")
        ClaimAmt = float(ClaimAmt)
        
        
        Claims.append((ClaimNum, ClaimDate, ClaimAmt))

        MoreClaims = input("Do you have more claims to enter? (Y/N): ").upper()
        if MoreClaims == "N":
            break
    
    return Claims

# Main program starts here.

while True:
    
    # Gather user inputs.

    CustFirst, CustLast, StAdd, City, Prov, Postal, PhoneNum = CustInfo()

    # Vehicle and Insurance inputs.

    NumCars = input("Enter the number of cars being insured: ")
    NumCars = int(NumCars)
    print()
    ExtraLibFee = 0.00
    ExtraLibMsg = "No"
    ExtraLib = "Y" #input("Does the customer want extra liability( Y / N ): ").upper()
    if ExtraLib == "Y":
        ExtraLibMsg = "Yes"
        ExtraLibFee = EXT_LIAB
    else:
        break

    OptGlassFee = 0.00
    OptGlassMsg = "No"
    OptGlass = "Y" #input("Does the customer want glass coverage( Y / N ): ").upper()
    if OptGlass == "Y":
        OptGlassMsg = "Yes"
        OptGlassFee = GLASS_COV
    else:
        break

    OptLonerFee = 0.00
    OptLonerMsg = "No"
    OptLoner = "Y" #input("Does the customer want loner coverage( Y / N ): ").upper()
    if OptLoner == "Y":
        OptLonerMsg = "Yes"
        OptLonerFee = LOAN_COV
    else: 
        break

    # Inputs for payments Full or Monthly with down payment.

    PayLst = ["Full", "Monthly"]
    while True:
        Payment = input("how does the customer want to pay( Full / Monthly ): ").title()
        if Payment not in PayLst:
            print()
            print("     Data Entry Error - Payment Option must be Full or Monthly... ")
            print()
        else:
            break
    

    if Payment == "Monthly":
        PayMsg = "Monthly payments made over 8 months."
        
        while True:
            DownPayMsg = "No"
            DownPayAmt = 0.00
            DownPay = input("Does the customer want to make a down payment(Y/N): ").upper()
            if DownPay == " ":
                print()
                print("     Data Entry Error - Down Payment must be (Y or N)... ")
                print()
            else:
                break

        if DownPay == "Y":
            DownPayMsg = "Yes"
            while True:
                try:
                    DownPayAmt = input("Enter the amount of down payment: ")
                    DownPayAmt = float(DownPayAmt)
                except:
                    print()
                    print("     Data Entry Error - Down Payment must be a number... ")
                    print()
                else:
                    break
                    

    elif Payment == "Full":
        PayMsg = "Payed in full! Thank You."
        DownPayAmt = 0.00
        DownPayMsg = "No"



    print()

    Claims =  ClaimsInfo()

    # Calculations.
    
    TotPrem = CalcPrem(NumCars)

    ExtraLibTot = ExtraLibFee * NumCars

    GlassCovTot = OptGlassFee * NumCars

    OptLonerTot = OptLonerFee * NumCars

    TotExtras = ExtraLibTot + GlassCovTot + OptLonerTot

    SubTot = TotPrem + TotExtras

    HST = SubTot * HST_RATE

    TotCost = SubTot + HST

    if Payment == "Monthly":
        if DownPay == "Y":
            MonthPayFee = (TotCost - DownPayAmt + PROCESS_FEE) / 8
        else: 
            MonthPayFee = (TotCost + PROCESS_FEE) / 8


    # Invoice Dates.

    InvDate = datetime.datetime.strftime(CUR_DATE, "%Y-%m-%d")
    InvYear = CUR_DATE.year
    InvMon = CUR_DATE.month
    InvDay = CUR_DATE.day

    if InvMon == 12:
        FirstPayMon = 1
        FirstPayYear = InvYear + 1
    else:
        FirstPayMon = InvMon + 1
        FirstPayYear = InvYear
    
    FirstPay = datetime.date(FirstPayYear, FirstPayMon, 1)



    # Display results
    print()
    print(f"       One Stop Insurance Company")
    print()
    print(f"--------------------------------------")
    print(f"Invoice date:               {FV.FDateS(CUR_DATE):<9s}")
    print()
    print(f"First Name:                 {CustFirst:>10s}")
    print(f"Last Name:                  {CustLast:>10s}")
    print()
    print(f"Street Address:       {StAdd:>15s}")
    print(f"City:                       {City:>10s}")
    print(f"Province:                           {Prov:>2s}")
    print(f"Postal code:                    {Postal:>6s}")
    print(f"Phone number:               {PhoneNum:>8s}")
    print()
    print(f"--------------------------------------")
    print()
    print(f"Number of cars to insure:           {NumCars:>2d}")
    print()
    print(f"Extra liability coverage:          {ExtraLibMsg:>3s}   ")
    print(f"Glass coverage:                    {OptGlassMsg:>3s}    ")
    print(f"Loaner car coverage:               {OptLonerMsg:>3s} ")
    print()
    print(f"Extra liability cost:         {FV.FDollar2(ExtraLibFee):>8s}")
    print(f"Glass coverage cost:          {FV.FDollar2(OptGlassFee):>8s}")
    print(f"Loaner car cost:              {FV.FDollar2(OptLonerFee):>8s}")
    print(f"                             ---------")
    print(f"Total extra coverage cost:    {FV.FDollar2(TotExtras):>8s}")
    print(f"Total premium cost:          {FV.FDollar2(TotPrem):>8s}")
    print(f"                             ---------")
    print(f"Subtotal:                    {FV.FDollar2(SubTot):>8s}")
    print(f"Taxes:                        {FV.FDollar2(HST):>8s}")
    print(f"                             ---------")
    print(f"Total Charges:               {FV.FDollar2(TotCost):>8s}")
    print(f"--------------------------------------")
    print(f"               Payment                ")
    print()
    print(f"Payment method:                {Payment:>7s}")
    if Payment != "Full":
        print(f"Down payment:                      {DownPayMsg:<3s}")
        print(f"Down payment amount:          {FV.FDollar2(DownPayAmt):>8s}")
    print(f"--------------------------------------")
    if Payment == "Full":
        print()
        print(f"     *{PayMsg}*")
    elif Payment == "Monthly":
        print(f"Monthly payments:             {FV.FDollar2(MonthPayFee):>8s}")
        print(f"First Payment Date:         {FV.FDateM(FirstPay):>10s}")
        print(f"--------------------------------------")
        print()
        print(f"*{PayMsg}*")




    print(f"")
    print(f"")
    print()
    print(f"           Claims History       ")
    print()
    print(f"  Claim         Claim         Claim   ")
    print(f"  Number         Date         Amount  ")
    print(f"--------------------------------------")
    for Claims in Claims:
        print(f"  {Claims[0]}       {Claims[1]}     {FV.FDollar2(Claims[2]):>8s}")
    print(f"--------------------------------------")

    AddCust = input("Do you want to enter the next customer? (Y/N): ").upper()
    if AddCust != "Y":
        break



    # Write the values to a data file for storage.


# Any housekeeping duties at the end of the program.