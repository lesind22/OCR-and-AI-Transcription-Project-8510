# Contrast and Enhancement.py 

#!/usr/bin/env python3
"""
Demo: Contrast Enhancement for Historical Documents Cover Page
=============================================================

This script applies several contrast enhancement techniques to a single image:
- Histogram Equalization (Global)
- CLAHE (Adaptive)
- Gamma Correction
- Unsharp Masking

Usage:
    python Contrast and Enhancement.py "/path/to/image.png"
"""

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def check_dependencies():
    """Check if required packages are installed."""
    try:
        import cv2
        import numpy
        import matplotlib
    except ImportError as e:
        print(f"Error: {e}. Please install required libraries: pip install opencv-python numpy matplotlib")
        sys.exit(1)

def load_image(image_path):
    """Load and display image information."""
    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError(f"Could not load image: {image_path}")
    print(f"Loaded: {Path(image_path).name}")
    print(f"Image shape: {image.shape}")
    return image

def convert_to_grayscale(image):
    """Convert BGR image to grayscale."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("✓ Converted to grayscale")
    return gray

def apply_histogram_equalization(image):
    """Apply global histogram equalization."""
    equalized = cv2.equalizeHist(image)
    print("✓ Applied global histogram equalization")
    return equalized

def apply_clahe(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    """Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)."""
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    clahe_image = clahe.apply(image)
    print(f"✓ Applied CLAHE (clip_limit={clip_limit}, tile_size={tile_grid_size})")
    return clahe_image

def apply_gamma_correction(image, gamma=1.2):
    """Apply gamma correction."""
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in range(256)]).astype("uint8")
    gamma_corrected = cv2.LUT(image, table)
    print(f"✓ Applied gamma correction (γ={gamma})")
    return gamma_corrected

def apply_unsharp_masking(image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    """Apply unsharp masking to enhance text sharpness."""
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.abs(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    print(f"✓ Applied unsharp masking (amount={amount}, σ={sigma})")
    return sharpened

def save_image(image, path):
    cv2.imwrite(str(path), image)
    print(f"✓ Saved: {path}")

def show_images(images, titles):
    n = len(images)
    plt.figure(figsize=(4*n, 6))
    for i, (img, title) in enumerate(zip(images, titles)):
        plt.subplot(1, n, i+1)
        plt.imshow(img, cmap='gray')
        plt.title(title)
        plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    check_dependencies()
    if len(sys.argv) != 2:
        print("Usage: python contrast_enhancement.py /path/to/image.png")
        sys.exit(1)

    image_path = sys.argv[1]
    if not Path(image_path).is_file():
        print(f"Error: The file '{image_path}' does not exist.")
        sys.exit(1)

    # Load and process the image
    image = load_image(image_path)
    gray = convert_to_grayscale(image)

    # Apply contrast enhancement techniques
    hist_eq = apply_histogram_equalization(gray)
    clahe = apply_clahe(gray)
    gamma = apply_gamma_correction(gray, gamma=1.2)
    unsharp = apply_unsharp_masking(gray)

    # Save outputs
    out_dir = Path("contrast_results")
    out_dir.mkdir(exist_ok=True)
    save_image(hist_eq, out_dir / "histogram_equalized.png")
    save_image(clahe, out_dir / "clahe.png")
    save_image(gamma, out_dir / "gamma_corrected.png")
    save_image(unsharp, out_dir / "unsharp_masked.png")

    # Show comparison
    show_images(
        [gray, hist_eq, clahe, gamma, unsharp],
        ["Original Grayscale", "Histogram Equalization", "CLAHE", "Gamma Correction", "Unsharp Masking"]
    )