import gateway.dependencies.dependencies as dependencies

from nameko.rpc import rpc

class UserAccessService:

    name = 'userServices'

    database = dependencies.Database()

    @rpc
    def add_user(self, nrp, userAccount, email, userPassword):
        user = self.database.add_user(nrp,userAccount, email,userPassword)
        return user

    @rpc
    def get_user(self, email, userPassword):
        user = self.database.get_user(email, userPassword)
        return user
    
    @rpc
    def add_file(self, userAccount, file):
        self.database.add_file(userAccount, file)