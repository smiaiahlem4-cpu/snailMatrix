# generate_snail_matrix.py

def generate_spiral(n):
    matrix = [[0]*n for _ in range(n)]
    
    left, right = 0, n-1
    top, bottom = 0, n-1
    num = 1
    
    while left <= right and top <= bottom:
        
        # Top row
        for i in range(left, right+1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        # Right column
        for i in range(top, bottom+1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        # Bottom row
        if top <= bottom:
            for i in range(right, left-1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
        
        # Left column
        if left <= right:
            for i in range(bottom, top-1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            
    return matrix


if __name__ == "__main__":
    n = int(input("n :"))
    result = generate_spiral(n)
    
    # Print full matrix as a 2D list
    print(result)
