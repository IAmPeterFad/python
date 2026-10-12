country = "USA"

if country == "United States":
    print("US")
else:
    print("Unknown Country")

match country:
    case "United States" | "USA":
        print("US")
    case "India":
        print("IN")
    case "Nigeria":
        print("NG")
    case "Germany":
        print("DE")
    case _ :
        "Unknown Country"