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

   
def print_student_name_and_id(about_me):

    full_name = about_me['full_name']
    student_id = about_me['student_id']
    first_name = full_name.split()[0]

    print(f"My name is {full_name}, but you can call me Sir {first_name}.")
    print(f"My student ID is {student_id}.")


    return

if __name__ == '__main__':
    main()