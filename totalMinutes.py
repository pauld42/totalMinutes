import sys, getopt, datetime


def main(argv):

    try:
        opts, args = getopt.getopt(argv,"s:e:",["startTime=","endTime="])
    except getopt.GetoptError as err:
        print(err)
        print ("Usage: totalMinutes.py -s <Start Time> -e <End Time>")
        sys.exit(2)

    if len(opts) == 0:
        print("Usage: totalMinutes.py -s <Start Time> -e <End Time>")
        sys.exit(2)

    startTime = ""
    endTime = ""

    for opt, arg in opts:
        if opt == "-s":
            startTime = datetime.datetime.strptime(arg,"%d/%b/%y %I:%M%p")
        if opt == "-e":
            endTime = datetime.datetime.strptime(arg,"%d/%b/%y %I:%M%p")

    diff = endTime - startTime
    minutes = diff.total_seconds() / 60
    print(minutes)

if __name__ == "__main__":
   main(sys.argv[1:])

