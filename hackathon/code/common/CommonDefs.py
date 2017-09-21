# Any publicly available server used for ICMP to check connection
PING_SERVER = "8.8.8.8"

# The unique identifier that maps the store-id to this RaPi deployment
STORE_ID = 1

# The no of attempts required before a system is made offline (2 hours - 8 attempts in 15 minute intervals)
OFFLINE_THRESHOLD_LIMIT = 8

# The no of attempts required before a system is made online (30 minutes - 2 attempts in 15 minute intervals)
ONLINE_THRESHOLD_LIMIT = 2

# Common definitions
HUL_INSTALL_DIR = "/usr/local/hul"
ONLINE_THRESHOLD = "OnlineThreshold"
OFFLINE_THRESHOLD = "OfflineThreshold"
IS_OFFLINE = "IsOffline"

# DB endpoint & credentials
cnx_str = {'host': 'museunilever.clpayxv3izmg.ap-south-1.rds.amazonaws.com',
           'username': 'i2i',
           'password': 'bridge!2!',
           'db': 'muse'}
