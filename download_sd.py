from modelscope import snapshot_download

print("Bắt đầu tải SD 2.1 (Tự động lọc bỏ các định dạng nặng không cần thiết)...")

# Hàm này sẽ tải model nhưng bỏ qua toàn bộ file .bin, .ckpt, .pt để tiết kiệm hàng chục GB
model_dir = snapshot_download(
    'AI-ModelScope/stable-diffusion-2-1',
    ignore_file_pattern=['*.bin', '*.ckpt', '*.pt', '*.msgpack']
)

print(f"\n✅ Tải hoàn tất! Đường dẫn thư mục model của bạn là:\n{model_dir}")