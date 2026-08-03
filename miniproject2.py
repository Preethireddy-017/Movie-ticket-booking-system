# ==========================================
# MOVIE TICKET BOOKING SYSTEM
# ==========================================
movies = []
genre = []
duration = []
price = []
shows = []
seatlayout = []
bookings = []
userdata = []
cartdata = []

admin_username = "admin"
admin_password = "admin123"

while True:

    print()
    print("*" * 50)
    print("*" * 8, "MOVIE TICKET BOOKING SYSTEM", "*" * 8)
    print("*" * 50)

    print("1. Admin")
    print("2. User")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    # ==========================================
    # ADMIN LOGIN
    # ==========================================
    if choice == 1:
        username = input("Enter Admin Username : ")
        password = input("Enter Admin Password : ")
        if username == admin_username and password == admin_password:
            print()
            print("Login Successful")
            while True:
                print()
                print("*" * 40)
                print("ADMIN MENU")
                print("*" * 40)

                print("1. Add Movie")
                print("2. View Movies")
                print("3. Delete Movie")
                print("4. Add Show Timings")
                print("5. Delete Show Timings")
                print("6. Manage Seats")
                print("7. View Bookings")
                print("8. Logout")

                admin_choice = int(input("Enter Choice : "))
                if admin_choice == 1:
                    while True:
                        movie = input("Enter Movie Name : ")
                        g = input("Enter Genre : ")
                        d = input("Enter Duration : ")
                        p = int(input("Enter Ticket Price : "))
                        movies.append(movie)
                        genre.append(g)
                        duration.append(d)
                        price.append(p)
                        print("\nMovie Added Successfully")
                        choice = input("\nDo you want to add another movie? (yes/no): ").lower()
                        if choice == "no":
                            break
                elif admin_choice == 2:
                    if len(movies) == 0:
                        print("\nNo Movies Available")
                    else:
                        print()
                        print("-" * 75)
                        print(f"{'S.No':<8}{'Movie Name':<20}{'Genre':<15}{'Duration':<15}{'Price'}")
                        print("-" * 75)
                        for i in range(len(movies)):
                            print(f"{i+1:<8}{movies[i]:<20}{genre[i]:<15}{duration[i]:<15}{price[i]}")
                        print("-" * 75)
                elif admin_choice == 3:
                    if len(movies) == 0:
                        print("\nNo Movies Available")
                    else:
                        print("\nAvailable Movies")
                        for movie in movies:
                            print(movie)
                        while True:
                            movie_name = input("\nEnter Movie Name to Delete : ")
                            if movie_name in movies:
                                index = movies.index(movie_name)
                                movies.pop(index)
                                genre.pop(index)
                                duration.pop(index)
                                price.pop(index)
                                print("\nMovie Deleted Successfully")
                            else:
                                print("\nMovie Not Found")
                            choice = input("\nDo you want to delete another movie? (yes/no): ").lower()
                            if choice == "no":
                                break
                elif admin_choice == 4:
                    if len(movies) == 0:
                        print("\nNo Movies Available")
                    else:
                        while True:
                            movie_name = input("\nEnter Movie Name : ")
                            if movie_name in movies:
                                morning = input("Enter Morning Show : ")
                                afternoon = input("Enter Afternoon Show : ")
                                evening = input("Enter Evening Show : ")
                                shows.append([movie_name, morning, afternoon, evening])
                                print("\nShow Timings Added Successfully")
                            else:
                                print("\nMovie Not Found")
                            ch = input("\nDo you want to add another show timing? (yes/no): ").lower()
                            if ch == "no":
                                break
                elif admin_choice == 5:
                    if len(shows) == 0:
                        print("\nNo Show Timings Available")
                    else:
                        print("\nAvailable Movies with Show Timings")
                        for show in shows:
                            print(show[0])
                        while True:
                            movie_name = input("\nEnter Movie Name to Delete Show Timings : ")
                            found = False
                            for show in shows:
                                if show[0].lower() == movie_name.lower():
                                    shows.remove(show)
                                    print("\nShow Timings Deleted Successfully")
                                    found = True
                                    break
                                if found == False:
                                    print("\nMovie Show Timings Not Found")
                                ch = input("\nDo you want to delete another show timing? (yes/no): ").lower()
                                if ch == "no":
                                    break
                elif admin_choice == 6:
                    if len(movies) == 0:
                        print("\nNo Movies Available")
                    else:
                        while True:
                            movie_name = input("\nEnter Movie Name : ").strip()
                            if movie_name in movies:
                                found = False
                                # Check whether seat layout already exists
                                for seat in seatlayout:
                                    if seat[0] == movie_name:
                                        found = True
                                        print("\nSeat Layout Already Exists")
                                        break
                                # Create seats if not found
                                if found == False:
                                    seats = []
                                    rows = ["A", "B", "C", "D"]
                                    for row in rows:
                                        for num in range(1, 6):
                                            seats.append(row + str(num))
                                    seatlayout.append([movie_name, seats])
                                    print("\nSeats Created Successfully")
                            else:
                                print("\nMovie Not Found")
                            ch = input("\nDo you want to manage another movie seats (yes/no): ").lower()
                            if ch == "no":
                                break
                elif admin_choice == 7:
                    if len(bookings) == 0:
                        print("\nNo Bookings Available")
                    else:
                        print()
                        print("-" * 105)
                        print(f"{'Booking ID':<15}{'User Name':<15}{'Movie':<20}{'Show Time':<15}{'Seats':<10}{'Amount':<10}{'Status'}")
                        print("-" * 105)
                        for booking in bookings:
                            print(f"{booking[0]:<15}{booking[1]:<15}{booking[2]:<20}{booking[3]:<15}{booking[4]:<10}{booking[5]:<10}{booking[6]}")
                        print("-" * 105)
                elif admin_choice == 8:
                    print()
                    print("*" * 40)
                    print("Admin Logged Out Successfully")
                    print("*" * 40)
                    break
    # ==========================================
    # USER SECTION
    # ==========================================
    elif choice == 2:
        while True:
            print()

            print("*" * 40)
            print("USER MENU")
            print("*" * 40)

            print("1. Register")
            print("2. Login")
            print("3. Back")

            user_choice = int(input("Enter Choice : "))

            # =============================
            if user_choice == 1:
                name = input("Enter Name : ")
                email = input("Enter Email : ")
                mobile = input("Enter Mobile : ")
                password = input("Create Password : ")
                userdata.append([name, email, mobile, password])

                print()
                print("Registration Successful")

            # =============================

            elif user_choice == 2:
                email = input("Enter Email : ")
                password = input("Enter Password : ")
                found = False
                for user in userdata:
                    if user[1] == email and user[3] == password:
                        found = True
                        print()
                        print("Login Successful")
                        while True:
                            print()

                            print("*" * 40)
                            print("CUSTOMER MENU")
                            print("*" * 40)

                            print("1. View Movies")
                            print("2. View Show Timings")
                            print("3. Book Ticket")
                            print("4. View Cart")
                            print("5. Cancel Ticket")
                            print("6. Logout")
                            customer_choice = int(input("Enter Choice : "))
                            # ==========================================
                            # CUSTOMER MENU OPTIONS
                            # ==========================================
                            if customer_choice == 1:
                                if len(movies) == 0:
                                    print("\nNo Movies Available")
                                else:
                                    print("\n" + "-" * 75)
                                    print(f"{'S.No':<8}{'Movie Name':<20}{'Genre':<15}{'Duration':<15}{'Price'}")
                                    print("-" * 75)
                                    for i in range(len(movies)):
                                        print(f"{i+1:<8}{movies[i]:<20}{genre[i]:<15}{duration[i]:<15}{price[i]}")
                                    print("-" * 75)
                            elif customer_choice == 2:
                                if len(shows) == 0:
                                    print("\nNo Show Timings Available")
                                else:
                                    print("\n" + "-" * 70)
                                    print(f"{'Movie':<20}{'Morning':<15}{'Afternoon':<15}{'Evening'}")
                                    print("-" * 70)
                                    for show in shows:
                                        print(f"{show[0]:<20}{show[1]:<15}{show[2]:<15}{show[3]}")
                                    print("-" * 70)
                            elif customer_choice == 3:
                                movie_name = input("\nEnter Movie Name : ")
                                found = False
                                for seat in seatlayout:
                                    if seat[0] == movie_name:
                                        found = True
                                        print("\nAvailable Seats\n")
                                        count = 0
                                        for s in seat[1]:
                                            print(f"{s:<5}", end=" ")
                                            count += 1
                                            if count % 5 == 0:
                                                print()
                                        show_time = input("\nEnter Show Time : ")
                                        selected_seats = []
                                        while True:
                                            seat_no = input("\nEnter Seat Number : ").upper()
                                            if seat_no in seat[1]:
                                                selected_seats.append(seat_no)
                                                seat[1].remove(seat_no)
                                                print(f"{seat_no} Added Successfully")
                                            else:
                                                print("Seat Not Available")
                                            ch = input("\nDo you want to add another seat? (yes/no): ").lower()
                                            if ch == "no":
                                                break
                                        if len(selected_seats) > 0:
                                            booking_id = len(bookings) + 101
                                            movie_index = movies.index(movie_name)
                                            amount = price[movie_index] * len(selected_seats)
                                            bookings.append([
                                                booking_id,
                                                user[0],
                                                movie_name,
                                                show_time,
                                                ",".join(selected_seats),
                                                amount,
                                                "Confirmed"
                                            ])
                                            cartdata.append([
                                                booking_id,
                                                user[0],
                                                movie_name,
                                                show_time,
                                                ",".join(selected_seats),
                                                amount
                                            ])
                                            print("\nTicket Booked Successfully")
                                            print("Seats Booked :", ",".join(selected_seats))
                                            print("Total Amount :", amount)
                                        break
                                if found == False:
                                    print("\nMovie Not Found")            
                            elif customer_choice == 4:
                                if len(cartdata) == 0:
                                    print("\nCart Empty")
                                else:
                                    print("\n" + "-" * 70)
                                    print(f"{'Booking ID':<15}{'Movie':<20}{'Seat':<15}{'Amount'}")
                                    print("-" * 70)
                                    for cart in cartdata:
                                        if cart[1] == user[0]:
                                            print(f"{cart[0]:<15}{cart[2]:<20}{cart[3]:<15}{cart[4]}")
                                    print("-" * 70)
                            elif customer_choice == 5:
                                booking_id = int(input("\nEnter Booking ID : "))
                                found = False
                                for booking in bookings:
                                    if booking[0] == booking_id and booking[1] == user[0]:
                                        booking[6] = "Cancelled"
                                        found = True
                                        print("\nTicket Cancelled Successfully")
                                        break
                                if found == False:
                                    print("\nBooking ID Not Found")
                            elif customer_choice == 6:
                                print()
                                print("*" * 40)
                                print("User Logged Out Successfully")
                                print("*" * 40)
                                break
                            else:
                                print("\nInvalid Choice")
                            
            elif user_choice == 3:
                break
            else:
                print("Invalid Choice")
    elif choice == 3:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
