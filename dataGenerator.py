import mysql.connector
import random

addressid = [] 
personid = [] 
userid = [] 
passengerid = [] 
bankinfoid = [] 
transactionid = [] 
tripid = [] 
traintripnumber = [] 
compartmenttrainnumber = [] 
compartmenttraintripid = [] 
compartmentticketnumber = [] 
coachtrainnumber = [] 
coachtraintripid = [] 
coachticketnumber = [] 
airplaneid = [] 
flightnumber = [] 
classid = [] 
internationalflightticketid = [] 
domesticflightticketid = [] 
busid = [] 
bustripnumber = [] 
busticketnum = [] 
hotelid = [] 
roomid = [] 
reservid = [] 
commentid =[] 
protectorid = [] 
discountid = []

countries = ['Iceland', 'Guyana', 'Jersey', 'Denmark', 'Angola', 'Marshall Islands', 'Vanuatu', 'Moldova', 'Niger', 'Barbados']
cities = ['Lauraberg', 'Hudsonland', 'Port Alyssa', 'Williamsmouth', 'Kimstad', 'Hartport', 'East Brett', 'Williambury', 'Port Matthew', 'Teresastad']
streets = ['Davis', 'Bradford', 'Underwood', 'Estrada', 'Robinson', 'Gonzales', 'Lee', 'Jones', 'Gomez', 'Gonzalez', 'Ramos', 'Daniels', 'Mitchell', 'Neal', 'Thompson', 'Chavez', 'Smith', 'Torres', 'Marks']
alleys = ['Wesley', 'William', 'John', 'Melissa', 'Mark', 'Abigail', 'Cindy', 'Christine', 'Kevin', 'Max']
postal_codes = ['21907', '99472', '12091', '89207', '24116', '65853', '40085', '11294', '15471', '74250']
units = [26, 35, 12, 8, 10, 3, 13, 31, 29, 24]

first_names = ['Nicholas', 'Victoria', 'Ashley', 'Destiny', 'Lisa', 'Jeffrey', 'Bethany', 'Rebecca', 'Joshua', 'Sarah']
last_names = ['Peterson', 'Wallace', 'Anthony', 'Sutton', 'Williams', 'Sanders', 'Schneider', 'Parker', 'Walton', 'Clarke']
phone_numbers = ['001-537-544-6431x826', '(583)365-6336', '241-377-6041', '(509)830-9954', '(319)992-5255x8299', '(317)841-9497x609', '(255)940-8078', '782-922-9944x3114', '631-321-2603', '(431)765-0138x1815']
national_codes = [8613458403, 9620788272, 3217346337, 9324489425, 3918523492, 7569842696, 4808466053, 3047580356, 1487588412, 2670826052]
genders = ['male', 'female']
birth_dates = ['2000-12-25','1990-09-02','1995-11-14','1980-01-01','1970-11-08','1985-06-19','2003-09-05','2002-02-11','2010-12-04','1992-12-20']

credits = [100, 150, 200, 120, 124, 153, 290, 60, 48, 20]
passwords = ['5KkxqhOL', 'Qr7QHqFxy', 'RjMUMkQ8', 'd0_CsVkw1', '5_9lAvOAR', 'fBLHGwC4', 'Qg9Mm&Uf', 'hiCMacW6@9', '5ExpsIeR', '7cB6mcYJI']
usernames = ['JosephRodriguez', 'AprilSchmidt', 'SamMargaret BakerDVM', 'JosephSixton', 'JoelTorres', 'LoriTaylor', 'DawnWilliams', 'LisaHarris', 'MelindaWilson', 'JasonWood']
scores = [3,8,10,12,15,16,20,25,43,39,50]
emails = ['heather13@example.org', 'tmartin@example.net', 'jwashington@example.com', 'chandlermark@example.net', 'lglenn@example.com', 'jennifercastillo@example.com', 'vanessadavila@example.org', 'schneiderjustin@example.org', 'bennettmathew@example.net', 'janet62@example.org']

shaba_numbers = ['IR926759374957488562984922','IR618457932015647931024679','IR643152798210024631047982','IR973461520854296135784203','IR126432950870005427914134']
account_numbers = ['92675937495748','61845793201564','64315279821002','97346152085429','12643295087000','12457835656809','58734221099731','54844632195701']
card_numbers = ['9267593749574801','6184579320156436','6431527982100251','9734615208542930','1264329508700049','1245783565680977','5873422109973183','5484463219570120']

dates = ['2024-02-13','2024-02-15','2024-02-18','2024-02-19','2024-02-21','2024-02-22','2024-02-24','2024-02-25','2024-02-27','2024-02-28']
times = ['13:39','15:30','16:00','12:00','1:59','9:48','5:36','4:20','11:11','10:50']
transaction_amounts = [70, 91, 86, 32, 40, 100, 29, 45, 73, 10]
transaction_types = ['charge','withdraw']

transportation_types = ['airplane','bus','coach train','compartment train']
transaction_companies = ['Seir-o-Safar', 'Mahan', 'Iran Air', 'Homa', 'Turkish', 'Qatar', 'Emarates', 'Maral', 'Iran Gasht', 'Fadak']
capacities = [30,100,120,150,25,300,190,200,280,50]
amenities = ['breakfast','lunch','dinner','brunch','free wi-fi','WC','drink','snacks']

# Random datas:
train_trip_numbers = ['123pq', '258oc', '010qw', '563sz', '948ji', '910xe', '103pw', '239mg', '406is', '531td']
stopping_stations_lst = ['South Josefort', 'West Angela', 'Millerburgh', 'North Misty', 'North Walter', 'West James', 'East Alexandria', 'Smithburgh', 'Rickeybury', 'Michaelhaven']
images = ['image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8']
prices = [50, 100, 86, 32, 40, 69, 90, 45, 73, 120]
train_models = ['tram', 'LRV', 'commuter train', 'maglev train', 'high-speed', 'EMU', 'DMU']
flight_numbers = [435292, 328900, 195717, 657561, 168423, 376079, 652288, 550021, 589669, 832196]
terminals = [i for i in range(1,11)]
airports = ['Belgium Airport', 'Anguilla Airport', 'Eqypt Airport', 'Egypt Airport', 'England Airport', 'Australia Airport', 'Malaysia Airport', 'Aruba Airport', 'Benin Airport', 'Germany Airport']
flight_durations = ['7:20', '4:12', '06:13', '06:02', '02:49', '12:14', '07:55', '02:03', '13:33', '21:12']
airplane_numbers = [3843561, 5869896, 1960939, 2579833, 4128069, 2871629, 4465319, 8374858, 2503187, 3284386]
bus_trip_numbers = ['946wf4', '237iv4', '291al3', '314vs5', '217ec5', '533tm8', '463yx1', '984lo6', '240pn4', '971mt7']
bus_numbers = [6911, 6066, 4721, 2964, 7676, 4361, 7380, 3210, 7158, 1969]
compartment_train_numbers = ['167aq67', '843df08', '193ex99', '813tr07', '687om72', '499yb23', '496hu94', '357gk37', '439ln20', '980ez97']
coach_train_numbers = ['374824', '820153', '924380', '857934', '838802', '921212', '832443', '835442', '848122', '327941']
class_type = ['business', 'economy']
baggage_allowances = [20, 25, 30, 35, 40]
coach_ticket_numbers = ['90ads9452', '3qng81068', '46tos6434', '26prf2015', '28dhv2798', '73cct5024', '70pmn9962', '30eyu4865', '68ihj3981', '77kqw6371']
compartment_ticket_numbers = ['91lds9452', '3qia81368', '466os6ii2', '29ddr2015', '48dnv2753', '7m4ct5004', '70lqn0062', '30ecv2805', '93ohj1381', '10kxz0371']

compartment_beds_num = [4,6]
wagons_num = [i for i in range(4, 16)]
compartments_num = [i for i in range(10, 26)]
seats_num = [i for i in range(25,61)]

#coachـtrainـticket
ticket_numbers=[3678888,9086388,9025377,9081745,8980561,8975499,2255836,4099337,3677354,9088863]
wagon_num=[i for i in range(1, 16)]
compartment_num = [i for i in range(1,26)]
seat_num=[i for i in range(1,31)]

# International_flights_ticket
passport_nums  =[56734336,935696798,39764240,54436735,90534665,34226658,92343397,32367795,34244333,48940374]
passport_expiration_dates =['2023-13-29','2025-09-02','2024-20-14','2026-01-01','2023-11-08','2024-06-19','2025-09-05','2026-02-11','2025-12-04','2024-12-20']

#bus_ticket
bus_ticket_num =[234388,244334,987641,764933,296300,890800,119433,515892,949278,980040]

#Hotel
hotel_name=['Spinas','Laleh','Persia','Homa','Khorshid','Parsian','Atana','Tashrifat','Mahan','Mahsan']
hotel_stars=[i for i in range(2, 6)]
phone_num=['021-87936594','021-88965021','025-37969021','021-84965421','025-38965021','021-88243021','021-89642871','021-89275029','025-37902793','025-38795091','025-39056021']

arrival_time=['2024-02-12 08:35:00','2024-02-12 12:15:00','2024-02-12 15:45:00','2024-02-12 10:20:00','2024-02-12 18:00:00','2024-02-12 14:10:00','2024-02-12 11:55:00','2024-02-12 16:30:00','2024-02-12 09:40:00','2024-02-12 13:25:00']

departure_time=['2024-02-12 13:20:00','2024-02-12 16:55:00','2024-02-12 09:30:00','2024-02-12 12:10:00','2024-02-12 15:40:00',
'2024-02-12 11:15:00','2024-02-12 14:50:00','2024-02-12 17:25:00','2024-02-12 10:00:00','2024-02-12 13:35:00',]
hotel_facilities=['gym','pool','shop','resturant', 'cinema']
capacity=[2500,1000,2000,500,1500,700,1200,1700]

#Hotel_room
room_num=[230,210,250,340,110,120,140,220,327,225]
hotel_price=[100, 170, 150, 120, 80, 50, 30, 200, 250, 35]
beds_num=[i for i in range(1, 6)]
room_type=['single','double','twin', 'suite']


# hotel_reservation
reseve_date=['2024-02-13','2024-02-15','2024-02-18','2024-02-19','2024-02-21','2024-02-22','2024-02-24','2024-02-25','2024-02-27','2024-02-28']


def generate_unique_id(cursor, table_name, id_column):
    while True:
        cursor.execute(f"SELECT MAX({id_column}) FROM {table_name};")
        max_id = cursor.fetchone()[0]

        new_id = 1 if max_id is None else int(max_id) + 1

        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {id_column} = {new_id};")
        count = cursor.fetchone()[0]

        if count == 0:
            break

    return new_id


def insert_random_data(num_records):

    #address
    for _ in range(num_records):
        
        address_id = generate_unique_id(cursor, 'address', 'address_id')
        addressid.append(address_id)
        country = random.choice(countries)
        city = random.choice(cities)
        main_street = random.choice(streets)
        secondary_street = random.choice(streets)
        alley = random.choice(alleys)
        postal_code = random.choice(postal_codes)
        unit = random.choice(units) 

        query = "INSERT INTO address (address_id, country, city, main_street, secondary_street, alley, postal_code, unit) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (address_id, country, city, main_street, secondary_street, alley, postal_code, unit)
        cursor.execute(query, values)
        

    #trip
    for _ in range(num_records):
        
        trip_id = generate_unique_id(cursor, 'trip', 'trip_id')
        tripid.append(trip_id)
        transportation_type = random.choice(transportation_types)
        transportation_company = random.choice(transaction_companies)
        capacity = random.choice(capacities)
        origin = random.choice(cities)
        destination = random.choice(cities)
        departure_date = random.choice(dates)
        departure_time = random.choice(times) 
        arrival_time = random.choice(times)
        amenity = random.choice(amenities)

        query = "INSERT INTO trip (trip_id, transportation_type, transportation_company, capacity, origin, destination, departure_date, departure_time, arrival_time, amenity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (trip_id, transportation_type, transportation_company, capacity, origin, destination, departure_date, departure_time, arrival_time, amenity)
        cursor.execute(query, values)

    
    #compartment_train
    for _ in range(num_records):
        
        compartment_train_number = generate_unique_id(cursor, 'compartment_train', 'compartment_train_number')
        compartmenttrainnumber.append(compartment_train_number)
        train_model = random.choice(train_models)
        number_of_wagons = random.choice(wagons_num)
        number_of_train_compartments = random.choice(compartments_num)
        number_of_beds_in_each_compartment = random.choice(compartment_beds_num)

        query = "INSERT INTO compartment_train (compartment_train_number, train_model, number_of_wagons, number_of_train_compartments, number_of_beds_in_each_compartment) VALUES (%s, %s, %s, %s, %s)"
        values = (compartment_train_number, train_model, number_of_wagons, number_of_train_compartments, number_of_beds_in_each_compartment)
        cursor.execute(query, values)


    #coach_train
    for _ in range(num_records):
        
        coach_train_number = generate_unique_id(cursor, 'coach_train', 'coach_train_number')
        coachtrainnumber.append(coach_train_number)
        train_model = random.choice(train_models)
        number_of_wagons = random.choice(wagons_num)
        number_of_seats_in_each_carriage = random.choice(seats_num)
        number_of_all_seats = number_of_wagons*number_of_seats_in_each_carriage

        query = "INSERT INTO coach_train (coach_train_number, train_model, number_of_wagons, number_of_seats_in_each_carriage, number_of_all_seats) VALUES (%s, %s, %s, %s, %s)"
        values = (coach_train_number, train_model, number_of_wagons, number_of_seats_in_each_carriage, number_of_all_seats)
        cursor.execute(query, values)


    #airplane
    airplanemodel = ['Boeing 747', 'Airbus A380', 'Cessna 172', 'Lockheed Martin F-22 Raptor', 'Embraer E-Jets', 'Sukhoi Su-35', 'Bombardier Challenger 650', 'Airbus A320', 'Boeing 787 Dreamliner', 'Lockheed C-130 Hercules']
    numberofairplaneseats = [42,97,93,65,64,91,110,16,87,34]

    for _ in range(num_records):
        airplane_id = generate_unique_id(cursor, 'airplane', 'airplane_id')
        airplaneid.append(airplane_id)
        airplane_model = random.choice(airplanemodel)
        number_of_airplane_seats = random.choice(numberofairplaneseats)

        query = "INSERT INTO airplane (airplane_id, airplane_model, number_of_airplane_seats) VALUES (%s, %s, %s)"
        values = (airplane_id, airplane_model, number_of_airplane_seats)
        cursor.execute(query, values)


    #bus
    busmodel = ['Mercedes-Benz Sprinter', 'Volvo 9700', 'MAN Lions City', 'New Flyer Xcelsior', 'Scania OmniCity/OmniLink', 'Neoplan Tourliner', 'BYD Electric Bus', 'Alexander Dennis Enviro500', 'Temsa Safari HD', 'Iveco Daily Minibus']
    numberofbusseats = [42,97,93,65,64,91,110,16,87,34]
    buslicenseplatenumber = ['946wf4', '237iv4', '291al3', '314vs5', '217ec5', '533tm8', '463yx1', '984lo6', '240pn4', '971mt7']
    
    for _ in range(num_records):
        bus_id = generate_unique_id(cursor, 'bus', 'bus_id')
        busid.append(bus_id)
        bus_model = random.choice(busmodel)
        number_of_bus_seats = random.choice(numberofbusseats)
        bus_license_plate_number = random.choice(buslicenseplatenumber)

        query = "INSERT INTO bus (bus_id, bus_model, number_of_bus_seats, bus_license_plate_number) VALUES (%s, %s, %s, %s)"
        values = (bus_id, bus_model, number_of_bus_seats, bus_license_plate_number)
        cursor.execute(query, values)


    #person
    for _ in range(num_records):
        
        person_id = generate_unique_id(cursor, 'person', 'person_id')
        personid.append(person_id)
        f_name = random.choice(first_names)
        l_name = random.choice(last_names)
        phone_num = random.choice(phone_numbers)
        national_code = random.choice(national_codes)
        birthdate = random.choice(birth_dates)
        gender = random.choice(genders)
        address_id = random.choice(addressid) 

        query = "INSERT INTO person (person_id, first_name, last_name, phone_number, national_code, birth_date, gender, address_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (person_id, f_name, l_name, phone_num, national_code, birthdate, gender, address_id)
        cursor.execute(query, values)


    #hotel   
    hotelname=['Spinas','Laleh','Persia','Homa','Khorshid','Parsian','Atana','Tashrifat','Mahan','Mahsan']
    hotelstars=[5,5,3,5,4,5,4,3,2,4]
    hotelphone=['021-87936594','021-88965021','025-37969021','021-84965421','025-38965021','021-88243021','021-89642871','021-89275029','025-37902793','025-38795091','025-39056021']
    arrivaltime=['2024-02-12 08:35:00','2024-02-12 12:15:00','2024-02-12 15:45:00','2024-02-12 10:20:00','2024-02-12 18:00:00','2024-02-12 14:10:00','2024-02-12 11:55:00','2024-02-12 16:30:00','2024-02-12 09:40:00','2024-02-12 13:25:00']
    departuretime=['2024-02-12 13:20:00','2024-02-12 16:55:00','2024-02-12 09:30:00','2024-02-12 12:10:00','2024-02-12 15:40:00','2024-02-12 11:15:00','2024-02-12 14:50:00','2024-02-12 17:25:00','2024-02-12 10:00:00','2024-02-12 13:35:00',]
    facilities=['gym','pool','shop','resturant','pool','shop','resturant','gym','pool','gym']
    hotelcapacity=[2500,1000,2000,500,1500,700,1200,1700,2500,1000,2000]

    for _ in range(num_records):
        hotel_id = generate_unique_id(cursor, 'hotel', 'hotel_id')
        hotelid.append(hotel_id)
        hotel_name = random.choice(hotelname)
        hotel_stars = random.choice(hotelstars)
        telephone = random.choice(hotelphone)
        address_id = random.choice(addressid)
        arrival_time = random.choice(arrivaltime)
        departure_time = random.choice(departuretime)
        hotel_facilities = random.choice(facilities)
        hotel_image = random.choice(images) 
        capcity = random.choice(hotelcapacity)

        query = "INSERT INTO hotel (hotel_id, hotel_name, hotel_stars, telephone, address_id, arrival_time, departure_time, hotel_facilities, hotel_image, capcity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (hotel_id, hotel_name, hotel_stars, telephone, address_id, arrival_time, departure_time, hotel_facilities, hotel_image, capcity)
        cursor.execute(query, values)


    #users
    for _ in range(num_records):
        
        user_id = generate_unique_id(cursor, 'users', 'user_id')
        userid.append(user_id)
        credit = random.choice(credits)
        user_password = random.choice(passwords)
        username = random.choice(usernames)
        score = random.choice(scores)
        email = random.choice(emails)
        person_id = random.choice(personid) 

        query = "INSERT INTO users (user_id, credit, user_password, username, score, email) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (user_id, credit, user_password, username, score, email)
        cursor.execute(query, values)


    #passenger
    for _ in range(num_records):
        
        passenger_id = generate_unique_id(cursor, 'passenger', 'passenger_id')
        passengerid.append(passenger_id)
        person_id = random.choice(personid) 
        user_id = random.choice(userid)

        query = "INSERT INTO passenger (passenger_id, person_id, user_id) VALUES (%s, %s, %s)"
        values = (passenger_id, person_id, user_id)
        cursor.execute(query, values)


    #discount
    amountofdiscount = [50, 100, 86, 32, 40, 69, 90, 45, 73, 120]
    expiratiodate = ['2024-02-13','2024-02-15','2024-02-18','2024-02-19','2024-02-21','2024-02-22','2024-02-24','2024-02-25','2024-02-27','2024-02-28']
    minimumpurchaseamount = [50, 100, 86, 32, 40, 69, 90, 45, 73, 120]
    typeoftrip = ['air travel', 'train travel', 'bus travel']

    for _ in range(num_records):
        discount_id = generate_unique_id(cursor, 'discount', 'discount_id')
        discountid.append(discount_id)
        amount_of_discount = random.choice(amountofdiscount)
        expiration_date = random.choice(expiratiodate)
        minimum_purchase_amount = random.choice(minimumpurchaseamount)
        type_of_trip = random.choice(typeoftrip)
        user_id = random.choice(userid)

        query = "INSERT INTO discount (discount_id, amount_of_discount, expiration_date, minimum_purchase_amount, type_of_trip, user_id) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (discount_id, amount_of_discount, expiration_date, minimum_purchase_amount, type_of_trip, user_id)
        cursor.execute(query, values)


    #hotel_comment
    registration_time = ['2024-02-12 08:35:00','2024-02-12 12:15:00','2024-02-12 15:45:00','2024-02-12 10:20:00','2024-02-12 18:00:00','2024-02-12 14:10:00','2024-02-12 11:55:00','2024-02-12 16:30:00','2024-02-12 09:40:00','2024-02-12 13:25:00']
    registration_date = ['2024-02-13','2024-02-15','2024-02-18','2024-02-19','2024-02-21','2024-02-22','2024-02-24','2024-02-25','2024-02-27','2024-02-28']
    commentscore = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    text = ['very good', 'so nice', 'very bad', 'so interesting' , 'so dirty' , 'very clean' , 'very exiting'] 

    for _ in range(num_records):
        comment_id = generate_unique_id(cursor, 'hotel_comment', 'comment_id')
        commentid.append(comment_id)
        user_id = random.choice(userid)
        comment_registration_time = random.choice(registration_time)
        comment_registration_date = random.choice(registration_date)
        score = random.choice(commentscore)
        hotel_id = random.choice(hotelid)
        comment_text = random.choice(text)

        query = "INSERT INTO hotel_comment (comment_id, user_id, comment_registration_time, comment_registration_date, score, hotel_id, comment_text) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (comment_id, user_id, comment_registration_time, comment_registration_date, score, hotel_id, comment_text)
        cursor.execute(query, values)


    #bank_info
    for _ in range(num_records):
        
        bank_info_id = generate_unique_id(cursor, 'bank_info', 'bank_info_id')
        bankinfoid.append(bank_info_id)
        shaba_number = random.choice(shaba_numbers)
        account_number = random.choice(account_numbers)
        card_number = random.choice(card_numbers)
        user_id = random.choice(userid) 

        query = "INSERT INTO bank_info (bank_info_id, shaba_number, account_number, card_number, user_id) VALUES (%s, %s, %s, %s, %s)"
        values = (bank_info_id, shaba_number, account_number, card_number, user_id)
        cursor.execute(query, values)


    #transactions
    for _ in range(num_records):
        
        transaction_id = generate_unique_id(cursor, 'transactions', 'transaction_id')
        transactionid.append(transaction_id)
        transaction_date = random.choice(dates)
        amount = random.choice(transaction_amounts)
        transaction_type = random.choice(transaction_types)
        transaction_time = random.choice(times)
        user_id = random.choice(userid) 

        query = "INSERT INTO transactions (transaction_id, transaction_date, amount, transaction_type, transaction_time) VALUES (%s, %s, %s, %s, %s)"
        values = (transaction_id, transaction_date, amount, transaction_type, transaction_time)
        cursor.execute(query, values)

    
    #Hotel_room
    hotelprice = [1000000,2000000,4000000,2500000,5400000,2800000,1700000,3000000,3500000,1500000]
    beds = [1,2,4,2,4,2,1,2,3,4]
    type = ['single','double','twin']
 
    for _ in range(num_records):
        room_id = generate_unique_id(cursor, 'hotel_room', 'room_id')
        roomid.append(room_id)
        price = random.choice(hotelprice)
        beds_num = random.choice(beds)
        room_type = random.choice(type)
        hotel_id = random.choice(hotelid)
        
        query = "INSERT INTO hotel_room (room_id, price, beds_num, room_type, hotel_id) VALUES (%s, %s, %s, %s, %s)"
        values = (room_id, price, beds_num, room_type, hotel_id)
        cursor.execute(query, values)


    #hotel_reservation
    reservdate=['2024-02-13','2024-02-15','2024-02-18','2024-02-19','2024-02-21','2024-02-22','2024-02-24','2024-02-25','2024-02-27','2024-02-28']
    arriveltime=['2024-02-12 08:35:00','2024-02-12 12:15:00','2024-02-12 15:45:00','2024-02-12 10:20:00','2024-02-12 18:00:00','2024-02-12 14:10:00','2024-02-12 11:55:00','2024-02-12 16:30:00','2024-02-12 09:40:00','2024-02-12 13:25:00']
    departuretime=['2024-02-12 13:20:00','2024-02-12 16:55:00','2024-02-12 09:30:00','2024-02-12 12:10:00','2024-02-12 15:40:00','2024-02-12 11:15:00','2024-02-12 14:50:00','2024-02-12 17:25:00','2024-02-12 10:00:00','2024-02-12 13:35:00',]
    
    for _ in range(num_records):
        reserv_id = generate_unique_id(cursor, 'hotel_reservation', 'reserv_id')
        reservid.append(reserv_id)
        passenger_id = random.choice(passengerid)
        arrival_time = random.choice(arrivaltime)
        departure_time = random.choice(departuretime)
        room_id = random.choice(roomid)
        reserv_date = random.choice(reservdate)
        hotel_id = random.choice(hotelid)

        query = "INSERT INTO hotel_reservation (reserv_id, passenger_id, arrival_time, departure_time, room_id, reserv_date, hotel_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (reserv_id, passenger_id, arrival_time, departure_time, room_id, reserv_date, hotel_id)
        cursor.execute(query, values)


    #train_trip
    for _ in range(num_records):
        
        train_trip_number = generate_unique_id(cursor, 'train_trip', 'train_trip_number')
        traintripnumber.append(train_trip_number)
        stopping_stations = random.choice(stopping_stations_lst)
        image = random.choice(images)
        adult_price = random.choice(prices)
        child_price = random.choice(prices)
        trip_id = random.choice(tripid) 

        query = "INSERT INTO train_trip (train_trip_number, stopping_stations, image, adult_price, child_price, trip_id) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (train_trip_number, stopping_stations, image, adult_price, child_price, trip_id)
        cursor.execute(query, values)


    #flight_trip
    Airplane_terminals = [i for i in range(1,11)]
    Air_ports = ['Belgium Airport', 'Anguilla Airport', 'Eqypt Airport', 'Egypt Airport', 'England Airport', 'Australia Airport', 'Malaysia Airport', 'Aruba Airport', 'Benin Airport', 'Germany Airport']
    flightdurations = ['7:20', '4:12', '06:13', '06:02', '02:49', '12:14', '07:55', '02:03', '13:33', '21:12']

    for _ in range(num_records):
        flight_number = generate_unique_id(cursor, "flight_trip", 'flight_number')
        flightnumber.append(flight_number)
        trip_id = random.choice(tripid)
        terminal = random.choice(Airplane_terminals)
        airport = random.choice(Air_ports)
        flight_duration = random.choice(flightdurations)
        airplane_id = random.choice(airplaneid)

        query = "INSERT INTO flight_trip (flight_number, trip_id, terminal, airport, flight_duration, airplane_id) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (flight_number, trip_id, terminal, airport, flight_duration, airplane_id)
        cursor.execute(query, values)
    

    #bus_trip
    bus_price = [50, 100, 86, 32, 40, 69, 90, 45, 73, 120]

    for _ in range(num_records):
        bus_trip_number = generate_unique_id(cursor, 'bus_trip', 'bus_trip_number')
        bustripnumber.append(bus_trip_number)
        trip_id = random.choice(tripid)
        terminal = random.choice(stopping_stations_lst)
        price = random.choice(bus_price)
        bus_id = random.choice(busid)
        
        query = "INSERT INTO bus_trip (bus_trip_number, trip_id, terminal, price, bus_id) VALUES (%s, %s, %s, %s, %s)"
        values = (bus_trip_number, trip_id, terminal, price, bus_id)
        cursor.execute(query, values)


    #compartment_train_trip
    for _ in range(num_records):
        
        compartment_train_trip_id = generate_unique_id(cursor, 'compartment_train_trip', 'compartment_train_trip_id')
        compartmenttraintripid.append(compartment_train_trip_id)
        train_trip_number = random.choice(traintripnumber) 
        compartment_train_number = random.choice(compartmenttrainnumber)

        query = "INSERT INTO compartment_train_trip (compartment_train_trip_id, train_trip_number, compartment_train_number) VALUES (%s, %s, %s)"
        values = (compartment_train_trip_id, train_trip_number, compartment_train_number)
        cursor.execute(query, values)


    #coach_train_trip
    for _ in range(num_records):
        
        coach_train_trip_id = generate_unique_id(cursor, 'coach_train_trip', 'coach_train_trip_id')
        coachtraintripid.append(coach_train_trip_id)
        train_trip_number = random.choice(traintripnumber) 
        coach_train_number = random.choice(coachtrainnumber)

        query = "INSERT INTO coach_train_trip (coach_train_trip_id, train_trip_number, coach_train_number) VALUES (%s, %s, %s)"
        values = (coach_train_trip_id, train_trip_number, coach_train_number)
        cursor.execute(query, values)


    #cabin
    classtype = ['business', 'economy']
    baggageallowances = [20, 25, 30, 35, 40]
    adultprice = [50, 100, 86, 32, 40, 69, 90, 45, 73, 120]
    childprice = [25, 50 , 43, 16, 20, 30, 45, 23, 32, 60]

    for _ in range(num_records):
        class_id = generate_unique_id(cursor, 'cabin', 'class_id')
        classid.append(class_id)
        class_type = random.choice(classtype)
        flight_number = random.choice(flightnumber)
        baggage_allowance = random.choice(baggageallowances)
        adult_price = random.choice(adultprice)
        child_price = random.choice(childprice)

        query = "INSERT INTO cabin (class_id, class_type, flight_number, baggage_allowance, adult_price, child_price) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (class_id, class_type, flight_number, baggage_allowance, adult_price, child_price)
        cursor.execute(query, values)

    #bus_ticket
    bus_ticke_series=[3673688,9038388,9735377,9291745,3680561,1775499,2295836,4029337,3777354,9088864]
    seat_num=[42,97,93,65,64,91,110,16,87,34]

    for _ in range(num_records):
        bus_ticket_num = generate_unique_id(cursor, 'bus_ticket', 'bus_ticket_num')
        busticketnum.append(bus_ticket_num)
        passenger_id = random.choice(passengerid)
        ticket_series = random.choice(bus_ticke_series)
        seat = random.choice(seat_num)
        bus_trip_number = random.choice(bustripnumber)

        query = "INSERT INTO bus_ticket (bus_ticket_num, passenger_id, ticket_series, seat, bus_trip_number) VALUES (%s, %s, %s, %s, %s)"
        values = (bus_ticket_num, passenger_id, ticket_series, seat, bus_trip_number)
        cursor.execute(query, values)
    

    #compartment_train_ticket
    for _ in range(num_records):
        
        compartment_ticket_number = generate_unique_id(cursor, 'compartment_train_ticket', 'compartment_ticket_number')
        compartmentticketnumber.append(compartment_ticket_number)
        ticket_number = random.choice(ticket_numbers)
        wagon_number = random.choice(wagon_num)
        seat_number = random.choice(seat_num)
        compartment_number = random.choice(compartment_num)
        compartment_train_trip_id = random.choice(compartmenttraintripid) 
        passenger_id = random.choice(passengerid)

        query = "INSERT INTO compartment_train_ticket (compartment_ticket_number, ticket_number, wagon_number, seat_number, compartment_number, compartment_train_trip_id, passenger_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (compartment_ticket_number, ticket_number, wagon_number, seat_number, compartment_number, compartment_train_trip_id, passenger_id)
        cursor.execute(query, values)


    #coach_train_ticket
    for _ in range(num_records):
        
        coach_ticket_number = generate_unique_id(cursor, 'coach_train_ticket', 'coach_ticket_number')
        coachticketnumber.append(coach_ticket_number)
        ticket_number = random.choice(ticket_numbers)
        wagon_number = random.choice(wagon_num)
        seat = random.choice(seat_num)
        coach_train_trip_id = random.choice(coachtraintripid) 
        passenger_id = random.choice(passengerid)

        query = "INSERT INTO coach_train_ticket (coach_ticket_number, ticket_number, wagon_number, seat, coach_train_trip_id, passenger_id) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (coach_ticket_number, ticket_number, wagon_number, seat, coach_train_trip_id, passenger_id)
        cursor.execute(query, values)

   
    #international_flight_ticket
    international_flight_ticket_series =[5673433,8893646,9356967,29474284,3976424,3948920,3984993,2047204,93746236]
    passportnum  =[56734336,935696798,39764240,54436735,90534665,34226658,92343397,32367795,34244333,48940374]
    passportexpirationdate =['2023-12-15','2025-09-02','2024-10-14','2026-01-01','2023-11-08','2024-06-19','2025-09-05','2026-02-11','2025-12-04','2024-12-20']
    adbirthdate =['2000-11-25','1990-09-02','1995-03-14','1980-01-01','1970-11-08','1985-06-19','2003-09-05','2002-02-11','2010-12-04','1992-12-20']

    for _ in range(num_records):
        international_flight_ticket_id = generate_unique_id(cursor, 'international_flight_ticket', 'international_flight_ticket_id')
        internationalflightticketid.append(international_flight_ticket_id)
        passenger_id = random.choice(passengerid)
        ticket_series = random.choice(international_flight_ticket_series)
        passport_num = random.choice(passportnum)
        passport_expiration_date = random.choice(passportexpirationdate)
        ad_birthdate = random.choice(adbirthdate)
        class_id = random.choice(classid)

        query = "INSERT INTO international_flight_ticket (international_flight_ticket_id, passenger_id, ticket_series, passport_num, passport_expiration_date, ad_birthdate, class_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (international_flight_ticket_id, passenger_id, ticket_series, passport_num, passport_expiration_date, ad_birthdate, class_id)
        cursor.execute(query, values)


    #domestic_flight_ticket
    domestic_flight_ticket_series =[5675433,8293646,9056967,29422284,3929424,3918920,3981193,2047219,93742936]

    for _ in range(num_records):
        domestic_flight_ticket_id = generate_unique_id(cursor, 'domestic_flight_ticket', 'domestic_flight_ticket_id')
        domesticflightticketid.append(domestic_flight_ticket_id)
        passenger_id = random.choice(passengerid)
        ticket_series = random.choice(domestic_flight_ticket_series)
        class_id = random.choice(classid)

        query = "INSERT INTO domestic_flight_ticket (domestic_flight_ticket_id, passenger_id, ticket_series, class_id) VALUES (%s, %s, %s, %s)"
        values = (domestic_flight_ticket_id, passenger_id, ticket_series, class_id)
        cursor.execute(query, values)


    #protector
    protector_emails = ['heather13@example.org', 'tmartin@example.net', 'jwashington@example.com', 'chandlermark@example.net', 'lglenn@example.com', 'jennifercastillo@example.com', 'vanessadavila@example.org', 'schneiderjustin@example.org', 'bennettmathew@example.net', 'janet62@example.org']
    
    for _ in range(num_records):
        protector_id = generate_unique_id(cursor, 'protector', 'protector_id')
        protectorid.append(protector_id)
        person_id = random.choice(personid)
        email = random.choice(protector_emails)

        query = "INSERT INTO protector (protector_id, person_id, email) VALUES (%s, %s, %s)"
        values = (protector_id, person_id, email)
        cursor.execute(query, values)



    conn.commit()
    cursor.close()
    conn.close()


conn = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    user="root",
    password="bahar1381",
    database="AliBaba"
)
cursor = conn.cursor()

insert_random_data(10)