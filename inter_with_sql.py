# THIS WILL ONLY WORK IN DJANGO CIVIL SPECIFIC BRANCH!!

#https://www.youtube.com/watch?v=M2NzvnfS-hI&ab_channel=techTFQ

#https://www.youtube.com/watch?v=miEFm1CyjfM&ab_channel=NeuralNine

import psycopg

from .deep_backend.rect_single_reinf import RectCrSectSingle


def some_rc_res():
    pass

class InputData():
    POSTGRESDATA = {
        'host': 'localhost',
        'dbname': 'analysis',
        'user': 'postgres',
        'password': 'wiKOlan#o0_sql',
        'port': 5432,
        }
    RCDATA = {'name':'moj_przekr_prost',
              'b':0.4,
              'h':1.7,
              'cl_conc':'C20_25',
              'cl_steel':'BSt500S',
              'c':30,
              'fi':12,
              'no_of_bars':14,'fi_s':8}

def sql_interactions():
    postgres_data = {
        'host': 'localhost',
        'dbname': 'analysis',
        'user': 'postgres',
        'password': 'wiKOlan#o0_sql',
        'port': 5432,
        }

    conn = None
    cur = None

    try:
        conn= psycopg.connect(**postgres_data)
        cur = conn.cursor()
        # cur.execute('DROP TABLE IF EXISTS teachers_py')
        # create_script = '''CREATE TABLE IF NOT EXISTS teachers_py (
        #     id bigserial,
        #     first_name varchar(25),
        #     last_name varchar(50),
        #     school varchar(50),
        #     hire_date date,
        #     salary numeric
        #     );'''
        cur.execute('DROP TABLE IF EXISTS bending_res')
        create_script2 = '''CREATE TABLE IF NOT EXISTS bending_res (
            id bigserial NOT NULL PRIMARY KEY,
            m_rd NUMERIC(7,3),
            ksi_eff NUMERIC(7,3),
            x_eff NUMERIC(7,3)
            );'''
        cur.execute(create_script2)
        res_tuple = RectCrSectSingle(**rcdata).compute_m_rd_single_r() 
        cur.execute("INSERT INTO bending_res (m_rd, ksi_eff, x_eff) VALUES (%s, %s, %s)",
                    (res_tuple))
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

def sql_interactions2(postgres_data, rc_data):
    with psycopg.connect(**postgres_data) as conn:
        with conn.cursor() as cur:
            cur.execute('DROP TABLE IF EXISTS bending_res')
            create_script2 = '''CREATE TABLE IF NOT EXISTS bending_res (
                id bigserial NOT NULL PRIMARY KEY,
                m_rd NUMERIC(7,3),
                ksi_eff NUMERIC(7,3),
                x_eff NUMERIC(7,3)
                );'''
            cur.execute(create_script2)
            res_tuple = RectCrSectSingle(**rc_data).compute_m_rd_single_r() 
            cur.execute("INSERT INTO bending_res (m_rd, ksi_eff, x_eff) VALUES (%s, %s, %s)",
                        (res_tuple))
            conn.commit()

def main():
    postgres_data = InputData.POSTGRESDATA
    rc_data = InputData.RCDATA
    sql_interactions2(postgres_data, rc_data)

if __name__ == '__main__':
    main()