import io
from typing import Tuple, Optional
from PIL import Image
from fastapi import UploadFile, HTTPException

ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/webp", "image/jpg"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
MAX_DIMENSION = 1024  # Max width/height to resize for fast AI inference

async def process_and_validate_image(file: Optional[UploadFile]) -> Optional[Tuple[Image.Image, bytes, str]]:
    """
    Validates uploaded outfit image, checks MIME type and size,
    and resizes large images using Pillow for efficient Gemini inference.
    Returns: Tuple of (PIL.Image, optimized_bytes, mime_type) or None.
    """
    if not file or not file.filename:
        return None

    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported image type: {file.content_type}. Please upload JPG, PNG, or WEBP."
        )

    content = await file.read()
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"Image size exceeds 10MB limit (uploaded: {len(content) / (1024 * 1024):.1f}MB)."
        )

    try:
        image = Image.open(io.BytesIO(content))
        image.verify()  # Verify image integrity
        # Reopen because verify() closes the stream
        image = Image.open(io.BytesIO(content))
        image = image.convert("RGB")

        # Resize if dimensions exceed MAX_DIMENSION
        if max(image.size) > MAX_DIMENSION:
            image.thumbnail((MAX_DIMENSION, MAX_DIMENSION), Image.Resampling.LANCZOS)

        out_io = io.BytesIO()
        image.save(out_io, format="JPEG", quality=85)
        optimized_bytes = out_io.getvalue()

        return image, optimized_bytes, "image/jpeg"
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Corrupted or invalid image file: {str(e)}"
        )

