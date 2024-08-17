TELEGRAM_BOT_TOKEN = 'put your telegram token here'

URLS = {
    "login_url": "https://attendence-system-1910.vercel.app/api/auth/login",
    "sub_url": "https://attendence-system-1910.vercel.app/api/attendances/details",
    "att_d_url": "https://attendence-system-1910.vercel.app/api/students/attendances/details",
    "lout_url": "https://attendence-system-1910.vercel.app/api/auth/logout"
}

# Dictionary to keep track of user states and data
user_states = {}
user_data = {}
