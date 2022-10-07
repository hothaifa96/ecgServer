from AppConfig.DBConnector import *


def save_wav(id, wav):
    try:
        cur, conn = get_connection()
        print('connected to database ECK ')
        command = f"INSERT INTO ECG (patient_id , wav ) VALUES ( '{id}',{wav}) ;"
        cur.execute(command)
        conn.commit()
        return True
    except Exception as e:
        print(e)
