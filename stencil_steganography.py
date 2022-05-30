from PIL import Image


def main():
    matrix = Image.open('images/word_matrix.png')
    mask = Image.open('images/mask.png')

    dimensions = find_size(matrix)
    big_mask = make_big(dimensions, mask)
    make_clear(big_mask)
    overlay(matrix, big_mask)

    matrix.save("images/decoded.png", format="png")


def find_size(matrix):
    return matrix.size


def make_big(dimensions, mask):
    return mask.resize((dimensions[0], dimensions[1]))


def make_clear(mask):
    return mask.putalpha(100)


def overlay(matrix, mask):
    return matrix.paste(mask, box=(0, 0), mask=mask)


if __name__ == '__main__':
    main()
