import copy
import webbrowser


def game_of_life(matrix, iterations=5, filename="game_of_life.html"):
    rows = len(matrix)
    cols = len(matrix[0])

    def count_live_neighbors(row, col):
        neighbor_offsets = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        count = 0
        for row_offset, col_offset in neighbor_offsets:
            neighbor_row = row + row_offset
            neighbor_col = col + col_offset
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                count += matrix[neighbor_row][neighbor_col]

        return count

    for _ in range(iterations):
        new_matrix = copy.deepcopy(matrix)
        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_live_neighbors(r, c)
                if matrix[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_matrix[r][c] = 0
                else:
                    if live_neighbors == 3:
                        new_matrix[r][c] = 1
        matrix = new_matrix

    html = "<!DOCTYPE html><html><head><title>Game of Life</title></head><body>"
    html += "<table border='1' cellspacing='0' cellpadding='0'>"
    for r in matrix:
        html += "<tr>"
        for c in r:
            color = "black" if c else "white"
            html += f"<td style='width:20px;height:20px;background-color:{color}'></td>"
        html += "</tr>"
    html += "</table></body></html>"

    with open(filename, "w") as f:
        f.write(html)

    webbrowser.open(filename)

    return matrix


grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

game_of_life(grid)
