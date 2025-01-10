
class Company:
    def __init__(self, invoice):
        self.invoice = invoice
        self.names = invoice.names
        self.set_value = invoice.set_value
        self.set_scheme = invoice.set_scheme
        self._AddressLocation = '//cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address'
        self._TaxScheme = '//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme'
        self._RegistrationAddress = '//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:RegistrationAddress'
        self._PartyLegalEntity = '//cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity'
        self._Party = '//cac:AccountingSupplierParty/cac:Party'

    # Tipo de persona 1 - Juridica, 2 - Natural
    @property
    def AdditionalAccountID(self):
        return self._AdditionalAccountID

    @AdditionalAccountID.setter
    def AdditionalAccountID(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:AccountingSupplierParty/cbc:AdditionalAccountID', 
            value
        )
        self._AdditionalAccountID = value

    @property
    def PartyName(self):
        return self._PartyName

    @PartyName.setter
    def PartyName(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name', 
            value
        )
        self._PartyName = value

    # tabla 13.4.3 Municipios-CityName
    @property
    def AddressID(self):
        return self._AddressID

    @AddressID.setter
    def AddressID(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._AddressLocation}/cbc:ID', 
            value
        )
        self._AddressID = value

    # tabla 13.4.3 Municipios-CityName
    @property
    def AddressCityName(self):
        return self._AddressCityName

    @AddressCityName.setter
    def AddressCityName(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._AddressLocation}/cbc:CityName', 
            value
        )
        self._AddressCityName = value

    # 13.4.2 Departamentos ISO 3166-2CO CountrySubentity, CountrySubentityCode
    @property
    def AddressCountrySubentity(self):
        return self._AddressCountrySubentity

    @AddressCountrySubentity.setter
    def AddressCountrySubentity(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._AddressLocation}/cbc:CountrySubentity', 
            value
        )
        self._AddressCountrySubentity = value

    # 13.4.2 Departamentos ISO 3166-2CO CountrySubentity, CountrySubentityCode
    @property
    def AddressCountrySubentityCode(self):
        return self._AddressCountrySubentityCode

    @AddressCountrySubentityCode.setter
    def AddressCountrySubentityCode(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._AddressLocation}/cbc:CountrySubentityCode', 
            value
        )
        self._AddressCountrySubentityCode = value

    @property
    def AddressLine(self):
        return self._AddressLine

    @AddressLine.setter
    def AddressLine(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._AddressLocation}/cac:AddressLine/cbc:Line', 
            value
        )
        self._AddressLine = value

    @property
    def RegistrationName(self):
        return self._RegistrationName

    @RegistrationName.setter
    def RegistrationName(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._TaxScheme}/cbc:RegistrationName', 
            value
        )
        self._RegistrationName = value

    @property
    def CompanyID(self):
        return self._CompanyID

    @CompanyID.setter
    def CompanyID(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._TaxScheme}/cbc:CompanyID', 
            value
        )
        self._CompanyID = value

    # tabla 13.2.1 Documento de identificación (Tipo de Identificador Fiscal)
    @property
    def DocumentType(self):
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, value):
        self.set_scheme(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._TaxScheme}/cbc:CompanyID', 
            'schemeName',
            value
        )
        self._DocumentType = value

    @property
    def VerificationDigit(self):
        return self._VerificationDigit

    @VerificationDigit.setter
    def VerificationDigit(self, value):
        self.set_scheme(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._TaxScheme}/cbc:CompanyID', 
            'schemeID',
            value
        )
        self._VerificationDigit = value

    # Responsabilidades fiscales, tabla 13.2.6.1
    @property
    def TaxLevelCode(self):
        return self._TaxLevelCode

    @TaxLevelCode.setter
    def TaxLevelCode(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._TaxScheme}/cbc:TaxLevelCode', 
            value
        )
        self._TaxLevelCode = value

    # tabla 13.4.3 Municipios-CityName
    @property
    def RegistrationID(self):
        return self._RegistrationID

    @RegistrationID.setter
    def RegistrationID(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._RegistrationAddress}/cbc:ID', 
            value
        )
        self._RegistrationID = value

    @property
    def RegistrationCityName(self):
        return self._RegistrationCityName

    @RegistrationCityName.setter
    def RegistrationCityName(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._RegistrationAddress}/cbc:CityName', 
            value
        )
        self._RegistrationCityName = value

    @property
    def RegistrationCountrySubentity(self):
        return self._RegistrationCountrySubentity

    @RegistrationCountrySubentity.setter
    def RegistrationCountrySubentity(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._RegistrationAddress}/cbc:CountrySubentity', 
            value
        )
        self._RegistrationCountrySubentity = value

    @property
    def RegistrationCountrySubentityCode(self):
        return self._RegistrationCountrySubentityCode

    @RegistrationCountrySubentityCode.setter
    def RegistrationCountrySubentityCode(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._RegistrationAddress}/cbc:CountrySubentityCode', 
            value
        )
        self._RegistrationCountrySubentityCode = value

    @property
    def RegistrationAddressLine(self):
        return self._RegistrationAddressLine

    @RegistrationAddressLine.setter
    def RegistrationAddressLine(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._RegistrationAddress}/cac:AddressLine/cbc:Line', 
            value
        )
        self._RegistrationAddressLine = value

    @property
    def LegalRegistrationName(self):
        return self._LegalRegistrationName

    @LegalRegistrationName.setter
    def LegalRegistrationName(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._PartyLegalEntity}/cbc:RegistrationName', 
            value
        )
        self._LegalRegistrationName = value

    @property
    def LegalCompanyID(self):
        return self._LegalCompanyID

    @LegalCompanyID.setter
    def LegalCompanyID(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._PartyLegalEntity}/cbc:CompanyID', 
            value
        )
        self._LegalCompanyID = value

    @property
    def LegalCorporateID(self):
        return self._LegalCorporateID

    @LegalCorporateID.setter
    def LegalCorporateID(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._PartyLegalEntity}/cac:CorporateRegistrationScheme/cbc:ID', 
            value
        )
        self._LegalCorporateID = value

    # Número de matrícula mercantil  
    @property
    def LegalCorporateName(self):
        return self._LegalCorporateName

    @LegalCorporateName.setter
    def LegalCorporateName(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._PartyLegalEntity}/cac:CorporateRegistrationScheme/cbc:Name', 
            value
        )
        self._LegalCorporateName = value

    @property
    def ContactName(self):
        return self._ContactName

    @ContactName.setter
    def ContactName(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._Party}/cac:Contact/cbc:Name', 
            value
        )
        self._ContactName = value

    @property
    def ContactTelephone(self):
        return self._ContactTelephone

    @ContactTelephone.setter
    def ContactTelephone(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._Party}/cac:Contact/cbc:Telephone', 
            value
        )
        self._ContactTelephone = value

    @property
    def ContactElectronicMail(self):
        return self._ContactElectronicMail

    @ContactElectronicMail.setter
    def ContactElectronicMail(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._Party}/cac:Contact/cbc:ElectronicMail', 
            value
        )
        self._ContactElectronicMail = value

    @property
    def CorporateRegistrationID(self):
        return self._CorporateRegistrationID

    @CorporateRegistrationID.setter
    def CorporateRegistrationID(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            f'{self._PartyLegalEntity}/cac:CorporateRegistrationScheme/cbc:ID', 
            value
        )
        self._CorporateRegistrationID = value