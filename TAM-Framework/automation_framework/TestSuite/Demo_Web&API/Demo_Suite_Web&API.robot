*** Settings ***
Suite Setup       ArchiveFile    # Archving Result files to zip
Suite Teardown    MoveFileToArchive    # Moving Archived files to Archive folder
Library           DateTime    #Suite Teardown    XrayResultsUpload    #Test Teardown    TestStatusUpdateJson    #Suite Setup    Selfcare_MoveFileToArchive    #Suite Teardown    XrayResultsUpload    #Test Teardown    TestStatusUpdateJson
Resource          ../../ResourceData/Resources.txt
Library           OperatingSystem
Resource          ../../Keywords/Demo_Keyword.txt
Resource          ../../Keywords/Demo_Setup_TearDown.txt
Library           XML
Library           RPA.JSON
Library           RPA.Database
Library           RPA.Browser.Selenium
Library           RPA.Desktop
Resource          ../../ResourceData/Demo/Demo_Locators.txt
Library           ScreenCapLibrary
Library           String
Library           BuiltIn
Library           OperatingSystem
Library           CSVLibrary

*** Test Cases ***
TC_01_WebApp
    [Tags]    QAD-45351
    ${executionname}    Set Variable    @{TEST_TAGS}
    Log    ${executionname}
    @{dict}=    read csv file to associative    ${Demo_CSV_FILE}
    log many    ${dict}
    ${dictlen}=    Get length    ${dict}
    ${i}    Set Variable    1
    FOR    ${i}    IN RANGE    ${dictlen}
        Log    ${executionname}
        IF    "${executionname}" == "${dict[${i}]['JiraID']}" and "${dict[${i}]['Flag']}" == "Y"
        ${testData}    BuiltIn.Set Variable    ${dict[${i}]}
        BuiltIn.Set Global Variable    ${testData}
        Log    ${testData}
        Demo_VariableValueRetreive
        Start Video Recording
        Saucedemo_URL
        Login_Saucedemo
        Purchase_Order
        Comment    To Check User
        Close Browser
        Stop Video Recording
    END
    END

TC_02_API
    ${endpoint}    Set Variable    https://restful-booker.herokuapp.com
    Create Session    alias    ${endpoint}
    &{headers}    Create Dictionary    Content-Type=application/json    charset=UTF-8
    ${response}    Get Request    alias    /booking    headers=${headers}
    Log    ${response}
    ${status}    Set Variable    ${response.status_code}
    Log    ${status}
    Log    ${response.text}
    Run Keyword If    "${status}"!="200"    Fail
    ${response}    Set Variable    ${response.text}
    ${response}    BuiltIn.Convert To String    ${response}
    ${response}    To Json    ${response}
    Save JSON to file    ${response}    ${CURDIR}/../../ResultFile/Result/DemoAPI.json
