from AppConfig.DBConnector import *
from werkzeug import security

def save_wav(id, wav):
    try:
        cur, conn = get_connection()
        print('connected to database --- ECK ')
        print(type(wav))

        with open('www.wav', 'wb') as w:
            w.write()
        command = f" INSERT INTO ECG (id , wav ) VALUES ({id}, {wav} ) ;"
        cur.execute(command)
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False
