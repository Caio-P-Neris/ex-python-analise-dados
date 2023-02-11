def main():
    # seu codigo aqui
    import pandas as pd
    import numpy as np
    df = pd.read_csv("https://www.dropbox.com/s/cpo4eyqoztwn3nc/fake-classrooms-correl07.csv?dl=1")
    independente = input()
    nx = float(input())

    (a, b) = np.polyfit(x=df[independente], y= df['Nota Final'], deg = 1)

    resposta = a*nx + b

    print('%.2f' % resposta)
if __name__ == '__main__':
    main()
