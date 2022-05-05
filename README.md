# Selenium Gmail Login - Example (Python)

## Description
This repo gives an example on how to run an automated browser using Selenium and Python that uses an existing Gmail session by utilizing Google Chrome debug mode. By doing so, it's possible to automate many feature that is locked behind authentication without and bypass the 2FA that might prevent the automated script to run properly. The development of this simple script was done in a Windows machine.

A simple automated example will be following a very simple flow

1. The Chrome Browser (Debug Mode) which already contains logged in Gmail Account will be automated to perform simple Gmail authentication
2. The automated browser will visit https://todoist.com login page
3. The automated browser will select Gmail as an authentication method and select the account that you need to edit in the script

## Steps
### 1. Install Python
<br>

### 2. Install pip
<br>

### 3. Install Virtual Environment (optional, recommended)
<br>

### 4. Install Selenium
If you're using Virtual Environment don't forget to activate it. If you're using Windows and got execution policy error, try running `Set-ExecutionPolicy Unrestricted -Scope Process`.

After everything is running well and Selenium can be installed, run `pip install selenium`
<br>

### 5. Add Google Chrome Path to Environment Variables
In Windows, go to start menu and search "Edit the system environment variables", find "Environment Variables" button in the "Advanced" Tab. Find Path variable, click edit, and add your Google Chrome directory (Mine was "C:\Program Files\Google\Chrome\Application").
<br>

### 6. Try running Chrome in debug mode
Open PowerShell and try running

`start chrome -remote-debugging-port=9014 --user-data-dir="<PATH_TO_ANY_DIRECTORY>"`

If you did the step 5 correctly, a new Chrome Window should be opened. Keep in mind that this browser use port 9014 in the example. The PATH_TO_ANY_DIRECTORY should be a new, empty folder since there will be a lots of content generated to that path.
<br>

### 7. Login into Gmail account in the Chrome debug mode
Just login as usual in this newly opened browser. Even after you close the browser, the login session should be remained in that browser as long as the user data directory is remained untouched. This Gmail account will be used in step 8.

### 8. Edit your Gmail account in script
Check script.py and edit GMAIL_ACCOUNT variable
<br>

### 9. Run the script
With the debug browser is opened and the Gmail account logged in into the browser, you can now run the script.

Run `python script.py`
<br>

### 10. Watch if the automation is working
<br>
