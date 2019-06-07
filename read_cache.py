import mysql.connector
import os


def main():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="159753")
    mycursor = mydb.cursor()
    mycursor.execute('select id from fma.track')
    a = 0
    #sql_update = 'update fma.track set is_cached=1 where id ='
    root = 'D:/share/fma/music/'
    cursf = mycursor.fetchall()
    for x in cursf:
        mid = x[0]
        tmp = mid // 1000
        path = '{}{:0>3}/{:0>6}.mp3'.format(root, tmp, mid)
        if os.path.exists(path):
            #    mycursor.execute(sql_update + str(id))
            #    a += 1
            newpath = '{}{:0>3}/{:0>6}_s.mp3'.format(root, tmp, mid)
            os.rename(path, newpath)
    print(a)
    mydb.commit()


if __name__ == '__main__':
    main()
