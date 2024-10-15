import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    user="root",
    password="bahar1381",
    database="AliBaba"
)
cursor = conn.cursor()

# cursor.execute("DROP DATABASE IF EXISTS AliBaba")

cursor.execute("""SELECT COUNT(DISTINCT p.passenger_id) AS total_passengers
FROM passenger p
LEFT JOIN hotel_comment hc ON p.passenger_id = hc.user_id
WHERE p.passenger_id IN (
    SELECT passenger_id FROM compartment_train_ticket
    UNION
    SELECT passenger_id FROM bus_ticket
    UNION
    SELECT passenger_id FROM international_flight_ticket
)
AND hc.comment_id IS NOT NULL;""")


# cursor.execute("""SELECT h.hotel_name, COUNT(hr.room_id) AS available_rooms
# FROM hotel AS h
# JOIN hotel_room AS hr ON h.hotel_id = hr.hotel_id
# LEFT JOIN hotel_reservation AS res ON hr.room_id = res.room_id
# WHERE res.room_id IS NULL OR (res.departure_time < CURRENT_TIME AND res.arrival_time > CURRENT_TIME)
# GROUP BY h.hotel_name;""")


# cursor.execute("""SELECT u.user_id, u.username, COUNT(t.transaction_id) AS total_transactions
# FROM users u
# JOIN transactions t ON u.user_id = t.user_id
# GROUP BY u.user_id, u.username
# HAVING total_transactions > (SELECT AVG(transaction_count) FROM (SELECT user_id, COUNT(transaction_id) AS transaction_count FROM transactions GROUP BY user_id) AS user_transactions);""")


# cursor.execute("""SELECT h.hotel_name, COUNT(p.passenger_id) AS total_passengers_with_discount
# FROM hotel h
# JOIN hotel_reservation hr ON h.hotel_id = hr.hotel_id
# JOIN passenger p ON hr.passenger_id = p.passenger_id
# JOIN discount d ON p.user_id = d.user_id
# GROUP BY h.hotel_name;""")


# cursor.execute("""SELECT u.user_id, COUNT(hr.reserv_id) AS total_hotel_reservations
# FROM users u
# JOIN transactions t ON u.user_id = t.user_id
# JOIN discount d ON u.user_id = d.user_id
# JOIN passenger pas ON u.user_id = pas.user_id
# JOIN hotel_reservation hr ON pas.passenger_id = hr.passenger_id
# GROUP BY u.user_id;""")


result = cursor.fetchall()
conn.commit()
print(result)
cursor.close()
conn.close()
