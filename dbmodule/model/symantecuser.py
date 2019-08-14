from enterpriseuser import EnterpriseUser

class SymantecUser(EnterpriseUser):
    def __init__(self, id,  name, managername, managerref, idpId, idpAccountId, idbId, idbAccountId):
        EnterpriseUser.__init__(id,  name, managername, managerref)
        self.idpId = idpId
        self.idpAccountId = idpAccountId
        self.idbId = idbId
        self.idbAccountId = idbAccountId
