import sys, getopt, datetime


def main(argv):
    usage = "Usage: totalMinutes.py -s <Start Time> -e <End Time>"
    dateTimeFormat = "%d/%b/%y %I:%M%p"
    try:
        opts, args = getopt.getopt(argv,"s:e:",["startTime=","endTime="])
    except getopt.GetoptError as err:
        print(err)
        print (usage)
        sys.exit(2)

    if len(opts) == 0:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-s":
            startTime = datetime.datetime.strptime(arg, dateTimeFormat)
        if opt == "-e":
            endTime = datetime.datetime.strptime(arg, dateTimeFormat)

    diff = endTime - startTime
    minutes = diff.total_seconds() / 60
    print(minutes)

if __name__ == "__main__":
   main(sys.argv[1:])

