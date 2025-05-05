# backend/services/smartapi_service.py
import os
from dotenv import load_dotenv, find_dotenv

# Force-load and override OS vars with your project’s .env
load_dotenv(find_dotenv(), override=True)

#DEBUG: verify correct variables
"""print("🔍 Using .env at:", find_dotenv())
print("🔑 CLIENT_ID    =", os.getenv("CLIENT_ID"))
print("👤 USERNAME     =", os.getenv("USERNAME"))
print("🔒 TOTP_SECRET  =", os.getenv("TOTP_SECRET"))"""
from SmartApi.smartConnect import SmartConnect
import pyotp
from logzero import logger

# … rest of your code …



# Load .env
if not load_dotenv():
    raise RuntimeError("❌ Could not find a .env file")

API_KEY     = os.getenv("CLIENT_ID")
USERNAME    = os.getenv("USERNAME")
PASSWORD    = os.getenv("PASSWORD")
TOTP_SECRET = os.getenv("TOTP_SECRET")

for var, val in [
    ("CLIENT_ID",     API_KEY),
    ("USERNAME",      USERNAME),
    ("PASSWORD",      PASSWORD),
    ("TOTP_SECRET",   TOTP_SECRET),
]:
    if not val:
        raise RuntimeError(f"❌ {var} not set in .env")

class SmartAPIService:
    _client: SmartConnect = None

    @classmethod
    def login(cls):
        # 1) Instantiate with only the API_KEY
        cls._client = SmartConnect(API_KEY)

        # 2) Generate a fresh TOTP
        totp = pyotp.TOTP(TOTP_SECRET).now()

        # 3) Call generateSession(clientcode, password, totp)
        session = cls._client.generateSession(USERNAME, PASSWORD, totp)
        if not session.get("status", False):
            raise Exception(f"SmartAPI login failed: {session}")

        # 4) Extract & set the JWT
        jwt = session["data"]["jwtToken"]
        cls._client.setAccessToken(jwt)

        logger.info("✅ SmartAPI login successful")
    @classmethod
    def get_jwt(cls):
        return cls._jwt_token
