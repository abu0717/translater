import requests, os
url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
soz = input('Tarjima qilmoqchi bol\'lgan so\'zingizni kiriting: ')
tilni_tanlang = input('uz, ru, en\nkiritadigan so\'zingizni tilini shunday ko\'rinishda kiriting: ')
tarjima_qilmoqchi = input('uz, ru, en\nko\'rinishida tarjima qilmoqchi bolgan tilingizni tanlang: ')
os.system('clear')
payload = {
	"q": f"{soz}",
	"target": f"{tarjima_qilmoqchi}",
	"source": f"{tilni_tanlang}"
}



headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "26695146d6mshd355a859397fcdbp101dafjsnfd8e01908979",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)
sozlar = response.json()
print(sozlar['data']['translations'][0]['translatedText'])