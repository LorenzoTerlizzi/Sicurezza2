# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# Per iniziare generiamo una coppia di chiavi e le stampiamo
# Generating RSA Key Pair
# Una volta stampate, non serve più
key_pair = RSA.generate(2048)
print(key_pair.export_key())
public_key = key_pair.publickey()
print(public_key.export_key())
exit(0)
# sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAtcjn5ua+pVdIHQaTCQinofFb7sHgDFmtamBlIAfofMyaH1tk\n5l3x5KHZhRatBiygDlSL8ts5DfUB1yrgNFYSr4h8GuHywNr9DF1tpgt3GwtXuOIn\nF8gbrxCDBCOiPqqwzPa0lK+NIlQxxibhf8jCzUjZ8IPATXeW619TDWcSNxH5ER7z\n+MRM0gq9oYVhneKtN7XbHjv9ne7OK5aS8gCmoHfWkx7AnMM3Ns2P44om8gDH/SPO\nmh1VSpfK1wqwyTHfKZDtgq84ChgqxfhzB09SCmnewOQJsY0yIks69AElftKhfOSY\nZw4MY5XOzm+sMapNpRCL8RUYzIk6J+bx0Y8QHwIDAQABAoIBAAC98rBfFb0gB5PS\nwIvjZKfFD+6ADRWP0iTigtcoIRtNTH2/RkCodoHL5VLlPkyNpxOX5cBWg7uaWekS\nbDradRYRVQxZCsAdxLWltfpdBp3uJGwFREqVDwPeaeJ88L8XvEQB58fJlaZjuJZJ\n91apr53d48HXD9RhHhUU3QZresgNwXM6WjScU98JnQiuADUxlRZoFKphMuUV2JPU\n6MCYOBbkt9tkk7rS67VeWxbOOTXLFyUtH0lba9XKf44CbhjIPqQweZH1nDPg/kjA\nitgzSXx+xUD3OJNc5SBBwGr+6Ur+xUf2RoHWjekMEYQagiSwjWh333IaknqPDYG6\nLSvefTUCgYEAvQUuyUFTTjh7SuwkkDKFFEsnD8Y7pT7aicOdlNpP6NTFWN2K/sVs\n4EOLfUx+d7rCS08MGGCIGkWMYvG7z3eu8YzbKnL6RaBnkJ4KQcf5VfNDTSHiL+2y\nKnVqMe7rCYps3AK0PgLChSCVoVgZatWR0GOoqiaLHkQWTjx3PGY0l8sCgYEA9jNd\nVGHB4Q/EA+S3iPqjqx4pSEV4L+ezdBYpPbrjSWlPM29M0jSAasVCl3W6zVhzqOz/\n0nn7clK4xazb7/LrULnJnF2Hz/iTQeBSG3uAZJzi3IUxLtvPE/iZkh0szRdEfXqd\nAM2B1xMrqTr6n+oGNmrEUNOdCjLENGJooMzQln0CgYB3c3cFqErE+9yulFzm44ZG\nNNgSl+vJmdbxiLVlBDHLqeqtJhRYvNr5PrZAEL87WsK+ZM33+ckJETqOrMVLbw8X\nhzRZtx+CMMRCGB3TRFTFhF3buLYAI+6b9meN9raB6QCyaOMO7R+Qke79b3dglGb5\nkoFcRc9U6SJPfta7TLuf0QKBgBa0jfrmORckeRNS2IpNcyKo2W3M2lSwraAbGxqS\nTbvLdn5r2U3Zga5XGtkVBnFBowkFMmKa1VGpx1iTpITwhjsfpzRAe/H2Hr6IjYnz\nTdf5kAJ+VhbYNrTEzITpI+SWLL7Vu/0C9uJ65h/pTIvK7V+/YPODUIxMOkQKf1O1\nD9eRAoGAQgfFWjn0CYxVcI56MWiQ3HNWqR2lKFujgoNPvbYUWHqGH1oEv065B+B6\nOQ0AfBgH5fXiaXN7edJ6eMyf2Q1ZlIUh62Dj9MPQEoT33TuAocHbiyI1W28asX+I\n83MX1DQ28atCDEeRm2RNfMUGPhTYYyd504y6oozur9b1HLdBhcM=\n-----END RSA PRIVATE KEY-----"
# sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtcjn5ua+pVdIHQaTCQin\nofFb7sHgDFmtamBlIAfofMyaH1tk5l3x5KHZhRatBiygDlSL8ts5DfUB1yrgNFYS\nr4h8GuHywNr9DF1tpgt3GwtXuOInF8gbrxCDBCOiPqqwzPa0lK+NIlQxxibhf8jC\nzUjZ8IPATXeW619TDWcSNxH5ER7z+MRM0gq9oYVhneKtN7XbHjv9ne7OK5aS8gCm\noHfWkx7AnMM3Ns2P44om8gDH/SPOmh1VSpfK1wqwyTHfKZDtgq84ChgqxfhzB09S\nCmnewOQJsY0yIks69AElftKhfOSYZw4MY5XOzm+sMapNpRCL8RUYzIk6J+bx0Y8Q\nHwIDAQAB\n-----END PUBLIC KEY-----"

sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAtcjn5ua+pVdIHQaTCQinofFb7sHgDFmtamBlIAfofMyaH1tk\n5l3x5KHZhRatBiygDlSL8ts5DfUB1yrgNFYSr4h8GuHywNr9DF1tpgt3GwtXuOIn\nF8gbrxCDBCOiPqqwzPa0lK+NIlQxxibhf8jCzUjZ8IPATXeW619TDWcSNxH5ER7z\n+MRM0gq9oYVhneKtN7XbHjv9ne7OK5aS8gCmoHfWkx7AnMM3Ns2P44om8gDH/SPO\nmh1VSpfK1wqwyTHfKZDtgq84ChgqxfhzB09SCmnewOQJsY0yIks69AElftKhfOSY\nZw4MY5XOzm+sMapNpRCL8RUYzIk6J+bx0Y8QHwIDAQABAoIBAAC98rBfFb0gB5PS\nwIvjZKfFD+6ADRWP0iTigtcoIRtNTH2/RkCodoHL5VLlPkyNpxOX5cBWg7uaWekS\nbDradRYRVQxZCsAdxLWltfpdBp3uJGwFREqVDwPeaeJ88L8XvEQB58fJlaZjuJZJ\n91apr53d48HXD9RhHhUU3QZresgNwXM6WjScU98JnQiuADUxlRZoFKphMuUV2JPU\n6MCYOBbkt9tkk7rS67VeWxbOOTXLFyUtH0lba9XKf44CbhjIPqQweZH1nDPg/kjA\nitgzSXx+xUD3OJNc5SBBwGr+6Ur+xUf2RoHWjekMEYQagiSwjWh333IaknqPDYG6\nLSvefTUCgYEAvQUuyUFTTjh7SuwkkDKFFEsnD8Y7pT7aicOdlNpP6NTFWN2K/sVs\n4EOLfUx+d7rCS08MGGCIGkWMYvG7z3eu8YzbKnL6RaBnkJ4KQcf5VfNDTSHiL+2y\nKnVqMe7rCYps3AK0PgLChSCVoVgZatWR0GOoqiaLHkQWTjx3PGY0l8sCgYEA9jNd\nVGHB4Q/EA+S3iPqjqx4pSEV4L+ezdBYpPbrjSWlPM29M0jSAasVCl3W6zVhzqOz/\n0nn7clK4xazb7/LrULnJnF2Hz/iTQeBSG3uAZJzi3IUxLtvPE/iZkh0szRdEfXqd\nAM2B1xMrqTr6n+oGNmrEUNOdCjLENGJooMzQln0CgYB3c3cFqErE+9yulFzm44ZG\nNNgSl+vJmdbxiLVlBDHLqeqtJhRYvNr5PrZAEL87WsK+ZM33+ckJETqOrMVLbw8X\nhzRZtx+CMMRCGB3TRFTFhF3buLYAI+6b9meN9raB6QCyaOMO7R+Qke79b3dglGb5\nkoFcRc9U6SJPfta7TLuf0QKBgBa0jfrmORckeRNS2IpNcyKo2W3M2lSwraAbGxqS\nTbvLdn5r2U3Zga5XGtkVBnFBowkFMmKa1VGpx1iTpITwhjsfpzRAe/H2Hr6IjYnz\nTdf5kAJ+VhbYNrTEzITpI+SWLL7Vu/0C9uJ65h/pTIvK7V+/YPODUIxMOkQKf1O1\nD9eRAoGAQgfFWjn0CYxVcI56MWiQ3HNWqR2lKFujgoNPvbYUWHqGH1oEv065B+B6\nOQ0AfBgH5fXiaXN7edJ6eMyf2Q1ZlIUh62Dj9MPQEoT33TuAocHbiyI1W28asX+I\n83MX1DQ28atCDEeRm2RNfMUGPhTYYyd504y6oozur9b1HLdBhcM=\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1lxZu5fo5fyZiBVCc+Hu\n4PpT0tMAMRbw4BlBYaYJHL1ptaDQaSxmc9FfnTyg3oUXE/Lj6FErItCPLD+Ps55Y\nHatM4w4CEJ0XjpVsJ/RF2GBU2Dbk2VgiplX47JUPgYkdYYoqDp/sEczSvHakYzch\n0JWErq6ZEBfiYKgpGP2zzkI/NpzVz4/SiTN7CZdokuvdTc7cZusNcX9cBnEVMTjK\nDALSRJHo7xZzFmssglRUX1j7ebMtvH+JwAjkQ81+WwtilRLRIYAjTRCItHHVFpec\n6lbiWSWtAHpZuBIGOGemqD1yYajGsxjsodosC1K/0pHH+X55cSLIrQ1SkMqCd5Do\nkwIDAQAB\n-----END PUBLIC KEY-----"

# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
# message = "L'attentato è programmato per le ore 19:45 del giorno 01/10/2024"
# encrypted_message = encrypt_message(message, public_key)
# # encrypted_message = "hp0HPD71T+d7kFLuduRCxoSPjvHuskVqWKUaYa1Guq9L0V4eqeqPWhiZ8fM7p+iV2Tx/cUU0uZc9XdjFWKRZ2S+VMZNYB/6T7HiRhuBkifTip5XZ8VGdTFPE3rCD7+kGXJ+PHzJ9iDW02QJuqL9tuxyXCqwHnGX4gagWqSh/IgbEO2u4pAXaBsw8Nc4CUvP3bY8kcG5TT/ZlKv9wm4eJLMKjzzhjWuUTzHf3SqcU6TdK9+CsBo3QJQZP7GqTYfvS5YVUc5VbvjPXcghkAAm0ykz3uYOEQrO60wgbHZLr0yzALCcEAEyhbHF9anYTuTvhnUFJrOujsVU/XUM5JC60kg=="
# # decrypted_message = decrypt_message(encrypted_message, key_pair)

# print("Original Message:", message)
# print("Encrypted Message:", encrypted_message)
# print("Decrypted Message:", decrypted_message)
