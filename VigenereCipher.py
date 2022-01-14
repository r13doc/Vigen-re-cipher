class VigenereCipher():
    
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

                
    def encode(self, text):
        # shift to a character with the corresponding index 
        # of the key in the alphabet
        key = (self.key * (len(text)//len(self.key) + 1))[:len(text)]
        
        # iterate variables check if they place in alphabet or not
        zipped = zip([self.alphabet.index(i) if i in self.alphabet
                      else i for i in text],
                    [self.alphabet.index(j) for j in key])
        # use algebraically ci = (pi + ki) 
        summ = [i+j if type(i) is int else i
                for (i,j) in zipped]
        # mod len from alphabet
        key_len = [(j % len(self.alphabet)) if type(j) is int else j
                  for j in summ]
        # convert index to alphabet
        enc = ''.join([self.alphabet[i] if type(i) is int
                      else i for i in key_len])
        return enc
        
        
    
    def decode(self, text):
        # shift to a character with the corresponding index 
        # of the key in the alphabet
        key = (self.key * (len(text)//len(self.key) + 1))[:len(text)]
        
        # iterate variables
        zipped = zip([self.alphabet.index(i) if i in self.alphabet 
                      else i for i in text],
                     [self.alphabet.index(j) for j in key]) 
        # use algebraically pi = (ci - ki)
        summ = [i-j if type(i) is int else i
                for (i,j) in zipped]
        # mod len from alphabet 
        key_len = [(j % len(self.alphabet)) if type(j) is int else j
                   for j in summ]
        # convert index to alphabet
        dec = ''.join([self.alphabet[i] if type(i) is int else i
                      for i in key_len])
        return dec


abc = (input('Enter alphabet for Vigenère cipher:'))
key = (input('Enter key for encoding, use same type sting as alphabet:'))
c = VigenereCipher(key, abc)
print('Remember all variables should be the same alphabets type and height characters.')
text = str(input('Enter word for encode:'))
enc = c.encode(text)
dec = c.decode(enc)
print('Encoded word from', text, 'is', enc)
print('Decoded word from', enc, 'is', dec)
