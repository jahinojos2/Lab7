#Jaime Hinojos
#80590883
#Lab7


def edit_distance(word1, word2):

    sim_matrix = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
    #Creates 2D array with the size of word1 x word2

    for i in range(len(word1)+1):#fills first column
        sim_matrix[0][i] = i


    for i in range(len(word2)+1):#fills second column
        sim_matrix[i][0] = i

    for i in range(len(word2)):#row index

        for j in range(len(word1)): #column index

            if word1[j] == word2[i]: #if word is the same it grabs the diagonal value and puts it in the matrix
                sim_matrix[i+1][j+1] = sim_matrix[i][j]

            else: #else grab the smallest value of the lest values next to the matrix index its currently in
                sim_matrix[i+1][j+1] = min(sim_matrix[i][j], sim_matrix[i][j+1], sim_matrix[i+1][j]) + 1


    for i in range(len(sim_matrix)):#prints the matrix
        print(sim_matrix[i])

    print #prints the number of operations to change one word to another
    print("number of operations to match "+word1+" and "+word2+" is:"+ str(sim_matrix[len(word2)][len(word1)]))

def main():
    word1 = "happy"
    word2 = "healthy"

    edit_distance(word1, word2)

main()