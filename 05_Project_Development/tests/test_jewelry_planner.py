import io
from PIL import Image

def test_generate_jewelry_text_only(client):
    """TC-14: Generate jewelry recommendation (text only)."""
    form_data = {
        "budget": 350.0,
        "occasion": "Summer Wedding",
        "style_preference": "Delicate Yellow Gold & Pearls"
    }
    response = client.post("/generate-jewelry", data=form_data)
    assert response.status_code == 200
    data = response.json()
    assert data["budget"] == 350.0
    assert data["total_estimated_cost"] <= 350.0
    assert len(data["items"]) > 0
    assert "recommended_metal" in data

def test_generate_jewelry_with_image(client):
    """TC-15: Generate jewelry with uploaded outfit image."""
    # Create sample in-memory image
    img = Image.new("RGB", (64, 64), color=(0, 100, 50))
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="JPEG")
    img_bytes = img_byte_arr.getvalue()

    form_data = {
        "budget": 450.0,
        "occasion": "Emerald Gala",
        "style_preference": "Royal Emerald & Gold"
    }
    files = {
        "image": ("outfit.jpg", img_bytes, "image/jpeg")
    }
    response = client.post("/generate-jewelry", data=form_data, files=files)
    assert response.status_code == 200
    data = response.json()
    assert data["budget"] == 450.0
    assert data["total_estimated_cost"] <= 450.0
    assert data["vision_analysis"]["image_processed"] is True

def test_generate_jewelry_invalid_image_type(client):
    """TC-16: Reject unsupported file upload."""
    form_data = {
        "budget": 200.0,
        "occasion": "Casual Dinner",
        "style_preference": "Silver"
    }
    files = {
        "image": ("malicious.exe", b"fake binary payload", "application/octet-stream")
    }
    response = client.post("/generate-jewelry", data=form_data, files=files)
    assert response.status_code == 400
    assert "Unsupported image type" in response.json()["detail"]

