import base64

def flag_generation():
    
    parts = [
        "Zm", "xh", "Z3", "s1", "ZT", "Nr", "Xz", "Ru", "ZF", "95",
        "MH", "Vf", "c2", "g0", "bG", "xf", "Zj", "Fu", "ZH", "0="
    ]
    
   
    enc_flag = ''.join(parts)
   
    flag_bytes = base64.b64decode(enc_flag)
    
    final_flag = ''.join([chr(b) for b in flag_bytes])
    
    return final_flag

# Generate and print the final flag
print(flag_generation())
