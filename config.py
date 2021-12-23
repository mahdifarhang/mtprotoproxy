PORT = 443

# name -> secret (32 hex chars)
# USERS = {
# 	"tg": "00000000000000000000000000000001",
# 	"tg2": "0123456789abcdef0123456789abcdef",
# }
# GENERATE RANDOM SECRET TOKEN:
# hexdump -n 40 -e '4/4 "%08X" 1 "\n"' /dev/urandom

USERS = {
	# PAYINGUsers


	# VIPUsers
	"mahdi": "8c30229c8a693d2c242e74f960d244a3",
	"maha": "c7fd27b44680bdea99b29add6a509b8a",
	"maman": "682363a07be5c604a72249dcc7d0771a",
	"baba": "c4c997d116bdbe47ae2593d3e2b71f74",
	"morteza": "e7e0335bcf5879bea79312f1dd9923a2",
}

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

# in seconds
STATS_PRINT_PERIOD = 10 * 60
PREFER_IPV6=False

# MY_DOMAIN = 'farhang.com'

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "f5ff1ac8b6a32710eadf517dcb1bcdac"
