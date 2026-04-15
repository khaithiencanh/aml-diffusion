import os
import shutil

# Bạn sửa 2 đường dẫn này cho đúng với máy của bạn
thu_muc_cu = "đường_dẫn_tới/basophil_1800_old" 
thu_muc_moi = "đường_dẫn_tới/basophil"

# Lấy danh sách 1.000 ảnh mới sinh ra
anh_moi = [f for f in os.listdir(thu_muc_moi) if f.endswith(".png")]
so_luong_anh_cu = len([f for f in os.listdir(thu_muc_cu) if f.endswith(".png")]) 

for file_name in anh_moi:
    # Cắt lấy số thứ tự của ảnh mới (ví dụ lấy "0" từ "0.png")
    so_cu = int(file_name.split('.')[0])
    
    # Cộng dồn số thứ tự này với số lượng ảnh cũ để tạo tên nối tiếp (ví dụ: 0 + 1800 = 1800.png)
    ten_moi = f"{so_cu + so_luong_anh_cu}.png"
    
    duong_dan_cu = os.path.join(thu_muc_moi, file_name)
    duong_dan_moi = os.path.join(thu_muc_cu, ten_moi)
    
    # Đổi tên và chuyển luôn file sang nhà cũ
    shutil.move(duong_dan_cu, duong_dan_moi)

print(f"Đã gộp và nối tiếp an toàn {len(anh_moi)} ảnh!")