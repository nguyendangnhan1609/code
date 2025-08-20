# chưa biết bài này có phải là bài giải của bài familiar hay không ??? 
n,k=map(int,input().split())
a=list(map(int, input().split()))
a.sort()
a=[0]+a
def check(x):
    global value
    tong=0
    for i in range(1,x+1): tong+=a[i]
    s=x*a[x]; 
    if (s-tong<=k):
        value = a[x]
        return True
    for i in range(x+1,n+1):
        tong=tong-a[i-x]+a[i]
        s=x*a[i]
        if (s-tong<=k):
            value=a[i]
            return True
    return False
l=1; r=n;
while (l<=r):
    mid=(l+r)//2
    if check(mid):
        res=mid
        l=mid+1
    else: r=mid-1
print(res, value)

# IN1: 
# 5
# 15
# 14
# 15
# 12
# 14
# OUT1: 4

# ############################

# IN2: 
# 3
# 8
# 10
# 9

# OUT 2:
#     3




# GƯƠNG MẶT THÂN QUEN Tên file: familiar.cpp
# "Gương mặt thân quen" là một chương trình giải trí khá nổi tiếng trên VTV3. Trong chương
# trình này, mỗi thí sinh sẽ bắt chước giọng hát của một ca sỹ nổi tiếng nào đó và trên cơ sở đó
# bạn giám khảo sẽ cho điểm từng thí sinh.
# Có tất cả N thí sinh tham gia thi. Cuộc thi được diễn ra trong nhiều vòng thi khác nhau. Mỗi
# vòng thi, thí sinh tốt nhất sẽ được N điểm, thí sinh tốt thứ nhì được N-1 điểm, thí sinh tốt thứ
# ba được N-2 điểm, ..., thí sinh tốt thứ N được 1 điểm. Điểm của mỗi vòng thi của từng thí sinh
# được cộng lại, sau vòng thi cuối cùng thí sinh nào được nhiều điểm nhất sẽ giành chức vô
# địch. Tất nhiên, nếu có nhiều thí sinh cùng đạt nhiều điểm nhất thì tất cả họ đều giành chức vô
# địch.
# Chỉ còn một vòng thi nữa là cuộc thi kết thúc. Hiện tại điểm tổng của các thí sinh là
# 1 2 , ,..., N
# a a a
# . Hỏi rằng có bao nhiêu thí sinh có quyền hy vọng rằng mình sẽ đạt chức vô địch
# sau vòng thi cuối cùng?
# Bài tập tìm kiếm nhị phân
# Input: familiar.inp
#  Dòng đầu tiên chứa số nguyên N (
# 5
# 3 3.10   N
# ) là số lượng thí sinh tham gia thi
#  N dòng tiếp theo, mỗi dòng ghi một số nguyên ai (
# 6
# 0 2.10 i   a
# ) là số điểm của các thí
# sinh trước vòng thi cuối cùng
# Output: familiar.inp
#  Một số nguyên duy nhất là số lượng thí sinh có thể đạt được chức vô địch sau vòng thi
# cuối cùng
# Example:
# familiar.inp familiar.out
# 5
# 15
# 14
# 15
# 12
# 14
# 4
# 3
# 8
# 10
# 9
