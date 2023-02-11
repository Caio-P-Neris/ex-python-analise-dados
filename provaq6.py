def main():
    # seu codigo aqui
    tentativa = 0
    while tentativa < 5:
        n = float(input())
        if n > 198:
            print('Meta atingida')
            tentativa = 10
        else: 
            print('Insuficiente')
            tentativa = tentativa + 1
if __name__ == '__main__':
    main()
