import os

def sf(fp, cs):
    fn, fe = os.path.splitext(fp)
    fe = fe.lstrip('.')

    od = f"{fn}_TYSM"
    os.makedirs(od, exist_ok=True)

    try:
        with open(fp, 'rb') as f:
            c = f.read()

        cb = 1024 * cs
        ts = len(c)
        nc = (ts // cb) + (1 if ts % cb else 0)

        h = f'<tysm>"{fe}","{nc}"</tysm>\n'.encode('utf-8')

        for i in range(nc):
            s = i * cb
            e = min(s + cb, ts)
            cd = c[s:e]

            cn = os.path.join(od, f"{i}.tysm")
            with open(cn, 'wb') as cf:
                if i == 0:
                    cf.write(h)
                cf.write(cd)

        print(f"File split into {nc} chunks. Chunks are saved in '{od}'.")

    except FileNotFoundError:
        print(f"Error: File '{fp}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

fp = "testing.txt"
cs = 10
sf(fp, cs)
