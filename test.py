# H, M = map(int, input().split())

# # 엠이 45이상일때는 엠 - 45
# # 엠이 45미만일때는 
# #     H = 0 h는 23이다
# #     H-1 엠+15


# if M >= 45:
#     print(H,M-45)
# elif M < 45:
#     if H == 0 :
#         print(23, M+15)
#     else :
#         print(H-1, M+15)

# H, M = map(int, input().split())

# if M > 44:
#     print(H, M-45)
# elif M < 45:
#     if H == 0:
#         print(23, M+15)
#     else:
#         print(H-1, M+15)

H, M = map(int, input().split())
N = int(input())

if M + N <= 60:
    print(H+1, M+N)
elif M + N > 60:
    print(H+(M+N)//60,((M+N)//60)(M+N))

   
