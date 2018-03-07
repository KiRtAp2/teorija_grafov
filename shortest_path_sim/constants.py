"""Ta modul shranjuje konstante, ki jih program hrani med izvanjanjem"""


WWIDTH = 500  # širina okna
WHEIGHT = 500  # višina okna

BORDER_WIDTH = 20
BORDER_HEIGHT = 20

NUM_OF_SQUARES = (50, 50)  # število polj v vsaki smeri
ALL_SQUARES = NUM_OF_SQUARES[0] * NUM_OF_SQUARES[1]  # število vseh polj
SQUARE_WIDTH = int((WWIDTH - 2 * BORDER_WIDTH) / NUM_OF_SQUARES[0])
SQUARE_HEIGHT = int((WHEIGHT - 2 * BORDER_HEIGHT) / NUM_OF_SQUARES[1])
SQUARE_FIELD_WIDTH = NUM_OF_SQUARES[0] * SQUARE_WIDTH
SQUARE_FIELD_HEIGHT = NUM_OF_SQUARES[1] * SQUARE_HEIGHT

SLEEP_DELAY = 0
