import gspread
from google.oauth2.service_account import Credentials
import sys
import time


def authenticate_auto_task(json_file, sh):
    # Authenticating and connecting with the Google sheet using the downloaded credential file
    # sys - to exit the script if the authentication function fails
    try:
        scopes = ['https://www.googleapis.com/auth/spreadsheets',
                  'https://www.googleapis.com/auth/drive']
        credentials = Credentials.from_service_account_file(json_file, scopes=scopes)
        sheet = gspread.authorize(credentials).open(sh).sheet1
        return sheet
    except gspread.exceptions.APIError:
        print("Failed to connect to Google Sheets API")
        sys.exit(1)
    except FileNotFoundError:
        print("Cross-check filepath: Json credential file not found")
        sys.exit(1)


def read_data(sh):
    # read  the data from the automated task sheet
    try:
        auto_file = sh.get_all_records()
        for row in auto_file:
            print(row)
    except gspread.exceptions.APIError:
        print("Failed to read data in Google sheet")
    except Exception as e:
        print(f"Unexpected error in reading data: {e}")


def write_data(sh, new_row):
    # Write a new row into the automated gtask sheet
    try:
        sh.append_row(new_row)
    except gspread.exceptions.APIError:
        print("Failed to write new data into Google sheet")
    except ValueError as e:
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"Error occurred while inputting/writing new data: {e}")


def update_data(sh, row, column, value):
    # update/change one of the values in the column/row of the google sheet
    try:
        sh.update_cell(row, column, value)
    except gspread.exceptions.APIError:
        print("Failed to update new data into Google sheet")
    except Exception as e:
        print(f"Unexpected Error in updating google sheet: {e}")


def delete_data(sh, row):
    # something went wrong here - apparently gspread does not have the delete_row attribute
    # Delete a specific row from the auto task google sheet
    try:
        sh.delete_rows(row)
    except gspread.exceptions.APIError:
        print('Failed to delete row in google sheet')
    except Exception as e:
        print(f"Unexpected error in deleting row: {e}")


def automate_data(sh, column_index):
    # Automate sheet to run every minute(60 secs)
    # get total sum of prices in the Price column
    # update the sum on a cell of the Google sheet
    # wait a minute until the next run
    try:
        while True:
            auto_data = sh.get_all_values()
            if len(auto_data) == 1:
                raise ValueError("Length of data should be more than 1")

            try:
                total_price = sum([int(row[0]) for row in auto_data[column_index:]])
            except ValueError:
                raise ValueError("Incorrect Data format: Data should be numeric")

            sh.update_cell(12, 199, total_price)
            print(f"Total Price: {total_price}")
            time.sleep(60)
    except gspread.exceptions.APIError as e:
        print(f'Automation  failed: {e}')
    except ValueError as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    cred_file = r"C:\Users\ayemi\Downloads\resolute-button-436012-j3-08389d26c3b4.json"
    sheet_name = "Automation Task"
    auto_sheet = authenticate_auto_task(cred_file, sheet_name)

    read_data(auto_sheet)
    write_data(auto_sheet, ["9/30/2023", "3:05", "Night", "FcB 0001-00000514", "9", str(406),
                            "Toba", str(3004), "Campari", 1, 1100, 1100])
    update_data(auto_sheet, 75, 3, "Morning")
    delete_data(auto_sheet, 195)

    automate_data(auto_sheet, 11)
