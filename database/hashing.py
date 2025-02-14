from passlib.context import CryptContext

pwd_cxt=CryptContext(schemes = ['bcrypt'], deprecated='auto' )

class Hash():
    def bcrypt(password):
        return pwd_cxt.hash(password)
    
    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(hashed_password,plain_password)