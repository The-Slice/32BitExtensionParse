Just a couple of things to be aware of when running this script.

YOU NEED TO HAVE RUN THIS SCRIPT AS AN EXTENSION ATTRIBUTE FIRST: 32BitExtensionAttribute.py

For this script:

You will need to know the the first computer ID on your Jamf server and your last ID as well. This is because it will iterate through each computer to grab it's 32 Bit extension attribute list

You will need to input a user with (bare minimum) read access for everything (I didn't want to get too detailed, also I'm lazy)

You will need to create a text file beforehand (empty)

These are all things you will need to change in the script before running it

You will most likely see "duplicates", this is not truly the case, they simply have different version numbers (which are displayed)

I'm going to guess the most asked question will be how to get the computer start ID's and end ID's. Those can be found by going to your JPS URL and tacking a /api to the end of it: https://YOURURL.com/api

Once there, go to /computers and use the GET on the /computers option. Choose the first ID and then go aaaaaaaaallllll the way to the bottom for the last ID.

Have fun!
