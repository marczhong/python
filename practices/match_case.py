day = input("Enter a day of the week: ")

match day:
      case "Monday":
            print("It's the start of the week!")
      case "Tuesday":
            print("It's the second day of the week!")
      case "Wednesday":
            print("It's the middle of the week!")
      case "Thursday":
            print("It's almost the weekend!")
      case "Friday":
            print("It's the last day of the workweek!")
      case "Saturday" | "Sunday":
            print("It's the weekend!")
      case _:
            print("That's not a valid day of the week.")

