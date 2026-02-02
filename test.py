import pandas as pd
import glob2
import scipy
import cv2

# 验证 pandas
df = pd.DataFrame({
    "img_path": ["./test1.jpg", "./test2.jpg"],
    "label": ["cat", "dog"]
})
print("✅ pandas 正常运行，表格数据创建成功")

# 验证 glob2
test_files = glob2.glob("*.jpg")  # 匹配当前目录下所有 jpg 图片
print(f"✅ glob2 正常运行，批量文件匹配完成（找到 {len(test_files)} 张 jpg 图片）")

# 验证 scipy
print(f"✅ scipy 正常运行，版本：{scipy.__version__}")

# 额外补充：验证 cv2（OpenCV），让校验更完整
print(f"✅ OpenCV 正常运行，版本：{cv2.__version__}")