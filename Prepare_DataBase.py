import sqlite3

conn = sqlite3.connect('sport_gym.db')
curr = conn.cursor()

curr.execute(f'''INSERT INTO gym_members(subscription_type, first_name, last_name, birthdate, phone, 
        register_date, section) 
        VALUES ('YEAR', 'Tornike', 'Chakvetadze', '1995-09-13', '551 23 89 75', '2019-12-25', 'Calisthenics'),
        ('YEAR', 'Zura', 'Maisuradze', '1996-02-12', '599 88 77 66', '2015-01-20', 'Boxing'),
        ('MONTH', 'Nikolas', 'Girgvliani', '1997-01-11', '571 22 40 36', '2016-02-21', 'Swimming'),
        ('WEEK', 'Xose', 'Xozrevanidze', '1994-02-12', '599 88 77 66', '2017-03-22', 'Boxing'),
        ('DAY', 'Levani', 'Urumashvili', '1997-03-13', '558 90 87 89', '2018-04-23', 'Calisthenics'),
        ('DAY', 'Nata', 'Komladze', '1995-04-14', '558 45 76 28', '2019-05-23', 'Swimming'),
        ('MONTH', 'Lana', 'Yipiani', '1996-05-15', '551 03 85 67', '2020-06-24', 'Boxing'),
        ('WEEK', 'Tamar', 'Qmosteli', '1997-06-16', '599 78 64 25', '2021-07-26', 'Wrestling'),
        ('WEEK', 'Avto', 'Sxiladze', '1998-07-17', '553 22 76 93', '2022-08-27', 'CrossFit'),
        ('MONTH', 'Giorgi', 'Gogoladze', '1999-08-18', '599 67 76 87', '2015-09-28', 'Boxing'),
        ('YEAR', 'Sandro', 'Wereteli', '1993-09-19', '599 98 78 90', '2016-10-29', 'Wrestling'),
        ('YEAR', 'Marita', 'Gigauri', '1990-01-11', '551 23 32 45', '2017-11-30', 'Boxing'),
        ('DAY', 'Alina', 'Chubinidze', '1999-02-13', '558 90 08 80', '2018-12-01', 'Swimming'),
        ('DAY', 'Vika', 'Ubilava', '1998-03-13', '551 56 67 78', '2019-01-03', 'CrossFit'),
        ('WEEK', 'Mehman', 'Siordia', '1990-04-13', '558 89 90 98', '2017-02-05', 'Calisthenics'),
        ('YEAR', 'Ali', 'Talibovi', '1992-05-15', '599 99 78 89', '2016-03-07', 'Rock Climbing'),
        ('YEAR', 'Akaki', 'Papashvili', '1998-06-17', '551 78 76 45', '2017-04-09', 'Swimming'),
        ('MONTH', 'Davit', 'Rogava', '1999-03-13', '599 78 09 83', '2018-05-10', 'Boxing'),
        ('DAY', 'Miranda', 'Lomidze', '1996-05-19', '551 34 00 88', '2019-06-12', 'Calisthenics'),
        ('MONTH', 'Salome', 'Xachidze', '1997-04-14', '558 77 09 87', '2021-07-14', 'Wrestling'),
        ('MONTH', 'Kate', 'Barbaqadze', '1997-05-15', '551 32 21 59', '2021-08-16', 'Boxing'),
        ('WEEK', 'Xatuna', 'Gelashvili', '1997-02-12', '599 56 78 52', '2020-09-18', 'Rock Climbing'),
        ('WEEK', 'Mixeil', 'Wurwumia', '1998-04-18', '571 22 89 75', '2020-10-20', 'Rock Climbing'),
        ('WEEK', 'John', 'Pxaladze', '1996-02-18', '571 77 67 65', '2019-12-22', 'Wrestling'),
        ('DAY', 'Bacho', 'Buxrikidze', '1997-04-13', '599 11 43 51', '2019-11-25', 'Boxing'),
        ('YEAR', 'Malxazi', 'Kenjoshvili', '1999-07-13', '571 99 87 80', '2015-12-28', 'CrossFit');
''')

conn.commit()
conn.close()

# curr.execute('''CREATE TABLE IF NOT EXISTS gym_members(
#     subscription_type text,
#     first_name text,
#     last_name text,
#     birthdate text,
#     phone text,
#     register_date text,
#     section text
# )''')
