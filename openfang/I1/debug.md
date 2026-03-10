Trong code mẫu ban đầu có dòng :from src.spikes.deps import Deps, User, agent, chat, create_deps. 
Khi chạy nó sẽ báo lỗi ModuleNotFoundError: No module named 'src.spikes' vì trong repo openfang không có thư mục src/spikes

Cách fig: xóa dòng đó và viết lại agent + tool trực tiếp trong file: agent_basic.py và vào cmd chạy: cd Tim-hieu-va-Trien-khai-OpenFang\openfang -> cd I1 chạy python agent_basic.py thì ra kết quả.