list_1_most_danger = "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"

list_2_danger = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="




import base64

class Encryption:
    @staticmethod
    def decrypt(coded : str)->str:
        decoded_bytes = base64.b64decode(coded)
        return decoded_bytes.decode('utf-8')
    


words_list = Encryption.decrypt(list_1_most_danger).split(",")
words_list2 = Encryption.decrypt(list_2_danger).split(",")

print(words_list)

print(words_list2)



