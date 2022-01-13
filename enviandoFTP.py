from ftplib import *

ftp = FTP('ftp.ibiblio.org')

print(ftp.getwelcome())#recebe a mensagem de boas vindas do servidor

usuario = input("Digite nome de usuário: ")
senha = input("Digite a senha: ")
ftp.login(usuario, senha)

print("Diretório atual de trabalho: ",ftp.pwd())#pwdmostra o caminho
ftp.cwd('pub')#cwd recebe novo caminho

print("Diretório corrente: ", ftp.pwd())
print(ftp.retrlines('LIST'))#lista os arquivos dentro do diretório

ftp.quit()

#https://docs.python.org/3/library/ftplib.html