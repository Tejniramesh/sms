from pymongo import MongoClient
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    MONGO_URI = st.secrets["MONGO_URI"]

DB_NAME = os.getenv("DB_NAME")

if not DB_NAME:
    DB_NAME = st.secrets["DB_NAME"]

client = MongoClient(MONGO_URI)

db = client[DB_NAME]

users_collection = db["users"]
contacts_collection = db["contacts"]
messages_collection = db["messages"]