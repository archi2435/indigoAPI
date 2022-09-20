import requests
import re


'''
Python module to easy working with Indigo api
Here both version Indigo api are combined,
but you can use only api.v1 or api.v2
'''

class IndigoAPI_v1():

    '''
    Class for working with Indigo api v1
    where you can contor the profiles (start/stop)
    You can start the profile and manage it using the selenium
    '''
    
    def __init__(self, port=35000):
        self.host = f'http://127.0.0.1:{port}/api'

    def start_profile(self, uuid, tabs=True, automation=False):
        '''
        If tabs is true - Indigo launch previus browser tabs
        Automation - it's parameter for launch profile to automation software,
        if this parameter is true - return the port on where the profile is running
        '''
        query = f"/v1/profile/start?loadTabs={tabs}&automation={automation}&profileId={uuid}"
        result = requests.get(self.host + query).json()
        return result

    def stop_profile(self, uuid):

        query = f"/v1/profile/stop?profileId={uuid}"
        result = requests.get(self.host + query).json()
        return result

    # This feauture don't work now in Indigo api
    # def check_status(self, uuid):
    #     query = f"/v1/profile/active?profileId={uuid}"
    #     result = requests.get(self.host + query).json()
    #     return result # Return "True" if profile launch now


class IndigoAPI_v2():

    '''
    Class for working wich Indigo api v2
    where you can manage profiles: 
    create new frofiles, delete and update
    '''

    def __init__(self, port=35000):
        self.host = f'http://127.0.0.1:{port}/api'

    def get_profile(self, uuid=None, group=None, name=None, notes=None):
        '''
        Get list Indigo profiles 
        You can filter this list by multiple parameters
        '''
        query = '/v2/profile'
        result = requests.get(self.host + query).json()

        if uuid or group or name or notes:
            result_filtered = []

            if uuid:
                for profile in result:
                    if profile['uuid'] == uuid:
                        result_filtered.append(profile) 

            if group:
                for profile in result:
                    if profile['group'] == group:
                        result_filtered.append(profile) 

            if name:
                for profile in result:
                    if profile['name'] == name:
                        result_filtered.append(profile) 

            if notes:
                for profile in result:
                    if profile['notes'] == notes:
                        result_filtered.append(profile)
            
            return result_filtered 

        return result

    def create_profile(self, name, os='win', browser='mimic', 
                       group=None, googleServices=False, proxy=None):
        '''
        Create Indigo profiles wich user parameters
        '''
        query = '/v2/profile'
        body = {
            'name' : name,
            'os' : os,
            'browser': browser,
            'googleServices' : googleServices
        }

        if group:
            body['group'] = group

        if proxy:
            # proxy format "type:login:password:ip:port" or "type:login:password@ip:port"

            format_proxy = re.split(':|@', proxy)
            if len(format_proxy) != 5:
                return 'invalid proxy format'
            body["network"] = {
                "proxy" : {
                "type": format_proxy[0],
                "username": format_proxy[1],
                "password": format_proxy[2],
                "host": format_proxy[3],
                "port": format_proxy[4]
                }
            }

        result = requests.post(self.host + query, json=body).json()
        return result # return profile uuid

    def del_profile(self, uuid):
        query = f'/v2/profile/{uuid}'
        result = requests.delete(self.host + query).status_code

        if result == 204:
            return 'Delete is completed'

        else:
            return 'Delete is not completed'

    def update_profile(self, uuid, name=None, os=None, browser=None, 
                       group=None, googleServices=None, proxy=None, notes=None):
        '''
        Update Indigo profile parameters
        '''
        query = f'/v2/profile/{uuid}'
        body = {}

        if name:
            body['name'] = name

        if os:
            body['os'] = os

        if browser:
            body['browser'] = browser

        if group:
            body['group'] = group

        if googleServices:
            body['googleServices'] = googleServices

        if proxy:
            # proxy format "type:login:password:ip:port" or "type:login:password@ip:port"

            format_proxy = re.split(':|@', proxy)
            if len(format_proxy) != 5:
                return 'invalid proxy format'
            body["network"] = {
                "proxy" : {
                "type": format_proxy[0],
                "username": format_proxy[1],
                "password": format_proxy[2],
                "host": format_proxy[3],
                "port": format_proxy[4]
                }
            }

        if notes:
            body['notes'] = notes
            
        result = requests.post(self.host + query, json=body)
        return result # return profile uuid


class IndigoAPI(IndigoAPI_v1, IndigoAPI_v2):

    '''
    Class where combined both version Indigo api
    You can here useng all features Indigo api v1 and Indigo api v2
    '''

    def __init__(self, port=35000):
        super().__init__(port)
