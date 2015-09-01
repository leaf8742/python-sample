#!/usr/bin/env python
# -*- coding: utf-8 -*-

class UserInformation:
    objectList = None
    accountType = None
    email = ""
    mobile = ""
    name = ""
    gender = "male"
    passwd = ""
    autoSignIn = False
    rememberPasswd = False
    sessionID = ""
    deviceTokenString = "INVALID_DEVICETOKEN"
    colorScheme = "default"
    binded = False
    picture = None
    mementoPicture = None
    
    def __init__(self,
                 objectList = None,
                 accountType = None,
                 email = "",
                 mobile = "",
                 name = "",
                 gender = "male",
                 passwd = "",
                 autoSignIn = False,
                 rememberPasswd = False,
                 sessionID = "",
                 deviceTokenString = "INVALID_DEVICETOKEN",
                 colorScheme = "default",
                 binded = False,
                 picture = None,
                 mementoPicture = None):
        self.objectList = objectList;
        self.accountType = accountType;
        self.email = email;
        self.mobile = mobile;
        self.name = name;
        self.gender = gender;
        self.passwd = passwd;
        self.autoSignIn = autoSignIn;
        self.rememberPasswd = rememberPasswd;
        self.sessionID = sessionID;
        self.deviceTokenString = deviceTokenString;
        self.colorScheme = colorScheme;
        self.binded = binded;
        self.picture = picture;
        self.mementoPicture = mementoPicture;

    def description(self):
        print("objectList:", self.objectList,
              "\naccountType:", self.accountType,
              "\nemail:", self.email,
              "\nmobile:", self.mobile,
              "\nname:", self.name,
              "\ngender:", self.gender,
              "\npasswd:", self.passwd,
              "\nautoSignIn:", self.autoSignIn,
              "\nrememberPasswd:", self.rememberPasswd,
              "\nsessionID:", self.sessionID,
              "\ndeviceTokenString:", self.deviceTokenString,
              "\ncolorScheme:", self.colorScheme,
              "\nbinded:", self.binded,
              "\npicture:", self.picture,
              "\nmementoPicture:", self.mementoPicture)
