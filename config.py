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
	"iman_nikfarjam":"39322599C9587F892FFFA00B1237DFB4",
	"hamid_ijadi":"502AAD8FD39379FFD3B93390DEAAA936",
	"ali_khatib":"7F50135D7D626BDE4898A045B6D00CC9",
	"mahdi_mashayekhi":"5A0F8D3E7B45B634F0BA0FF9FFFE7098",
	"mahdi_sarhaddi":"719BAAF0B9334B53940FAB00B7A8F1FF",
	"amirv":"F156C259B8273AF306B8F22029B170D4",
	"moghaddas":"E4E3A9295939F7EFA1EEFA64F758B87D",
	"hasan":"87F39124014D040A37B628FE7DB65FDD",
	"mansouri":"F0869A239BAF4097DFDB827C108FACF8",
	"lotfi":"F9C29F1B45019460406BC145F0057E6E",

        "smaple5":"C68131AD5E5C51A2EE6B7399D6CD12B3",
        "smaple6":"D1FF5AF7887D90BD845AFD21F55DBC12",
        "smaple7":"D8BA0F5968DBFD8255150D1829618489",
        "smaple8":"0E46B670E051C5C669C73FDF8F9C80F4",
        "smaple9":"3C39173B1D7E1A56710508F1CF7AE184",
        "smaple10":"4D407B74100D3073D2C3EA79E6E4826F",
        "smaple11":"9205F7F0BEA80DC4D4CED36A68595013",
	"smaple12":"96C256450017D52F465ED0D0E0DFE9F1",


	# VIPUsers
	"mahdi":"4431FC98E74DFBF11E8CD0EA8FF03F10",
#	"test": "8c30229c8a693d2c242e74f960d244a3",
	"test": "28EF69567C37329FBA6DDB52056E5529",

	"maha": "7E25CF28473602881491DACB5E4E901A",
	"maman": "1140C6C7CA5352C588FEB90AF522ADDB",
	"baba": "5CE31F8DAC94EE69908E104173D1440E",
	"morteza": "C04E6B90075BE1CBE0085F6FA38C4DD5",
	"maryam":"D39F14A1C3DA64F9AF161F361FACC947",
	"zahouri":"90201B54D8D300FC4524B88A80DAA086",
        "roya":"1705FFCEB849DA3D240EC518C3DDEA20",
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
STATS_PRINT_PERIOD = 60 * 60
PREFER_IPV6=False

MY_DOMAIN = 'mfarhang.ir'

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "f5ff1ac8b6a32710eadf517dcb1bcdac"
