#!/usr/bin/python3
import hashlib
import os
import random
import binascii
import ecdsa
import base58
#import datetime
import webbrowser
from json import (load as jsonload, dump as jsondump)
from os import path
import json
import hmac
import base64

#start_time = datetime.datetime.now()

def bip(num):
    with open('BIP0039.txt', 'r') as f:
        words = f.read().split()
        for word in words:
            sent = [random.choice(words)
                for word in range(int(num))]
            return ' '.join(sent)

def passw(filename):
    try:
        with open(filename, 'r') as f:
            words = f.read().split()
            for word in words:
                sent = [random.choice(words)
                        for word in range(int(1))]
                return ' '.join(sent)
    except FileNotFoundError:
        pass
    except TypeError:
        pass


def hmac512(mnemonic, passphrase):
    d = mnemonic+' '+ passphrase
    return d
    
def master(hmacsha512):
    return hashlib.sha256(hmacsha512.encode("utf-8")).hexdigest().upper()


def pubkey(masterkey):
    privatekey = binascii.unhexlify(masterkey)
    s = ecdsa.SigningKey.from_string(privatekey, curve = ecdsa.SECP256k1)
    return '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')

def addr(public_key):
    output = []; alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    var = hashlib.new('ripemd160')
    var.update(hashlib.sha256(binascii.unhexlify(public_key.encode())).digest())
    var = '00' + var.hexdigest() + hashlib.sha256(hashlib.sha256(binascii.unhexlify(('00' + var.hexdigest()).encode())).digest()).hexdigest()[0:8]
    count = [char != '0' for char in var].index(True) // 2
    n = int(var, 16)
    while n > 0:
        n, remainder = divmod(n, 58)
        output.append(alphabet[remainder])
    for i in range(count): output.append(alphabet[0])
    return ''.join(output[::-1])

def wif(masterkey):
    var80 = "80"+masterkey
    var = hashlib.sha256(binascii.unhexlify(hashlib.sha256(binascii.unhexlify(var80)).hexdigest())).hexdigest()
    return str(base58.b58encode(binascii.unhexlify(str(var80) + str(var[0:8]))), 'utf-8')

def database(address):
    with open("data-base", "r") as m:
        add = m.read().split()
        for ad in add:
            continue
        if address in add:
            data = open("Win.txt","a")
            data.write("Bingo " + str(sect)+"\n" +str(address)+"\n"+str(WIF)+"\n"+"\n")
            data.close()
            return 'Bingo'
        else:
            i = 'No luck'
            return i

    
def main():
    print("Most common- 3, 6, 9, 12, 15, 18, 21, 24")
    num = input("Passphrase Word Count? > ")
    #num = int(num)
    generator = True
    while True:
        if generator:
            mnemonic = bip(num)
            masterkey = master(mnemonic)
            public_key = pubkey(masterkey)
            address = addr(public_key)
            WIF = wif(masterkey)
            data_base = database(address)
            print('mnemonic:   '+str(mnemonic)+'\n'+
                  'private key:                           '+str(masterkey)+'\n'+
                  'address:                                 '+str(address)+'\n'+
                  'wif:                                        '+str(WIF)+"\n"+
                  'address with balance:           '+str(data_base)+'\n\n')
            
main()

