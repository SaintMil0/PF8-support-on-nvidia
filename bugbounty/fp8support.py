import numpy as np

class FP8_E4M3:
    def __init__(self, value):
        self.value = self.E4M3_to_fp8(value)

    def E4M3_to_fp8(self, value):
        # Convert a floating-point number to E4M3 FP8 format
        # Implement conversion logic here
        # Note: This is a simplified placeholder
        if value == 0:
            return 0x00
        sign = 0 if value > 0 else 1
        value = abs(value)
        exponent = min(max(int(np.log2(value)) + 7, 0), 15)
        mantissa = int((value / (2 ** (exponent - 7))) * 8) & 0x7
        return (sign << 7) | (exponent << 3) | mantissa

    def to_float(self):
        # Convert an E4M3 FP8 number back to a standard floating-point number
        # Implement conversion logic here
        # Note: This is a simplified placeholder
        sign = (self.value >> 7) & 0x1
        exponent = (self.value >> 3) & 0xF
        mantissa = self.value & 0x7
        value = (mantissa / 8.0) * (2 ** (exponent - 7))
        return -value if sign else value

    def __add__(self, other):
        result = self.to_float() + other.to_float()
        return FP8_E4M3(result)

    def __sub__(self, other):
        result = self.to_float() - other.to_float()
        return FP8_E4M3(result)

    def __mul__(self, other):
        result = self.to_float() * other.to_float()
        return FP8_E4M3(result)

    def __truediv__(self, other):
        result = self.to_float() / other.to_float()
        return FP8_E4M3(result)
      

class FP8_E5M2:
    def __init__(self, value):
        self.value = self.E5M2_to_fp8(value)

    def E5M2_to_fp8(self, value):
        # Convert a floating-point number to E5M2 FP8 format
        # Implement conversion logic here
        # Note: This is a simplified placeholder
        if value == 0:
            return 0x00
        sign = 0 if value > 0 else 1
        value = abs(value)
        exponent = min(max(int(np.log2(value)) + 15, 0), 31)
        mantissa = int((value / (2 ** (exponent - 15))) * 4) & 0x3
        return (sign << 7) | (exponent << 2) | mantissa

    def to_float(self):
        # Convert an E5M2 FP8 number back to a standard floating-point number
        # Implement conversion logic here
        # Note: This is a simplified placeholder
        sign = (self.value >> 7) & 0x1
        exponent = (self.value >> 2) & 0x1F
        mantissa = self.value & 0x3
        value = (mantissa / 4.0) * (2 ** (exponent - 15))
        return -value if sign else value

    def __add__(self, other):
        result = self.to_float() + other.to_float()
        return FP8_E5M2(result)

    def __sub__(self, other):
        result = self.to_float() - other.to_float()
        return FP8_E5M2(result)

    def __mul__(self, other):
        result = self.to_float() * other.to_float()
        return FP8_E5M2(result)

    def __truediv__(self, other):
        result = self.to_float() / other.to_float()
        return FP8_E5M2(result)
