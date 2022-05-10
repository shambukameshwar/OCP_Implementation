*** Settings ***
Suite Setup       ArchiveFile    # Archving Result files to zip
Suite Teardown    MoveFileToArchive    # Moving Archived files to Archive folder
Library           DateTime    #Suite Teardown    XrayResultsUpload    #Test Teardown    TestStatusUpdateJson    #Suite Setup    Selfcare_MoveFileToArchive    #Suite Teardown    XrayResultsUpload    #Test Teardown    TestStatusUpdateJson
Resource          ../../ResourceData/Resources.txt
Library           OperatingSystem
Resource          ../../Keywords/Demo_Keyword.txt
Resource          ../../Keywords/Demo_Setup_TearDown.txt
Library           XML
Resource          ../../ResourceData/Demo/Demo_Locators.txt
Library           ScreenCapLibrary
Library           String
Library           BuiltIn
Library           OperatingSystem
Library           AppiumLibrary
Library           CSVLibrary

*** Test Cases ***
TC_01_MobileApp_Ondemand
    #loginToChatApplication
    Open_chat_Application
    Comment    Popup_alert
    login_with_user
    logout_user

TC_02_MobileApp_Cloud
    #loginToChatApplication
    Open_chat_Application_Cloud
    Comment    Popup_alert
    login_with_user
    logout_user
