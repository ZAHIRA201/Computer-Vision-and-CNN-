import cv2
from flet import *
import pytesseract

# Dictionnaire de traduction
translation_dict = {
    'provinsi': 'Province',
    'kabupaten': 'Département',
    'nik': 'Numéro d\'identification',
    'name': 'Nom',
    'jenis_kelamin': 'Genre',
    'gol_darah': 'Groupe sanguin',
    'alamat': 'Adresse',
    'kelurahan': 'Village',
    'kecamatan': 'Commune',
    'agama': 'Religion',
    'status_perkawinan': 'État civil',
    'pekerjaan': 'Profession',
    'berlaku_hingga': 'Valable jusqu\'à'
}

def translate_field(field, value):
    field_translated = translation_dict.get(field, field)
    return field_translated, value

def main(page: Page):
    
    page.scroll = "auto"
    inputKtp = TextField(label="Insérez votre carte ici")
    
    con_result = Container(
        padding=10,
        content=Column([
            Text("Résultat de votre carte", size=30),
            TextField(label="Province"),
            TextField(label="Département"),
            TextField(label="Numéro d'identification"),
            TextField(label="Nom"),
            TextField(label="Genre"),
            TextField(label="Groupe sanguin"),
            TextField(label="Adresse"),
            TextField(label="Commune"),
            TextField(label="Religion"),
            TextField(label="État civil"),
            TextField(label="Profession"),
            TextField(label="Valable jusqu'à"),
        ])
    )

    def processfile(e):
        img = cv2.imread(inputKtp.value)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
        result = pytesseract.image_to_string(threshed)
        print(result)

        data = {}
        for word in result.split("\n"):
            split_word = word.split(" ")
            if len(split_word) >= 2:
                if "PROVINSI" in word:
                    data['provinsi'] = ' '.join(split_word[-2:])
                elif "KABUPATEN" in word:
                    data['kabupaten'] = split_word[-1]
                elif "NIK" in word:
                    data['nik'] = split_word[-1]
                elif "Nama" in word:
                    data['name'] = ' '.join(split_word[1:])
                elif "Tempat/Tgl Lahir" in word:
                    data['tempat_tgl_lahir'] = ' '.join(split_word[-3:])
                elif "Jenis Kelamin" in word:
                    data['jenis_kelamin'] = split_word[1]
                    data['gol_darah'] = split_word[-1]
                elif "Alamat" in word:
                    data['alamat'] = result[result.index(word) + len(word):result.index(word) + len(word) + 26].strip()
                elif "Kel/Desa" in word:
                    data['kelurahan'] = split_word[-1]
                elif "Kecamatan" in word:
                    data['kecamatan'] = split_word[-1]
                elif "Agama" in word:
                    data['agama'] = split_word[-1]
                elif "Status Perkawinan" in word:
                    data['status_perkawinan'] = split_word[-1]
                elif "Pekerjaan" in word:
                    data['pekerjaan'] = split_word[-2]
                elif "Berlaku Hingga" in word:
                    data['berlaku_hingga'] = ' '.join(split_word[-3:-1])
        
        print(data)
        if len(data) > 0:
            con_result.content.controls[1].value = data.get('provinsi', '')
            con_result.content.controls[2].value = data.get('kabupaten', '')
            con_result.content.controls[3].value = data.get('nik', '')
            con_result.content.controls[4].value = data.get('name', '')
            con_result.content.controls[5].value = data.get('jenis_kelamin', '')
            con_result.content.controls[6].value = data.get('gol_darah', '')
            con_result.content.controls[7].value = data.get('alamat', '')
            con_result.content.controls[8].value = data.get('kecamatan', '')
            con_result.content.controls[9].value = data.get('agama', '')
            con_result.content.controls[10].value = data.get('status_perkawinan', '')
            con_result.content.controls[11].value = data.get('pekerjaan', '')
            con_result.content.controls[12].value = data.get('berlaku_hingga', '')
            page.snack_bar = SnackBar(
                Text("Succès de l'extraction des données du carte", size=30), bgcolor="green"
            )
            page.snack_bar.open = True

        # Extraction de la photo
        x_photo, y_photo, largeur_photo, hauteur_photo = 728, 110, 238, 300  # Coordonnées de la région de la photo
        photo = img[y_photo:y_photo+hauteur_photo, x_photo:x_photo+largeur_photo]
        cv2.imwrite("photo_extraite1.png", photo)  # Enregistrer la photo extraite localement
        print("Photo extraite enregistrée avec succès.")

        page.update()

    page.add(Column([
        inputKtp,
        ElevatedButton("Process file", on_click=processfile),
        con_result,
    ]))

app(target=main)