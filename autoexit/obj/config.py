import secret
from traders import APIService


class AutoExitConfig: 
    def __init__(self, api_service:APIService, package:str, version:str) -> None:
        self.api_service:APIService = api_service

        if self.api_service == APIService.ALPHA_VANTAGE:
            self.api_key = secret.ALPHA_VANTAGE_API_KEY

        self.package_name = package
        self.version = version

    def __str__(self):
        return f"AutoExitConfig(api_key={self.api_key}, package_name={self.package_name}, version={self.version})"

    def __repr__(self):
        return str(self)