import cloudinary
import cloudinary.uploader
import cloudinary.api
from dotenv import load_dotenv
import os

load_dotenv()

def configure_cloudinary():
    """Configure Cloudinary with credentials from .env"""
    cloudinary.config(
        cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
        api_key=os.getenv('CLOUDINARY_API_KEY'),
        api_secret=os.getenv('CLOUDINARY_API_SECRET'),
        secure=True
    )
    print("✅ Cloudinary configured successfully")

def upload_to_cloudinary(file_path, folder=None):
    """
    Upload file to Cloudinary
    
    Args:
        file_path (str): Path to the file to upload
        folder (str): Optional folder name in Cloudinary
    
    Returns:
        dict: Upload result with URL and public_id
    """
    try:
        # Get folder from .env or use default
        upload_folder = folder or os.getenv('CLOUDINARY_UPLOAD_FOLDER', 'pest_detection')
        
        upload_result = cloudinary.uploader.upload(
            file_path,
            folder=upload_folder,
            resource_type="auto"  # auto-detect image/video
        )
        
        return {
            'success': True,
            'url': upload_result.get('secure_url'),
            'public_id': upload_result.get('public_id'),
            'format': upload_result.get('format'),
            'width': upload_result.get('width'),
            'height': upload_result.get('height'),
            'resource_type': upload_result.get('resource_type')
        }
        
    except Exception as e:
        print(f"Cloudinary upload error: {str(e)}")
        return {
            'success': False,
            'error': str(e)
        }

def delete_from_cloudinary(public_id):
    """Delete file from Cloudinary"""
    try:
        result = cloudinary.uploader.destroy(public_id)
        return result.get('result') == 'ok'
    except Exception as e:
        print(f"Cloudinary delete error: {str(e)}")
        return False