import qrcode

# requirements: installer ce package avant execution du code
# pip install qrcode[pil]


def qenerate_qr_code(url):
    """
    Génère un code QR à partir d'une URL et le sauvegarde sous forme d'image.
    """
    # Créer l'objet QRCode
    qr = qrcode.QRCode(
        version=1,  # contrôle la taille du QR code (1 à 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # niveau de correction d'erreur
        box_size=10,  # taille de chaque "case"
        border=4,  # épaisseur de la bordure (en cases)
    )

    # Ajouter l'URL au QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Créer une image à partir du QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Sauvegarder l'image
    img.save("qr_code.png")

    print("Le code QR a été généré et sauvegardé sous le nom 'qr_code.png'")
