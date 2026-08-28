def generate(numRows: int):
        if numRows==0:
             return []
        layer = [[1]]
        temp = []
        for loop in range(numRows - 1):
            prev_row = layer[-1]
            new_row = [1]
            for i in range(len(prev_row)-1):
                new_row.append(prev_row[i] + prev_row[i+1])                 
            new_row.append(1)
            layer.append(new_row)
        return layer

generate(4)
print(generate(10))