
from fix import Fix


fix_message = "8=FIX.4.4 34=1080 49=TESTBUY1 35=D 11=636730640278898634 38=7000 55=MSFT 60=20180920-18:14:19.492"

if __name__ == '__main__':
    fix_object = Fix()
    fix_object.parse_str(fix_message)
    print(fix_object.ticker)