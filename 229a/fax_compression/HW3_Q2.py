import pandas as pd
import numpy as np
from PIL import Image
import os
dir = os.path.dirname(os.path.abspath(__file__))


class ModifiedHuffmanEncoder:
    def __init__(self, terminating_codes_path, makeup_codes_path):
        self.codes = self.get_codes(
            terminating_codes_path, makeup_codes_path)

    def get_codes(self, term_path, makeup_path):
        # build table[color][length] = code
        try:
            df_term = pd.read_csv(term_path, dtype={'CodeWord': str})
            df_makeup = pd.read_csv(makeup_path, dtype={'CodeWord': str})
        except FileNotFoundError as e:
            print(f"Error loading code tables: {e}")
            raise
        df = pd.concat([df_term, df_makeup])
        codes = {0: {}, 1: {}}
        for (l1, l2), group in df.groupby(['RunLength', 'Color']):
            length = int(l1)
            color = 0 if l2 == "Black" else 1
            code = group['CodeWord'].iloc[0]
            codes[color][length] = code
        return codes

    def get_runs_for_bitmap(self, image_bitmap: np.ndarray):
        # pairs of {color, length}
        # force EOL
        runs = [[-1, -1]]
        # iterate over rows
        for row in image_bitmap:
            runs.append([1, 0])
            target_color = 1
            # iterate over pixels
            for color in row:
                color = int(color)
                if color == target_color:
                    # update run length
                    runs[-1][1] += 1
                else:
                    # create new run
                    target_color = 1-target_color
                    runs.append([target_color, 1])
            # force EOL
            runs.append([-1, -1])
        return runs

    def encode_run(self, color, length):
        EOL = "000000000001"
        # handle EOL
        if length == -1:
            return EOL
        # handle bad inputs
        if color not in [0, 1]:
            raise ValueError(
                f"Color {color} is not 0 or 1")
        if length > 1728 + 63 or length < 0:
            raise ValueError(
                f"Run length {length} exceeds maximum of 1728 + 63")
        # handle make + term
        term = length % 64
        if length < 64:
            return self.codes[color][term]
        else:
            make = length - term
            return self.codes[color][make] + self.codes[color][term]

    def encode_image(self, image_bitmap):
        full_bitstream = ""
        runs = self.get_runs_for_bitmap(image_bitmap)
        # print("len runs", len(runs))
        for color, length in runs:
            full_bitstream += self.encode_run(color, length)
        return full_bitstream


class ModifiedHuffmanDecoder:
    def __init__(self, terminating_codes_path, makeup_codes_path):
        self.codes = self.get_codes(
            terminating_codes_path, makeup_codes_path)

    def get_codes(self, term_path, makeup_path):
        # build table[color][code] = length
        try:
            df_term = pd.read_csv(term_path, dtype={'CodeWord': str})
            df_makeup = pd.read_csv(makeup_path, dtype={'CodeWord': str})
        except FileNotFoundError as e:
            print(f"Error loading code tables: {e}")
            raise
        df = pd.concat([df_term, df_makeup])
        codes = {0: {}, 1: {}}
        for (l1, l2), group in df.groupby(['RunLength', 'Color']):
            length = int(l1)
            color = 0 if l2 == "Black" else 1
            code = group['CodeWord'].iloc[0]
            codes[color][code] = length
        return codes

    def decode_image(self, bitstream):
        """
        Decodes a bitstream into a bitmap image.

        Args:
            bitstream (str): compressed bitstream.

        Returns:
            np.array: decoded image as a 2D NumPy array.
        """
        EOL = "000000000001"
        rows = []
        code = ""
        row = []
        target_color = 1
        # iterate over each bit
        for bit in bitstream:
            code += bit
            # handle EOL
            if code == EOL:
                rows.append(row)
                code = ""
                row = []
                target_color = 1
                continue
            # handle code
            if code in self.codes[target_color]:
                length = self.codes[target_color][code]
                row.extend([target_color]*length)
                code = ""
                # terminating code
                if length <= 63:
                    target_color = 1-target_color
        # remove first line which is always empty
        rows = rows[1:]
        return np.array(rows, dtype=np.uint8)


def save_bit_array_to_png(bit_array: np.ndarray, output_path: str) -> None:
    arr = np.asarray(bit_array, dtype=np.uint8)
    if arr.ndim != 2:
        raise ValueError("bit_array must be a 2-D array")
    # Convert 0/1 to 0/255 and create an 8-bit image, then convert to 1-bit for correct display.
    img = Image.fromarray(arr * 255, mode='L').convert('1')
    img.save(output_path)


def load_png_to_bit_array(image_path: str) -> np.ndarray:
    img = Image.open(image_path)
    bw_img = img.convert('1')
    bool_array = np.array(bw_img)
    bit_array = bool_array.astype(np.uint8)
    return bit_array


def save_bitstring_to_txt(bitstring: str, txt_path: str) -> None:
    if any(c not in ('0', '1') for c in bitstring):
        raise ValueError("bitstring must contain only '0' and '1'.")
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(bitstring)


def load_txt_to_bitstring(txt_path: str) -> str:
    with open(txt_path, 'r', encoding='utf-8-sig') as f:
        data = f.read()
    bitstring = ''.join(data.split())
    if any(c not in ('0', '1') for c in bitstring):
        bad = sorted(set(c for c in bitstring if c not in ('0', '1')))
        raise ValueError(f"Input contains non-binary characters: {bad}")
    return bitstring


if __name__ == '__main__':
    TERMINATING_CODES_PATH = os.path.join(dir, "T4-terminating-codes.csv")
    MAKEUP_CODES_PATH = os.path.join(dir, "T4-makeup-codes.csv")
    encoder = ModifiedHuffmanEncoder(TERMINATING_CODES_PATH, MAKEUP_CODES_PATH)
    decoder = ModifiedHuffmanDecoder(TERMINATING_CODES_PATH, MAKEUP_CODES_PATH)

    # Decode fax
    if True:
        FAX_PATH = os.path.join(dir, "fax1.txt")
        bitstring = load_txt_to_bitstring(FAX_PATH)
        print("bitstring length:", len(bitstring))
        bit_array = decoder.decode_image(bitstring)
        save_bit_array_to_png(bit_array, os.path.join(dir, "fax1.png"))

    # Encode images
    if True:
        IMAGE_FILES = ["img1.png", "img2.png", "img3.png", "fax1.png"]
        print("image", "|", "compressed", "|", "png")
        for file in IMAGE_FILES:
            img_path = os.path.join(dir, file)
            bit_array = load_png_to_bit_array(img_path)
            txt = encoder.encode_image(bit_array)
            save_bitstring_to_txt(txt, os.path.join(dir, file+".txt"))
            print(file, "|", len(txt), "|", os.path.getsize(img_path))

    # Testing
    if True:
        IN_PATH = os.path.join(dir, "img1.png")
        TMP_PATH = os.path.join(dir, "tmp.txt")
        OUT_PATH = os.path.join(dir, "img1_ed.png")

        bit_array = load_png_to_bit_array(IN_PATH)
        print("bit array shape", bit_array.shape)
        bitstream = encoder.encode_image(bit_array)
        print("len bitstream", len(bitstream))
        save_bitstring_to_txt(bitstream, TMP_PATH)

        bitstring = load_txt_to_bitstring(TMP_PATH)
        print("len bitstring", len(bitstring))
        bit_array_ed = decoder.decode_image(bitstring)
        print("bit array ed shape", bit_array_ed.shape)
        save_bit_array_to_png(bit_array_ed, OUT_PATH)
