from cryptographyFramework import *

initializeWrite()
user = "Rafael"
password = "2525"
encryptedText = encryptMessage(user, password, "Ce viu a previa da musica nova do tue?")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Pitbull de madame")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Luis rei do chess")
saveNewLine(encryptedText)

