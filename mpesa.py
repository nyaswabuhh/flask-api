import base64
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime


shortcode="174379"
callback_url="https://e49a82ede2d6.ngrok-free.app/mpesa/callback"
pass_key="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
token_url="https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
stk_push_url="https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
SAF_STK_PUSH_QUERY_API="https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"

headers={}
def get_mpesa_access_token():
    try:
        res = requests.get(token_url,
            auth=HTTPBasicAuth(consumer_key, consumer_secret),
        )
        token = res.json()['access_token']

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        print(headers)
    except Exception as e:
        print(str(e), "error getting access token")
        raise e

    return token

def generate_password():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    password_str = shortcode + pass_key + timestamp
    password = base64.b64encode(password_str.encode()).decode()
    return password, timestamp

def make_stk_push(amount, phone, sale_id):
    token = get_mpesa_access_token()
    password, timestamp = generate_password()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    

    push_data = {
        "BusinessShortCode": shortcode,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": int(amount),
        "PartyA": str(phone),
        "PartyB": shortcode,
        "PhoneNumber": str(phone),
        "CallBackURL": callback_url,
        "AccountReference": str(sale_id),
        "TransactionDesc": "Flask API Test",
    }

    response = requests.post(
        stk_push_url,
        json=push_data,
        headers=headers)

    response_data = response.json()

    print(response_data)

    return response_data

# get_mpesa_access_token()

# make_stk_push(3, "254724948170")
