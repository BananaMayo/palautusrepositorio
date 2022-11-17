*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input Register Command
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Register Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Register Command
    Input Credentials  ka  kalle123
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Register Command
    Input Credentials  kalle  kal123
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Register Command
    Input Credentials  kalle  kalkkeaar
    Output Should Contain  Must contain at least one special character
