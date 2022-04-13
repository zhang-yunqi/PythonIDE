import ftplib
from contextlib import closing


def send() -> None:
    with ftplib.FTP('127.0.0.2') as ftp:

        filename = 'main.o'

        try:
            ftp.login('python', '123456')

            with open(filename, 'rb') as fp:

                res = ftp.storlines("STOR " + filename, fp)

                if not res.startswith('226 Transfer complete'):
                    print('Upload failed')

        except ftplib.all_errors as e:
            print('FTP error:', e)


great_func()
