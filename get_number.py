import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("mobil telfon raqamni kiritng Mamlakat Kodi bilan birga\n")
mobileNo = phonenumbers.parse(mobileNo)

print(timezone.time_zones_for_number(mobileNo))

print('Kompaniya nomi: ',carrier.name_for_number(mobileNo,"uz"))

print('Mamlakat nomi: ',geocoder.description_for_number(mobileNo,"uz"))

print("Haqiqiy mobil raqami :",phonenumbers.is_valid_number(mobileNo))

print("raqamni tekshirish imkoniyati",phonenumbers.is_possible_number(mobileNo))
