import mysql.connector
import librosa
import os


def main():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="159753")
    mycursor = mydb.cursor()
    mycursor.execute('select id from musync.track where is_short_cached=1 and short_duration is null and id > 133297')
    a = 0
    sql_update = 'update musync.track set short_duration={} where id={}'
    root = 'D:/share/fma/music/'
    cursf = mycursor.fetchall()
    for x in cursf:
        mid = x[0]
        tmp = mid // 1000
        path = '{}{:0>3}/{:0>6}_s.mp3'.format(root, tmp, mid)
        if os.path.exists(path):
            print(str(a) + ' ' + str(mid))
            a += 1
            duration = librosa.get_duration(filename=path)
            mycursor.execute(sql_update.format(duration, mid))
            mydb.commit()


if __name__ == '__main__':
    main()
