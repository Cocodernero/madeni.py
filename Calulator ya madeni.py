def main():
    print("Hii ni cal ya madeni ")
    print("")


    principal = float(input("weka deni hapa: "))
    apr = float(input("weka annual interest rate: "))
    mwaka = int(input("weka nambari ya mwaka: "))

    interest_ya_mwezi = apr /1200
    nambari_ya_mwezi = mwaka * 12
    malipo_ya_mwezi = principal * interest_ya_mwezi / (1 - (1+ interest_ya_mwezi) ** (-nambari_ya_mwezi))


    print("Deni unafaa kulipaa kila mwezi ni :$ %.2f " %  malipo_ya_mwezi)

main()

