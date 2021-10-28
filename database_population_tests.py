import sqlite3 as sql

def add_test_restaurant_hairy():
    # Connecting to database
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor() 
    # Adding data
    # restaurant The Hairy Sack
    c.execute("INSERT INTO restaurants (name, street, suburb, max_reservations, caption, description, price, cuisine_type, num_courses, website, image) VALUES ('The Hairy Sack', '1 Hairy Street', 'Kenmore', '3000', 'A very hair meal vending machine', 'Imagine being unable to leave your house cause the hairy meatball you had last down comes out of the toilet to strangle you. Get this experience today at the hairy sack - the best place to be strangled by meatballs around the town.', '123', 'asian', '2', 'https://www.youtube.com/watch?v=TFtlK6fuVno&list=UUBfB4NCL1v1Wx_tMD6hpLkw&index=58', '/static/image/gerardsbistro.jpg')")
    # Applying changes
    con.commit()

# hungry jacks
def add_test_restaurant_hjs():
    # Connecting to database
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor() 
    # Adding data
    # restaurant hungry jacks
    c.execute("INSERT INTO restaurants (name, street, suburb, max_reservations, caption, description, price, cuisine_type, num_courses, website, image) VALUES ('Hungry Jacks', '127 Queen Street', 'Brisbane City', '30', 'those bin chicken fries hit different', 'there is nothing better than a late night out in the city and hitting up the queen st hungry jacks. its like brisbanes communal spawn point', '500', 'modern australian', '10', 'https://hungryjacks.com.au', '/static/image/2021-10-26_10-41.png')")
    # Applying changes
    con.commit()



def add_test_user_neo():
    # Connecting to database
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor()
    # Adding data
    # user neo
    c.execute("INSERT INTO users (name, password_hash, email, image) VALUES ('Neo', 'pbkdf2:sha256:260000$I7MOhQQ2dNIVkUjd$a250d000c849c5b4eafc6705afb4097864272de30515d98be616c3be6875edcf', 'Neo@gmail.com', '/static/image/user_neo.jpg')")
    # Applying changes
    con.commit()


def add_test_user_internette():
    # Connecting to database
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor()
    # Adding data
    # user internette
    c.execute("INSERT INTO users (name, password_hash, email, image) VALUES ('internette', 'pbkdf2:sha256:260000$bAxvfw89ii2grpIF$23359b9630ea16da8ded096b0ce283580dab5697fd3eafd6869676e1f9c8277e', 'internette@email.com', '/static/image/account.png')")
    # Applying changes
    con.commit()

def add_test_user_simon():
    # Connecting to database
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor()
    # Adding data
    # user simon
    c.execute("INSERT INTO users (name, password_hash, email, image) VALUES ('simon', 'pbkdf2:sha256:260000$fwDiHn04YRmg6BUu$b608404f64f2860aaa83a4306d0dac07f8f4a016c3442288edad42219901a914', 'simon@email.com', '/static/image/bonkproof.png')")
    # Applying changes
    con.commit()

def add_test_user_rock():
    # Connecting to database
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor()
    # Adding data
    # user rock
    c.execute("INSERT INTO users (name, password_hash, email, image) VALUES ('The Rock', 'pbkdf2:sha256:260000$TdryVoMuFR8gp9AV$f13a2891fc083b90d0d6f0a73543c7acfdd914d34a054d60706ca2e4d8877f85', 'rock@email.com', '/static/image/user_rock.jpg')")
    # Applying changes
    con.commit()


def add_test_user_matt():
    # Connecting to database
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor()
    # Adding data
    # user matt
    c.execute("INSERT INTO users (name, password_hash, email, image) VALUES ('Matt', 'pbkdf2:sha256:260000$DGwfD8M5W2PmU9bn$d522e4dfc5eb7c3f83c71f9baec9d947b1ffc4163713c1df15ee1fffb277610a', 'matt@email.com', '/static/image/user_matt.jpg')")
    # Applying changes
    con.commit()

def add_test_user_sweeney():
    # Connecting to database
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor()
    # Adding data
    # user sweeney
    c.execute("INSERT INTO users (name, password_hash, email, image) VALUES ('Sweeney', 'pbkdf2:sha256:260000$AmJGHN1t0Ilr2CbJ$0ea41ab5706a982858e5d864707be3f318c776989028309a8a9eb9536c7feeb4', 'sweeney@email.com', '/static/image/Sweeney.png')")
    # Applying changes
    con.commit()


def add_test_comment_hairy():
    # Connecting to database
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor() 
    # Adding data
    # neo comment on hairy sack
    c.execute("INSERT INTO comments (text, post_date, user_rating, user_id, restaurant_id) VALUES ('Best Hairy Sack in the Matrix ooooh god damn i love hair sacks meatballs', '2021-10-25 02:06:30.489405', '5', '1', '1')")
    # Applying changes
    con.commit()


def add_test_comment_hjs():
    # Connecting to database
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor() 
    # Adding data
    #internette comment on hjs
    c.execute("INSERT INTO comments (text, post_date, user_rating, user_id, restaurant_id) VALUES ('Love this place', '2021-10-26 10:47:35.705792', '5', '2', '2')")
    # Applying changes
    con.commit()


def add_test_restaurantstatus_hairy():
    # Connecting to database
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor() 
    # Adding data
    # restaurant status
    c.execute("INSERT INTO restaurantstatuses (status, at_time, restaurant_id) VALUES ('upcoming', '2021-10-25 02:06:30.493405', '1')")
    # Applying changes
    con.commit()

def add_test_restaurantstatus_hjs():
    # Connecting to database
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor() 
    # Adding data
    # restaurant status
    c.execute("INSERT INTO restaurantstatuses (status, at_time, restaurant_id) VALUES ('upcoming', '2021-10-26 10:38:15.996731', '2')")
    # Applying changes
    con.commit()


def add_test_reservation():
     # Connecting to database
    con = sql.connect('website\sitedata.sqlite')
    # Getting cursor
    c =  con.cursor() 
    # Adding data



# add_test_comments()
# add_test_restaurants()
# add_test_restaurantstatus()
# add_test_users()


