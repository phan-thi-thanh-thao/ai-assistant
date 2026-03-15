from typing import List, Dict, Any
from src.database.connection import supabase_conn
from src.database.database import DatabaseCRUD

print("=" * 60)
print("TEST CONNECTION VÀ 3 LỆNH GET")
print("=" * 60)

# Test connection
print("\n1. TEST CONNECTION:")
try:
    is_connected = supabase_conn.test_connection()
    print(f"   ✓ Kết nối: {'Thành công' if is_connected else 'Thất bại'}")
except Exception as e:
    print(f"   ✗ Lỗi: {e}")

# Khởi tạo DatabaseCRUD
db = DatabaseCRUD()

# GET 1: Lấy dữ liệu từ bảng health
print("\n2. GET - Lấy dữ liệu từ bảng health:")
try:
    health_data = db.get_table_data("health", limit=5)
    print(f"   ✓ Lấy được {len(health_data)} records")
    if health_data:
        print(f"   Columns: {list(health_data[0].keys())}")
        print(f"   Ví dụ: {health_data[0]}")
except Exception as e:
    print(f"   ✗ Lỗi: {e}")

# GET 2: Lấy dữ liệu từ bảng exercises
print("\n3. GET - Lấy dữ liệu từ bảng exercises:")
try:
    exercises_data = db.get_table_data("exercises", limit=5)
    print(f"   ✓ Lấy được {len(exercises_data)} records")
    if exercises_data:
        print(f"   Columns: {list(exercises_data[0].keys())}")
        print(f"   Ví dụ: {exercises_data[0]}")
except Exception as e:
    print(f"   ✗ Lỗi: {e}")

# GET 3: Lấy 1 record theo ID từ bảng health
print("\n4. GET - Lấy record theo ID từ bảng health:")
try:
    health_record = db.get_by_id("health", 1)
    if health_record:
        print(f"   ✓ Tìm thấy record: {health_record}")
    else:
        print(f"   ⚠ Không tìm thấy record với id=1")
except Exception as e:
    print(f"   ✗ Lỗi: {e}")

print("\n" + "=" * 60)
print("HOÀN THÀNH!")
print("=" * 60)
