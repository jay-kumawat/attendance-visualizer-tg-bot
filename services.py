import requests as rs
import pandas as pd
from utils import json_decode
from collections import defaultdict

def fetch_data(urls, login_data, user_id, bot):
    data = defaultdict(dict)
    with rs.Session() as s:
        try:
            # Attempt login
            response = s.post(urls["login_url"], data=login_data)
            if response.status_code != 200:
                bot.send_message(user_id, "Login failed. Please check your credentials and try again.")
                return pd.DataFrame()

            # Extract token from Set-Cookie header
            set_cookie_header = response.headers.get('Set-Cookie')
            if not set_cookie_header:
                bot.send_message(user_id, "Authentication token missing. Login might have failed.")
                return pd.DataFrame()

            token_start_index = set_cookie_header.find('token=') + len('token=')
            token_end_index = set_cookie_header.find(';', token_start_index)
            token = set_cookie_header[token_start_index:] if token_end_index == -1 else set_cookie_header[token_start_index:token_end_index]

            # Fetch data
            header = {"Authorization": f"Bearer {token}"}
            sub_url_response = s.get(urls["sub_url"], headers=header)
            if sub_url_response.status_code != 200:
                bot.send_message(user_id, "Failed to fetch the subject data.")
                return pd.DataFrame()

            payload = json_decode(sub_url_response.content)
            if not payload:
                bot.send_message(user_id, "No subjects data to process.")
                return pd.DataFrame()

            for key in payload.keys():
                att_data_response = s.post(urls["att_d_url"], json=payload[key], headers=header)
                if att_data_response.status_code != 200:
                    bot.send_message(user_id, f"Failed to fetch attendance data for {key}.")
                    continue

                data[key] = att_data_response.json()

            print("\rData Fetched Successfully", end='', flush=True)

        except Exception as e:
            bot.send_message(user_id, f"An error occurred: {str(e)}")

        finally:
            # Ensure logout is attempted
            lout_response = s.post(urls["lout_url"], headers=header, data={})
            if lout_response.status_code == 200:
                print("\rLogged Out Successfully", flush=True)
            else:
                print("\rFailed to log out", flush=True)

    return pd.DataFrame(data)
