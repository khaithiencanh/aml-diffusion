import os

# Đường dẫn tới thư mục chứa dữ liệu của bạn
data_dir = r"C:\Users\ezycloudx-admin\AML_LMU"

# Danh sách ánh xạ từ thư mục viết tắt sang tên gốc của tác giả
rename_map = {
    "BAS": "Basophil",
    "EBO": "Erythroblast",
    "EOS": "Eosinophil",
    "KSC": "Smudge cell",
    "LYA": "Atypical Lymphocyte",
    "LYT": "Typical Lymphocyte",
    "MMZ": "Metamyelocyte",
    "MOB": "Monoblast",
    "MON": "Monocyte",
    "MYB": "Myelocyte",
    "MYO": "Myeloblast",
    "NGB": "Band Neutrophil",
    "NGS": "Segmented Neutrophil",
    "PMB": "Promyelocyte Bilobed",
    "PMO": "Promyelocyte"
}

print("Bắt đầu đổi tên thư mục...")

for old_name, new_name in rename_map.items():
    old_path = os.path.join(data_dir, old_name)
    new_path = os.path.join(data_dir, new_name)
    
    # Kiểm tra nếu thư mục cũ tồn tại thì tiến hành đổi tên
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"✅ Đã đổi tên: {old_name} -> {new_name}")
    elif os.path.exists(new_path):
        print(f"⚠️ Thư mục {new_name} đã tồn tại, bỏ qua.")
    else:
        print(f"❌ Không tìm thấy thư mục {old_name}.")
        
print("Hoàn tất!")