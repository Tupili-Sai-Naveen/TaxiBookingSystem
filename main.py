from taxi_booking import TaxiBooking

def main():
    taxi_booking = TaxiBooking()
    loop = True
    
    while loop:
        print("Choose any one\n1. Book Taxi\n2. Display Details\n3. Exit")
        try:
            n = int(input())
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
        
        if n == 1:
            try:
                pickup_location = input("Enter Pickup Location (A-Z): ").strip().upper()
                drop_location = input("Enter Drop Location (A-Z): ").strip().upper()
                pickup_time = int(input("Enter Pickup Time (0-23): "))
                result = taxi_booking.book_taxi(pickup_location, drop_location, pickup_time)
                print(result)
            except ValueError as e:
                print(f"Invalid input: {e}")
        elif n == 2:
            taxi_booking.display_details()
        elif n == 3:
            loop = False
            print("\tThank You!!!")
        else:
            print("Invalid choice. Please choose between 1, 2, and 3.")

if __name__ == "__main__":
    main()
