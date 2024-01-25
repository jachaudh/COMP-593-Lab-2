def main():
    
    about_me = {

        'full_name': 'Jay Chaudhari',
        'student_id': 10291240  ,
        'pizza_toppings': ['MUSHROOMS', 'ONION', 'BLACKPEPPER'],
        'movies': [

            {
                'title': 'Intersteller',
             'genre': 'Sci-Fi',
            }
            {
            'title': 'FordvsFerrari', 
             'genre': 'Drama',
            }
        ]
    }

    
    add_movie = {'title': 'The Godfather', 'genre': 'crime'}
    about_me['movies'].append(add_movie)


    return

if __name__ == '__main__':
    main()