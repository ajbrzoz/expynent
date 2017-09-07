import re

import expynent

# RegEx pattern that matches a credit card number.
# Match:
#    - 3519 2073 7960 3241
#    - 3519-2073-7960-3241
#    - 3519 2073-7960 3241
#    - 3519207379603241
CREDIT_CARD = re.compile(expynent.CREDIT_CARD)

# RegEx pattern that strictly matches a credit card number.
# Match:
#    - 1111-2222-3333-4444
#    - 1111 2222 3333 4444
#    - 1111222233334444
CREDIT_CARD_STRICT = re.compile(expynent.CREDIT_CARD_STRICT)

# RegEx pattern that match slug.
# Match:
#    - greatest-slug-ever
SLUG = re.compile(expynent.SLUG)

# RegEx pattern that match hex value.
# Match:
#    - #a3c113
HEX_VALUE = re.compile(expynent.HEX_VALUE)

# RegEx pattern that match IPv4 address.
# Match:
#    209.18.181.23
IP_V4 = re.compile(expynent.IP_V4)

# RegEx pattern that match IPv6 address.
# Match:
#    2001:0db8:85a3:0000:0000:8a2e:0370:7334
IP_V6 = re.compile(expynent.IP_V6, re.VERBOSE | re.IGNORECASE | re.DOTALL)

# RegEx pattern that match MAC address.
# Match:
#    - 00:08:C7:1B:8C:02
MAC_ADDRESS = re.compile(expynent.MAC_ADDRESS)

# RegEx pattern that match datetime in ISO 8601 format.
# Match:
#    - 1BoatSLRHtKNngkdXEeobR76b53LETtpyT
BITCOIN_ADDRESS = re.compile(expynent.BITCOIN_ADDRESS)

# RegEx pattern that match Yandex.Money account.
# Match:
#    - 97508675463414
YANDEX_MONEY = re.compile(expynent.YANDEX_MONEY)

# RegEx pattern that match longtitude
# Match:
#    - 112.1844026051194
LONGITUDE = re.compile(expynent.LONGITUDE)

# RegEx pattern that match latitude
# Match:
#    - -66.4214188124611
LATITUDE = re.compile(expynent.LATITUDE)

# RegEx pattern that match dtime in 24 hour format
# Match:
#    - 23:45
TIME_24H_FORMAT = re.compile(expynent.TIME_24H_FORMAT)

# RegEx pattern that match datetime in ISO 8601 format.
# Match:
#    - 2014-12-05T12:30:45.123456-05:30
ISO_8601_DATETIME = re.compile(expynent.ISO_8601_DATETIME)

# RegEx pattern that match ISBN 10 and ISBN 13.
# Match:
#    - ISBN-13: 978-1-56619-909-4
#    - ISBN-13: 978 5 93286 159 2
#    - 978-1-56619-909-4
#    - ISBN-10: 1-56619-909-3
#    - 1-56619-909-3
#    - 978 1 56619 909 4
#    - 1 56619 909 3
ISBN = re.compile(expynent.ISBN)

# RegEx pattern that match binary numbers.
# Match:
#    - L
#    - XL
#    - XV
#    - XX
#    - XI
#    - etc.
ROMAN_NUMERALS = re.compile(expynent.ROMAN_NUMERALS)

# RegEx pattern that matches Ethereum address starts with 0x
# Match:
#    - 0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe
#    - 0x5ed8cee6b63b1c6afce3ad7c92f4fd7e1b8fad9f
#    - 0xfac399e49f5b6867af186390270af252e683b154
#    - 0x85fc71ecffb0703a650f05263a3c1b0548092f32
ETHEREUM_ADDRESS = re.compile(expynent.ETHEREUM_ADDRESS)

# RegEx pattern that matches UUID's.
# Match:
#    - 54de7ea8-e01b-43c9-ad38-382d9e5f62ef
#    - 54DE7EA8-E01B-43C9-AD38-382D9EFF62EF
UUID = re.compile(expynent.UUID)

# RegEx pattern that matches float numbers
# Match:
#    - 1.1
#    - 3.1e10
#    - 1.2e+10
#    - 1.2e-10
#    - -1.2e-10
#    - 5.1E10
FLOAT_NUMBER = re.compile(expynent.FLOAT_NUMBER)

# RegEx pattern to match PESEL
PESEL = re.compile(expynent.PESEL)
