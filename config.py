from my_configs import *

PORT = 443

# name -> secret (32 hex chars)
# USERS = {
    # "tg":  "00000000000000000000000000000001",
    # "tg2": "0123456789abcdef0123456789abcdef",
# }
# GENERATE RANDOM SECRET TOKEN:
# hexdump -n 40 -e '4/4 "%08X" 1 "\n"' /dev/urandom

USERS = {**PAYINGUsers, **VIPUsers}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "www.gitlab.com"

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "f5ff1ac8b6a32710eadf517dcb1bcdac"
