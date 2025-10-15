from PIL import Image
import os
from matplotlib import pyplot as plt
import numpy as np

dir = os.path.dirname(os.path.abspath(__file__))


def solve(filename):
    imgpath = os.path.join(dir, filename)
    img = Image.open(imgpath).convert('L')
    A = np.asarray(img)
    print(f"Shape: {A.shape}, type: {A.dtype}")
    U, s, Vt = np.linalg.svd(A)
    S = np.zeros(A.shape)
    S[:len(s), :len(s)] = np.diag(s)

    fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(16, 8))
    axs = axs.flatten()

    oplot = axs[0]
    oplot.imshow(A, cmap='gray')
    oplot.set_title('Original image')

    splot = axs[1]
    splot.plot(s, marker='o', linestyle='None')
    splot.set_xlabel('k')
    splot.set_ylabel('kth singular value')
    splot.set_title('Singular values')

    slogplot = axs[2]
    slogplot.plot(s, marker='o', linestyle='None')
    slogplot.set_xlabel('k')
    slogplot.set_ylabel('kth singular value')
    slogplot.set_title('Singular values (log scale)')
    slogplot.set_yscale('log')

    def kapx(k, ax):
        Sk = S[:k, :k]
        Uk = U[:, :k]
        Vtk = Vt[:k, :]
        Ak = Uk@Sk@Vtk
        ax.imshow(Ak, cmap='gray')
        error = pow(np.linalg.norm(A-Ak)/np.linalg.norm(A), 2)
        perc = k/len(s)
        ax.set_xlabel(f"Error: {round(error, 4)}")
        ax.set_title(f"% singular values used: {round(perc, 4)}")
    kapx(30, axs[3])
    kapx(80, axs[4])
    kapx(100, axs[5])
    plt.tight_layout()
    plt.savefig(imgpath+".png")


if __name__ == "__main__":
    solve("img1.png")
    solve("img2.png")
