print("Company Valuation using Dividends or Freecashflow")

def main():
    n = 0 #number of years set at zero
    total_pv = 0 #pv set at zero to initialize the suming of pv to be used in for loop
    div = int(input("Enter the current dividend: ")) #this can be replaced with a freecashflow
    growth_change = int(input("""Does the dividend grow?
        1. yes
        2. no
        : """)) # allows user to choose route since calculation for intrinsic value can be done differently based on assumption that there is growth in dividends or not.
        
    if growth_change == 1:
        choice = int(input("""        1. constant growth
        2. two step change
        : """)) #this specifies the way tge profits grow, either with constant growth or changing growth after sometime
        
        if choice ==1:
            growth = float(input("Enter growth as decimal: "))
            int_rates = float(input("Enter cost of equity or interest rates: ")) #interest rates are also used as the cost of equity. one can also use WACC or CAPM
            mkt_value = (div * (1+ growth))/(int_rates - growth)   #this formula is used when given the current profit. consideration for an anticipated next year dividend is not done.
            print(f'market value: ', mkt_value)
            
        elif choice ==2:
            n_years = int(input("Enter years for the first growth: "))
            growth = float(input("Enter the first growth: "))
            growth2 = float(input("Enter the second growth: "))
            int_rates = float(input("Enter the cost of capital or interest rates: "))
            for year in range(1, n_years+1): # 1 is added to the years to ensure the iteration is done for exactly the number of years set by user. the starting point is 1 not zero to ensure realistic counting of years from 1 
                n += 1 # this ensures the n incrrases as iterations increase. the proceeding n's are already adjusted for
                dcf = 1/(1+int_rates)**n
                future_div = div * (1 + growth)**n #this calculates the next year's expected dividend
                pv= future_div* dcf
                total_pv += pv
                print(f'year: {year}')
                print(f'   DCF: {dcf}')
                print(f'   Estimated Dividends: {future_div}')
                print(f'   PV: {pv}')
                print(f'   NPV: {total_pv}')
                
            dcf2 = 1/(1+int_rates)**n_years
            f_div = div * (1 + growth)**n_years
            mkt_value_nyears = f_div/(int_rates - growth2)
            market_value = mkt_value_nyears / dcf2
                
            intrinsic_value = total_pv + market_value
            print(f"intrinsic value: {intrinsic_value}")
        else:
            print("Enter valid input")
            
    elif growth_change ==2:
        int_rates = float(input("Enter cost of capital or interest rate as decimal"))
        market_value =  div/int_rates
        print(f'intrinsic value: ', market_value)
    else:
        print("Enter valid input")
        
if __name__ == "__main__":
    main()    
        