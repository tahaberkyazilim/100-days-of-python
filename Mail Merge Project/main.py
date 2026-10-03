with open("Input/Letters/starting_letter.txt", mode = "r") as letter:
    letter_before = letter.read()
    # Bu with satırı işlem yapacağımız mektubu okuyup hafızaya kaydediyor "letter_before" diye

with open("Input/Names/invited_names.txt", mode = "r") as names_file:
    # Bu with satırı davetli kişileri okuyor
    for names in names_file.readlines():
        #Bu for satırı readlines kullanarak kaç kişi varsa o kadar döngüde isimleri temizleyip (strip ile) name diye kaydediyor
        name = names.strip()
        updated_file = letter_before.replace("[name]", name)
        # Bu satır yeni mektupları hazırlıyor
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode = "w") as ready_file:    
            ready_file.write(updated_file)
            # Bu with de hazır dosyaları istediğimiz konuma yazdırıyor, 8 mektup olacak çünkü readlines 8 değer aldı


