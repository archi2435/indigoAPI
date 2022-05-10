# Python Indigo API

**It's unofficial module based on [Swagger documentation](https://app.swaggerhub.com/apis/Multilogin/MultiloginLocalRestAPI/1.0#/Misc/ActiveGet 'SwaggerHub Indigo API documentation')**

## 1 Discription

Module to easy the work wich Indigo API. Here both version API are combined. But you can use only Indigo API v1 or Indigo API v2.  

You can use this module wich Python selenium for create automation scripts. If you're going use Indigo API wich Python selenium, web sites will not understand that you are using third-party software.  

***

## 2 First setting

This module will not work if you have not defined the Indigo port.  
[Instruction on official site](https://help-faq.indigobrowser.com/ru/knowledge-bases/2/articles/406-cli-i-local-api)  

1. Open file "**app.properties**" in directory: "**C:\Users\%username%\.indigobrowser**"  
2. Add string "**multiloginapp.port=[PORT_NUMBER]**" in this file.  
*In module default port = 35000, but you can use any other*  
3. Save file.  

***  

## 3 Start work and documentation

You need to make an object based on class "**IndigoAPI**" to start the work with module:  
*in class "IndigoAPI" combined both versions API i was talking about. You can take class "IndigoAPI_v1" or "IndigoAPI_v2" to use one of the API versions*

    indigo = IndigoAPI()

If yoг're indigo port != 35000, set it when creating an object:

    indigo = IndigoAPI(port=[PORT_NUMBER])

### 3.1 List all methods

    indigo = IndigoAPI()

    indigo.start_profile()
    indigo.stop_profile()
    indigo.get_profile()
    indigo.create_profile()
    indigo.del_profile()
    indigo.update_profile()

***

### 3.2 Start profile

    indigo.start_profile(uuid=[uuid], tabs=[Boolean], automation=[Boolean])
    # uuid is required parameter

You need set profile uuid to start profile  
*uuid - unique profile id*  

    indigo.start_profile(uuid=[uuid])

Add parameter "tabs=False" if you not going load previus browser tabs.  
*Default tabs=True*  

    indigo.start_profile(uuid=[uuid], tabs=False)  

Add parameter "automation=true" if you going use automation scripts.  
*Default automation=False*  

    indigo.start_profile(uuid=[uuid], automation=true)  

***

### 3.3 Start profile with Python selenium

If "automation=true" function return port where launched indigo profile. You can use this port for connection selenium to Indigo.

    from selenium import webdriver


    indigo = IndigoAPI()
    profile = indigo.start_profile(uuid=[uuid], automation=true)
    # port profile == profile['value']

    opts = options.DesiredCapabilities()
    driver = webdriver.Remote(command_executor=profile['value'], desired_capabilities={})

***

### 3.4 Stop profile

You need set only uuid to stop profile

    indigo_stop_profile(uuid=[uuid])
    # uuid is required parameter

***

### 3.5 Get profile

    indigo.get_profile(uuid=[uuid], group=[group_id], name=[name], notes=[notes])

Use this method for get profile list. You can set some parameters by which the returned list will be filtered.

***

### 3.6 Create profile

    indigo.create_profile(name=[name], os=[os], 
                          browser=[browser], group=[group_id],
                          googleServices=[Boolean], proxy=[proxy])
    # name is required parameter

Use this method for create a new profile in indigo browser. Set pameters to change profile information.  

* **name = name**
* **os = "win" (default) / "mac" / "lin" / "android"**
* **browser = "mimic" (default) / "stealthfox" / "mimic_mobile"**
* **group = group_id**
* **googleServices = True / False**
* **proxy = proxy**

***

### 3.7 Create profile with proxy

Use this format when add proxy in profile: "**type:login:password:ip:port**"

    indigo.create_profile(name=[name], proxy="hhtp:login:password:1.1.1.1:1111")
    indigo.create_profile(name=[name], proxy="sooks4:login:password:1.1.1.1:1111")
    indigo.create_profile(name=[name], proxy="sooks5:login:password:1.1.1.1:1111")  

You can also use this format "**type:login:password@ip:port**"  

    indigo.create_profile(name=[name], proxy="hhtp:login:password@1.1.1.1:1111")
    indigo.create_profile(name=[name], proxy="sooks4:login:password@1.1.1.1:1111")
    indigo.create_profile(name=[name], proxy="sooks5:login:password@1.1.1.1:1111")

***

### 3.8 Delete profile

You need set only uuid for delete profile

    indigo.del_profile(uuid=uuid)  

***

### 3.9 Update profile settings

    indigo.update_profile(self, uuid, name=None, os=None, 
                          browser=None, group=None, googleServices=None, 
                          proxy=None, notes=None)
    # uuid is required parameter  

Use this method to change profile settings. You can set some parameters to change.  

* **name = name**
* **os = "win" (default) / "mac" / "lin" / "android"**
* **browser = "mimic" (default) / "stealthfox" / "mimic_mobile"**
* **group = group_id**
* **googleServices = True / False**
* **proxy = proxy**
* **notes = notes**  

***

## 4 Indigo API v1 methods

You can use indigo API v1 if you need only control a profiles  

    indigo = IndigoAPI_v1()

    indigo.start_profile(uuid)
    indigo.stop_profile(uuid)

***

## 5 Indigo API v2 methods

Use indigo API v2 if you need only managment a profiles

    indigo = IndigoAPI_v2()

    indigo.get_profile()
    indigo.create_profile(name)
    indigo.del_profile(uuid)
    indigo.update_profile(uuid)