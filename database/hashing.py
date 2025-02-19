from passlib.context import CryptContext

pwd_cxt=CryptContext(schemes = ['bcrypt'], deprecated='auto' )

class Hash():
    def bcrypt(password):
        return pwd_cxt.hash(password)
    
    def verify(hashed_password,plain_password):
        # print(hashed_password+"dsdsd")
        return pwd_cxt.verify(plain_password,hashed_password)
        # print(a)