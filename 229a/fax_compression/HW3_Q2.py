import pandas as pd
import numpy as np
from PIL import Image


class ModifiedHuffmanEncoder:
    """
    Implements the T.4 Modified Huffman (MH) encoding for a binary image.
    Assumes the input bitmap uses 1 for White and 0 for Black.
    """

    def __init__(self, terminating_codes_path, makeup_codes_path):
        """
        Initializes the encoder by loading the Huffman code tables.

        Args:
            terminating_codes_path (str): Path to the CSV with terminating codes.
            makeup_codes_path (str): Path to the CSV with makeup codes.
        """
        self.codes = self._load_codes(terminating_codes_path, makeup_codes_path)

    def _load_codes(self, term_path, makeup_path):
        """
        Loads Huffman codes from CSV files into a nested dictionary for quick lookup.
        It's crucial to read the 'CodeWord' column as a string to preserve leading zeros.
        """
        try:
            df_term = pd.read_csv(term_path, dtype={'CodeWord': str})
            df_makeup = pd.read_csv(makeup_path, dtype={'CodeWord': str})
        except FileNotFoundError as e:
            print(f"Error loading code tables: {e}")
            print("Please ensure 'terminating codes' and 'makeup codes' are in the same directory.")
            raise
        codes = {}
        #TODO Implement this function
        return codes

    def _get_runs_for_bitmap(self, image_bitmap: np.ndarray):
        """
        Computes runs per row of the bitmap.
        The first expected color is White; if the first pixel is Black, emit a 0-length White run.
        """
        runs = []
        #TODO Implement this function
        return runs

    def _encode_run(self, color, length):
        """
        Encode a single run using (optionally) a makeup codes then a terminating code.
        """
        if length > 1728 + 63:
            raise ValueError(f"Run length {length} exceeds maximum of 1728 + 63.")
        bitstream = ""
        #TODO Implement this function
        return bitstream

    def encode_image(self, image_bitmap):
        """
        Encodes the full bitmap as a single continuous bitstream.
        """
        full_bitstream = ""
        #TODO Implement this function
        return full_bitstream


class ModifiedHuffmanDecoder:
    """
    Decodes a T.4 Modified Huffman (MH) bitstream.
    """

    def __init__(self, terminating_codes_path, makeup_codes_path):
        self.codes = self._build_reverse_lookup(terminating_codes_path, makeup_codes_path)

    def _build_reverse_lookup(self, term_path, makeup_path):
        """Builds inverted dictionaries for mapping CodeWord -> (Type, Length)."""
        df_term = pd.read_csv(term_path, dtype={'CodeWord': str})
        df_makeup = pd.read_csv(makeup_path, dtype={'CodeWord': str})
        codes = {}
        #TODO Implement this function
        return codes

    def decode_image(self, bitstream):
        """
        Decodes a bitstream with EOL markers into a bitmap image.

        Args:
            bitstream (str): The compressed bitstream with EOL markers.

        Returns:
            np.array: The decoded image as a 2D NumPy array.
        """
        EOL = "000000000001"
        rows = []
        #TODO Implement this function
        return np.array(rows, dtype=np.uint8)

############################################################
# --- Utility Functions for Image and Bitstring Handling ---
############################################################

def bit_array_to_png(bit_array: np.ndarray, output_path: str):
    """
    Converts a NumPy bit array back into a black and white PNG image.
    Args:
        bit_array: A 2D NumPy array (dtype=uint8) where 0 is black, 1 is white.
        output_path: The path to save the output PNG file.
    """
    arr = np.asarray(bit_array, dtype=np.uint8)
    if arr.ndim != 2:
        raise ValueError("bit_array must be a 2-D array")
    # Convert 0/1 to 0/255 and create an 8-bit image, then convert to 1-bit for correct display.
    img = Image.fromarray(arr * 255, mode='L').convert('1')
    img.save(output_path)

def png_to_bit_array(image_path: str) -> np.ndarray:
    """
    Opens a PNG image and converts it into a NumPy bit array.

    Args:
        image_path: The file path to the PNG image.

    Returns:
        A 2D NumPy array with dtype=uint8, where 0 represents
        black and 1 represents white.
    """
    img = Image.open(image_path)
    bw_img = img.convert('1')
    bool_array = np.array(bw_img)
    bit_array = bool_array.astype(np.uint8)
    return bit_array

def save_bitstring_as_txt(bitstring: str, file_path: str) -> int:
    if any(c not in ('0', '1') for c in bitstring):
        raise ValueError("bitstring must contain only '0' and '1'.")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(bitstring)
    return len(bitstring)

def load_bitstring_from_txt(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        data = f.read()
    bitstring = ''.join(data.split())
    if any(c not in ('0', '1') for c in bitstring):
        bad = sorted(set(c for c in bitstring if c not in ('0', '1')))
        raise ValueError(f"Input contains non-binary characters: {bad}")
    return bitstring

if __name__ == '__main__':
    TERMINATING_CODES_PATH = "T4-terminating-codes.csv"
    MAKEUP_CODES_PATH = "T4-makeup-codes.csv"
    encoder = ModifiedHuffmanEncoder(TERMINATING_CODES_PATH, MAKEUP_CODES_PATH)
    decoder = ModifiedHuffmanDecoder(TERMINATING_CODES_PATH, MAKEUP_CODES_PATH)


