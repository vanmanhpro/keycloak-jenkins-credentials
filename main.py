from keycloak import KeycloakAdmin
import json
import sys



if __name__ == "__main__":
    keycloak_admin = KeycloakAdmin(server_url='https://ec2-13-54-104-82.ap-southeast-2.compute.amazonaws.com/auth/',
                                    username=sys.argv[1],
                                    password=sys.argv[2],
                                    realm_name='e2e-tenancy',
                                    verify=False)
                                    
    print(json.dumps(keycloak_admin.get_clients(), indent=2))