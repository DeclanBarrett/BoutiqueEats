import sqlite3 as sql

#comments
def add_comment_deer():
    # Connecting to database
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor() 
    # Adding data
    c.execute("INSERT INTO comments (text, post_date, user_rating, user_id, restaurant_id) VALUES ('Went here on Saturday and it was amazing. Will definitely be ingesting both pills again', '2021-11-02 04:15:33.814300', '5', '1', '3')")
    # Applying changes
    con.commit()

def add_comment_dan():
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor() 
    # Adding data
    c.execute("INSERT INTO comments (text, post_date, user_rating, user_id, restaurant_id) VALUES ('Had the beef', '2021-11-02 04:15:33.814300', '5', '1', '4')")
    # Applying changes
    con.commit()

#add all comments in one function
def fill_comments():
    add_comment_deer()
    add_comment_dan()

#reservations
def reservation_elksa():
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor() 
    # Adding data
    c.execute("INSERT INTO reservations (quantity, reservation_time, reservation_created, user_order, restaurant_id, id) VALUES ('5', '2021-11-06 18:35:00.000000', '2021-11-02 03:34:43.705734', 'balls', '1', '1')")
    # Applying changes
    con.commit()

def reservation_rda():
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor() 
    # Adding data
    c.execute("INSERT INTO reservations (quantity, reservation_time, reservation_created, user_order, restaurant_id, id) VALUES ('2', '2021-11-05 17:16:00.000000', '2021-11-02 04:15:33.824300', '', '4', '1')")
    # Applying changes
    con.commit()

#add all reservations in one function
def fill_reservations():
    reservation_elksa()
    reservation_rda()


def elksa_hours_1():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Thursday', '18:00:00.000000', '23:59:00.000000', '1')")
    con.commit()

def elksa_hours_2():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Friday', '18:00:00.000000', '23:59:00.000000', '1')")
    con.commit()

def elksa_hours_3():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Saturday', '18:00:00.000000', '23:59:00.000000', '1')")
    con.commit()

def elksa_hours_4():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Sunday', '15:00:00.000000', '23:59:00.000000', '1')")
    con.commit()

def elksa_opening_hours():
    elksa_hours_1()
    elksa_hours_2()
    elksa_hours_3()
    elksa_hours_4()

def joy_hours_1():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Friday', '17:30:00.000000', '22:00:00.000000', '2')")
    con.commit()

def joy_hours_2():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Saturday', '17:30:00.000000', '22:00:00.000000', '2')")
    con.commit()

def joy_hours_3():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Sunday', '17:30:00.000000', '22:00:00.000000', '2')")
    con.commit()

def joy_opening_hours():
    joy_hours_1()
    joy_hours_2()
    joy_hours_3()

def ddb_hours_1():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Tuesday', '17:30:00.000000', '22:00:00.000000', '3')")
    con.commit()

def ddb_hours_2():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Wednesday', '17:30:00.000000', '22:00:00.000000', '3')")
    con.commit()

def ddb_hours_3():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Thursday', '17:30:00.000000', '22:00:00.000000', '3')")
    con.commit()

def ddb_hours_4():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Friday', '17:30:00.000000', '22:00:00.000000', '3')")
    con.commit()

def ddb_hours_5():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Saturday', '17:30:00.000000', '22:00:00.000000', '3')")
    con.commit()

def ddb_opening_hours():
    ddb_hours_1()
    ddb_hours_2()
    ddb_hours_3()
    ddb_hours_4()
    ddb_hours_5()

def rda_hours_1():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Wednesday', '18:00:00.000000', '23:59:00.000000', '4')")
    con.commit()

def rda_hours_2():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Thursday', '18:00:00.000000', '23:59:00.000000', '4')")
    con.commit()

def rda_hours_3():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Friday', '12:00:00.000000', '23:59:00.000000', '4')")
    con.commit()

def rda_hours_4():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Saturday', '06:00:00.000000', '23:59:00.000000', '4')")
    con.commit()

def rda_opening_hours():
    rda_hours_1()
    rda_hours_2()
    rda_hours_3()
    rda_hours_4()

def rogue_hours_1():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Wednesday', '17:30:00.000000', '22:30:00.000000', '5')")
    con.commit()

def rogue_hours_2():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Thursday', '17:30:00.000000', '22:30:00.000000', '5')")
    con.commit()

def rogue_hours_3():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Friday', '17:30:00.000000', '22:30:00.000000', '5')")
    con.commit()

def rogue_hours_4():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Saturday', '17:30:00.000000', '22:30:00.000000', '5')")
    con.commit()

def rogue_hours_5():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantopeninghours (day_of_the_week, start_time, end_time, restaurant_id) VALUES ('Sunday', '17:00:00.000000', '21:00:00.000000', '5')")
    con.commit()

def rogue_opening_hours():
    rogue_hours_1()
    rogue_hours_2()
    rogue_hours_3()
    rogue_hours_4()
    rogue_hours_5()

##add all restaurantopeninghours in one function
def fill_restaurantopeninghours():
    elksa_opening_hours()
    joy_opening_hours()
    ddb_opening_hours()
    rda_opening_hours()
    rogue_opening_hours()

def restaurant_1():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurants (name, street, suburb, max_reservations, caption, description, price, cuisine_type, num_courses, website, image) VALUES ('ELSKA', '2/148 Merthyr Rd', 'new farm', '120', 'Elska is an old Nordic translation for love. the love that we hold for food, connection and family.', 'ELSKA is an intimate twelve seated degustation restaurant focusing on the beautiful produce Australia has to offer, highlighted with Nordic culinary techniques. The restaurant is a collaboration of Nathans love for food and Frejas passion for connection.', '135', 'contemporary', '15',  'https://www.elska.com.au/about', '/static/image/elska_vertical.jpg')")
    con.commit()

def restaurant_2():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurants (name, street, suburb, max_reservations, caption, description, price, cuisine_type, num_courses, website, image) VALUES ('joy.', 'Shop 7/690 Ann St', 'fortitude valley', '12', 'Compact, artful venture with a seasonal fixed-price menu of modern, Japanese-inspired small plates.', 'Joy Restaurant was founded by chefs Tim and Sarah Scott in 2019. Joy is all about creativity, passion & fun. With Tim stepping away in 2020, Sarah has taken over and spends all her time ensuring you are all getting an experience driven by passion, deliciousness and story telling.', '150', 'japanese', '1', 'https://www.joyrestaurant.com.au/', '/static/image/joy.jpg')")
    con.commit()

def restaurant_3():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurants (name, street, suburb, max_reservations, caption, description, price, cuisine_type, num_courses, website, image) VALUES ('Deer Duck Bistro', '396 Milton Rd', 'auchenflower', '100', 'Modern European dishes and tasting menus in a moodily lit, playful space with antique furnishings.', 'Combining various textures and flavours in pure, refined, exhilarating culinary delights, Deer Duck Bistro invites you to a journey of innovative and deeply satisfying culinary adventure. Hidden away in a little suburb known as Auchenflower, Deer Duck Bistro brings a unique fine dining and degustation experience.', '139', 'european', '9', 'https://deerduckbistro.com.au/', '/static/image/deerduck.jpg')")
    con.commit()

def restaurant_4():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurants (name, street, suburb, max_reservations, caption, description, price, cuisine_type, num_courses, website, image) VALUES ('Restaurant Dan Arnold', '10/959 Ann St', 'fortitude valley', '100', 'Here at RDA, we serve modern Australian cooking, thoughtful, and elegant food in a relaxed and informal setting.', 'Dan and his wife Amelie opened their restaurant in July 2018 in Fortitude Valley, Brisbane. Since then, Dan and his team are creating tasting menus using ingredients sourced from small producers and local farms.', '190', 'modern australian', '9', 'https://www.restaurantdanarnold.com/', '/static/image/danarnold.jpg')")
    con.commit()

def restaurant_5():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurants (name, street, suburb, max_reservations, caption, description, price, cuisine_type, num_courses, website, image) VALUES ('Rogue Bistro', '14 Austin St', 'newstead', '100', 'Spacious venue with contemporary, minimalist decor, and a small, refined Modern European menu.', 'We offer a set 6 course Dego Menu for all guests dining in (dont worry, we can accommodate for dietary requirements too!). Our chefs refresh this menu with a few new courses every month so you will always have your faves to come back to and something new to try!', '85', 'modern european', '6', 'https://www.roguebistro.com/menu', '/static/image/roguebistro.jpg')")
    con.commit()

##add all restaurants in one function
def fill_restaurants():
    restaurant_1()
    restaurant_2()
    restaurant_3()
    restaurant_4()
    restaurant_5()

## restaurantstatuses
def rest_status_1():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantstatuses (status, at_time, restaurant_id) VALUES ('upcoming', '2021-11-01 18:44:43.278239', '1')")
    con.commit()

def rest_status_2():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantstatuses (status, at_time, restaurant_id) VALUES ('upcoming', '2021-11-01 18:44:43.278239', '2')")
    con.commit()

def rest_status_3():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantstatuses (status, at_time, restaurant_id) VALUES ('inactive', '2021-11-01 18:44:43.278239', '3')")
    con.commit()

def rest_status_4():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantstatuses (status, at_time, restaurant_id) VALUES ('upcoming', '2021-11-01 18:44:43.278239', '4')")
    con.commit()

def rest_status_5():
    con = sql.connect('website\sitedata.sqlite')
    c =  con.cursor() 
    c.execute("INSERT INTO restaurantstatuses (status, at_time, restaurant_id) VALUES ('booked', '2021-11-01 18:44:43.278239', '5')")
    con.commit()

##add all restaurantstatuses in one function
def fill_status():
    rest_status_1()
    rest_status_2()
    rest_status_3()
    rest_status_4()
    rest_status_5()

## users
def add_neo():
    con = sql.connect('website\sitedata.sqlite')
    c = con.cursor() 
    c.execute("INSERT INTO users (name, password_hash, email, image) VALUES ('Neo', 'pbkdf2:sha256:260000$CApL0lFzS4WKg331$a1767a51cd8542d5a022f6615a6419c03a1369a76deeec2379caf282af3d1071', 'neo@gmail.com', '/static/image/user_neo.jpg')")
    con.commit()


# add all users in one function
def fill_users():
    add_neo()


