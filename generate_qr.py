import segno

qr = segno.make("TRIPHALA_KWATH")

qr.save(
    "triphala_qr.png",
    scale=20
)

print("QR Generated")