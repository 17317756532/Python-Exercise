import sqlite3

# Read content from the file and store it in a list
file_path = "stephen_king_adaptations.txt"
with open(file_path, "r") as file:
    stephen_king_adaptations_list = file.readlines()

# Establish connection with the database
conn = sqlite3.connect("stephen_king_adaptations.db")
cursor = conn.cursor()

# Create a table
create_table_query = """CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (
                            movieID INTEGER PRIMARY KEY AUTOINCREMENT,
                            movieName TEXT,
                            movieYear INTEGER,
                            imdbRating REAL
                        );"""
cursor.execute(create_table_query)

# Insert content into the database table
for line in stephen_king_adaptations_list:
    movie_data = line.strip().split(",")
    
    if len(movie_data) != 3:
        continue

    movie_name = movie_data[0]
    
    try:
        movie_year = int(movie_data[1])
        imdb_rating = float(movie_data[2])
    except ValueError:
        continue

    cursor.execute("INSERT INTO stephen_king_adaptations_table (movieName, movieYear, imdbRating) VALUES (?, ?, ?)",
                   (movie_name, movie_year, imdb_rating))

conn.commit()

# User interaction loop
while True:
    print("Please select an operation:")
    print("1. Search by movie name")
    print("2. Search by movie year")
    print("3. Search by movie rating")
    print("4. Quit the program")

    option = input("Enter the option number: ")

    if option == "1":
        movie_name = input("Enter the movie name to be searched: ")
        search_query = "SELECT * FROM stephen_king_adaptations_table WHERE movieName = ?"
        cursor.execute(search_query, (movie_name,))
        result = cursor.fetchall()

        if len(result) > 0:
            print("Search result:")
            for row in result:
                print("Movie Name:", row[1])
                print("Movie Year:", r)

