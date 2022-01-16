import phonenumbers
from phonenumbers import carrier, geocoder, timezone


mobile_no = input("Enter Mobile Number with Country Code: (Ex: +91 8220097133) =>")
mobile_no = phonenumbers.parse(mobile_no)


# Time Zone
print("Time Zone: ",timezone.time_zones_for_number(mobile_no))


# Carrier/Network
print("Network :", carrier.name_for_number(mobile_no,"en"))

# Country/region
print("Region: ",geocoder.description_for_number(mobile_no,"en"))

# Number is valid or not 
print("Valid Mobile Number :",phonenumbers.is_valid_number(mobile_no))



