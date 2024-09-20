# **Automating Google sheets with GSpread**   
This project demonstrates automated interactions with a Gooogle Sheet using GSpread library. The entire project covers and outlines reading, writing, updating, deleting data/rows annd autommating calculative tasks(in this case summing up values) inn a common time interval.  
## **Project Overview**   
The script enables connection to a Google sheet using Google sheets and Google drive API.  
The followinng operations are performed withhin the script:   
1. **Connecting to Google sheet**: The script authennticates with Google sheet API usinng OAUth2 and a service account to obtain credential files in json fromat.
2. **Reads Gooogle sheet**: Reads the data rows and columns in the Google sheet
3. **Writes data in to the Google sheet**: Writes data into a specified cell of the Google sheet
4. **Updates new data into existing rows or cells in the Google sheet**
5. **Deletes Data**: Deletes speciffic rows in the Google sheet
6. **Automate Tasks**: This opperation runs periodically(60 seccs) to sum the numeric values in a speccified column and updates the result to a specified cell in the Google Sheet 
