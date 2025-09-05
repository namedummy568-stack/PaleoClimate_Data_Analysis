# Updated vegetation index calculation script with advanced logic

def calculate_ndvi(red_band, nir_band):
    # Add a small epsilon to avoid division by zero
    epsilon = 1e-8
    return (nir_band - red_band) / (nir_band + red_band + epsilon)

def calculate_evi(blue_band, red_band, nir_band, L=1, C1=6, C2=7.5, G=2.5):
    return G * ((nir_band - red_band) / (nir_band + C1 * red_band - C2 * blue_band + L))