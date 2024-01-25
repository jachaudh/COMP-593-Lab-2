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

   
def add_pizza_toppings(about_me, toppings):

    about_me['pizza_toppings'].extend(toppings)
    about_me['pizza_toppings'] = sorted(set(about_me['pizza_toppings']))
    about_me['pizza_toppings'] = [topping.upper() for topping in about_me['pizza_toppings']]
    

def print_pizza_toppings(toppings):

    print("My favourite pizza toppings are:")
    print("\n".join(f"- {topping}" for topping in toppings[:3]).upper())  
    print("\nMy favourite pizza toppings are:")
    additional_toppings = ['chicken', 'tomatoes', 'peperoni', 'letus']
    print("\n".join(f"- {topping}" for topping in additional_toppings))
    print()





    return

if __name__ == '__main__':
    main()