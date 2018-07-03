from builtins import ValueError

import numpy as np
import logging
import site


logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG, filename=u'logi.log')


def Error(num):
    if num==1:
        print("File content error,too many spaces")
        logging.critical(u'File content error,too many spaces\n')
    elif num==2:
        print("File content error,too many transfers")
        logging.critical(u'File content error,too many transfers\n')
    elif num==3:
        print("Error reading number")
        logging.critical(u'Error reading number\n')
    elif num==4:
        print("Error when working with file")
        logging.critical(u'Error when working with file\n')
    elif num==5:
        print("Error the size of the matrix")
        logging.critical(u'Error the size of the matrix\n')
    elif num==6:
        print("Error calculating roots")
        logging.critical(u'Error calculating roots\n')
    quit()


FileName=input('Enter name of file ')

try:
    file=open(FileName)
except IOError as error:
    print(str(error))
else:
    with file:  #автоматом закроет файл после того как выйдет из тела
        line=file.readline()
        try:
            razmer=int(line)
        except ValueError:
            Error(3)
        if razmer < 1:
            Error(5)
        M1: object=np.zeros((razmer, razmer))
        V2=np.zeros((razmer))
        buf=""
        i=0
        j=0
        while True:
            c=file.read(1)
            if not c:
                if i==razmer:
                    Error(2)
                try:
                    V2[i]=float(buf)
                except ValueError:
                    Error(3)
                print("End of file")
                break
            elif (c==' ') or (c=='\n'):
                if (buf!=""):
                    if c==' ':
                        if j==razmer:
                            Error(1)
                        try:
                            M1[i, j]=float(buf)
                        except ValueError:
                            Error(3)
                    else:
                        if i==razmer:
                            Error(2)
                        try:
                            V2[i]=float(buf)
                        except ValueError:
                            Error(3)
                    if c==' ':
                        j=j+1
                        buf=""
                    if c=='\n':
                        i=i+1
                        j=0
                        buf=""
            elif (c.isdigit()) or (c=='-') or (c=='.'):
                buf=buf+c
            else:
                Error(4)
    print(M1,'Койфициенты при переменных')
    print(V2,'Свободные члены')

    try:
        print(np.linalg.solve(M1, V2),'Корни уравнений')
    except ValueError:
        Error(6)
    a=""
    b=""
    c=""
    a=str(np.linalg.solve(M1, V2))
    b=str(M1)
    c=str(V2)
    logging.info("Answer: " + a + "\n")
    logging.info("The coefficients in front of the unknown: " + b + "\n")
    logging.info("Free term: " + c + "\n")
    logging.info("- date, program running\n")



#def Errors(num):
  #  if num==1:
 #       print("File content error,too many spaces")
 #       logging.critical(u'File content error,too many spaces\n')
 #   elif num==2:
  #      print("File content error,too many transfers")
  #      logging.critical(u'File content error,too many transfers\n')
  #  elif num==3:
  #      print("Error reading number")
  #      logging.critical(u'Error reading number\n')
  #  elif num==4:
   #     print("Error when working with file")
  #      logging.critical(u'Error when working with file\n')
  #  elif num==5:
  #      print("Error the size of the matrix")
  #      logging.critical(u'Error the size of the matrix\n')
  #  elif num==6:
  #      print("Error calculating roots")
  #      logging.critical(u'Error calculating roots\n')
 #   