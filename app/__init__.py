"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa46rhp8u791gs3b6g-a.oregon-postgres.render.com",
        database="to_do_buzz",
        user=" to_do_buzz_user",
        password="xKPlqicyIsz3i7picQE5CMCYRxMPMaAR")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
