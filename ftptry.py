import ftplib
FTP_HOST="ftp.dlptest.com"
FTP_USERNAME="dlpuser"
FTP_PASS="rNrKYTX9g7z3RgJRmxWuGHbeu"

ftp=ftplib.FTP(FTP_HOST,FTP_USERNAME,FTP_PASS)
ftp.encoding="utf-8"

#
# filename="pokemon_data_tab.txt"
# with open(filename,"rb") as file:
#     ftp.storbinary("STOR pokemon_data_tab.txt",file)
#
# print("success")
# print(ftp.dir())
filename="pokemon_data_tab.txt"
with open(filename,"wb") as file:
    ftp.retrbinary("RETR pokemon_data_tab.txt",file.write)

ftp.quit()
print("SUCCESS")



