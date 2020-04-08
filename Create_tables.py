import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to PostgreSQL DBMS
con = psycopg2.connect("dbname = OpisOp user=postgres password='38gAc57ip!'")
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Obtain a DB Cursor
cursor = con.cursor()


def create_tables():
    commands = (
        '''
        DROP TABLE IF EXISTS most_bought_day CASCADE;
        CREATE TABLE most_bought_day
        (
        product_id varchar,
        day timestamp,
        FOREIGN KEY (product_id) references products(id)
        )
        ''',
        '''
        DROP TABLE IF EXISTS cart_recommendations CASCADE;
        CREATE TABLE cart_recommendations
        (
        product_cart_id varchar,
        product_recommendation_id varchar,
        FOREIGN KEY (product_cart_id) references products(id),
        FOREIGN KEY (product_recommendation_id) references products(id)
        )
        ''',
        '''
        DROP TABLE IF EXISTS most_bought_period CASCADE;
        CREATE TABLE most_bought_period
        (
        product_id varchar,
        timeperiod varchar,
        FOREIGN KEY (product_id) references products(id)
        )
        ''',
        '''
        DROP TABLE IF EXISTS weers_omstandigheden CASCADE;
        CREATE TABLE weers_omstandigheden
        (
        date varchar,
        location varchar,
        temperature varchar,
        humidity varchar,
        product_id varchar
        )
    '''
    )


    try:
        for command in commands:
            cursor.execute(command)

        cursor.close()
        con.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


create_tables()