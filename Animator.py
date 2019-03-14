import BalanceCompressAlgorithm
import CompressRow
import Transpose
import matplotlib.pyplot as plt
from matplotlib import animation
import MakeBoolArray
import Move

def Animator(Array,moves,dim):
    StaticArray = Array
    ArrayDim = dim
    def MakeMove(Array,move):
        print move
        COM = BalanceCompressAlgorithm.CenterOfMass(StaticArray, ArrayDim)
        dim = len(Array)
        arrays = [Array]
        i = 0
        if 1 > 0:
            if len(move) == 2:
                Array = Move.Move(Array,move[0],move[1])
            else:
                if move[0] == 'r':
                    row = int(move[3])
                    RowTotals = BalanceCompressAlgorithm.RowSum(Array,ArrayDim)
                    Array[int(move[3])] = BalanceCompressAlgorithm.CompressRow(COM[1],ArrayDim, RowTotals[int(move[3])])
                if move[0] == 'c':
                    col = int(move[3])
                    Array = Transpose.Transpose(Array,dim)
                    Array = CompressRow.CompressRow(Array,col,COM)
                    Array = Transpose.Transpose(Array,dim)
            arrays.append(Array)
            i += 1
        return arrays

    def update(n):
        if n > 0 and n<len(moves):
            ax.cla()
            print n
            plotArray(Array,n)

    def plotArray(Array,n):
        MakeMove(Array,moves[n])
        i = 0
        j = 0
        x = []
        y = []
        while i<10:
            while j<10:
                if Array[i][j] == True:
                    x.append(i)
                    y.append(j)
                j += 1
            i += 1
            j = 0
        ax.plot(y,x,'ro')
        plt.grid(True)
        plt.autoscale(False)
        plt.ylim(-1,10)
        plt.xlim(-1,10)



    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(1,1,1)
    anim  = animation.FuncAnimation(fig, update,interval = 10)
    plt.show()
