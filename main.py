import argparse
from analyser import pico_y_placa_predictor

if __name__ == '__main__':
    # usage: main.py [-h] -p PLATE -d DATE [-t TIME] [-l LOCALE] [-f FORMAT]
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--plate", type=str, required=True,
                    help="Input the plate to be analysed")
    ap.add_argument("-d", "--date", type=str, required=True,
                    help="date to validate")
    ap.add_argument("-t", "--time", type=str, default=None,
                    help="time of the day to check, if not given it takes current time")
    ap.add_argument("-l", "--locale", type=str, default=None,
                    help="locale to use it helps if the system has different locale")
    ap.add_argument("-f", "--format", type=str, default=None,
                    help="format to parse date and time")
    args = vars(ap.parse_args())

    response = pico_y_placa_predictor(args['plate'], args['date'], args['time'])

    if response:
        print("You can circulate freely")
    else:
        print("Better take a cab!, if you get seen your car is going to be detained.")