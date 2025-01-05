import requests
import hashlib
import sys

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char   # first 5 hash chars (hex)
    response = requests.get(url)
    return response

def get_password_leaks_count(hashes, hash_to_check):
    hashes= (line.split(":") for line in hashes.text.splitlines())
    for h,count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1_password= hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5_hash, tail_hash = sha1_password[:5], sha1_password[5:]
    response_api= request_api_data(first_5_hash)
    return get_password_leaks_count(response_api,tail_hash)

def main(args):
    for password in args:
        pwned_count= pwned_api_check(password)
        if pwned_count:
            print(f'\"{password}\" has been pwned {pwned_count} times. Time to change your password.')
        else:
            print(f'{password} has not found. Carry on!')
    return 'done!!!\n\n'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))