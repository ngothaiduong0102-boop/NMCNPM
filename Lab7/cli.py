import argparse
from app import verify_pin, withdraw

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--card', required=True)
    p.add_argument('--pin', required=True)
    p.add_argument('--amount', required=True, type=int)
    args = p.parse_args()

    if not verify_pin(args.card, args.pin):
        print('[AUTH] FAIL – invalid card or PIN')
        return

    print(f'[AUTH] OK – card {args.card}')
    try:
        nb = withdraw(args.card, args.amount)
        print(f'[WITHDRAW] Debited {args.amount}. New balance = {nb}')
        print('[SUCCESS] Transaction logged.')
    except Exception as e:
        print('[ERROR]', e)

if __name__ == '__main__':
    main()
