s = input() #BBBSSC
s = s.replace('\n','');
nb,ns,nc = map(int,input().split())
pb,ps,pc = map(int,input().split())
m = int(input())
banh_mi = xuc_xich = pho_mat = 0;
for x in s:
    if (x == 'B'): banh_mi += 1;
    if (x == 'S'): xuc_xich += 1;
    if (x == 'C'): pho_mat += 1;
    
# def check(x):
#     so_banh_mi = x * banh_mi;
#     so_xuc_xich = x * xuc_xich;
#     so_pho_mat = x * pho_mat;
#     if (so_banh_mi <= nb): so_banh_mi = 0;
#     else: so_banh_mi -= nb;
#     if (so_xuc_xich <= ns): so_xuc_xich = 0;
#     else: so_xuc_xich -= ns;
#     if (so_pho_mat <= nc): so_pho_mat = 0;
#     else: so_pho_mat -= nc;
#     so_tien = so_banh_mi * pb + so_xuc_xich * ps + so_pho_mat * pc;
#     return so_tien <= m;

def check(x):
    """
    Hàm này kiểm tra xem có đủ nguyên liệu và tiền để làm x chiếc bánh hamburger hay không.

    Tham số:
    - x: số lượng bánh hamburger cần kiểm tra.
    
    Trả về:
    - True nếu có thể làm được x chiếc bánh.
    - False nếu không đủ tiền hoặc nguyên liệu.
    """
    
    # 1. Tính toán số lượng nguyên liệu cần thiết để làm x chiếc bánh
    so_banh_mi_can = x * banh_mi
    so_xuc_xich_can = x * xuc_xich
    so_pho_mat_can = x * pho_mat
    
    # 2. Tính toán số lượng nguyên liệu cần mua thêm từ cửa hàng
    # Nếu số lượng cần ít hơn hoặc bằng số lượng có sẵn, ta không cần mua thêm.
    so_banh_mi_mua = max(0, so_banh_mi_can - nb)
    so_xuc_xich_mua = max(0, so_xuc_xich_can - ns)
    so_pho_mat_mua = max(0, so_pho_mat_can - nc)

    # 3. Tính tổng chi phí mua thêm nguyên liệu
    tong_chi_phi = (so_banh_mi_mua * pb) + \
                   (so_xuc_xich_mua * ps) + \
                   (so_pho_mat_mua * pc)
                   
    # 4. So sánh tổng chi phí với số tiền hiện có (m)
    # Trả về True nếu chi phí <= số tiền hiện có, ngược lại là False.
    return tong_chi_phi <= m
    
l = 0; r = m + nb + ns + nc;
while (l<=r):
    mid = (l+r)//2;
    if (check(mid)):
        kq = mid;
        l = mid + 1;
    else:
        r = mid - 1;
print(kq)