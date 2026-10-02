# # # # # # посчитать по списку кодов [200, 404, 200, 500, 200, 404, 301]
# # # # # # количество успешных, клиентских и серверных ошибок.

# # # # # codes = [200, 404, 200, 500, 200, 404, 301]
# # # # # count_200 = 0
# # # # # count_300 = 0
# # # # # count_400 = 0
# # # # # count_500 = 0
# # # # # for i in codes:
# # # # #     if 200 <= i < 300:
# # # # #         count_200 += 1
# # # # #     if 300 <= i < 400:
# # # # #         count_300 += 1
# # # # #     if 400 <= i < 500:
# # # # #         count_400 += 1
# # # # #     if 500 <= i:
# # # # #         count_500 += 1
# # # # # print(count_200)
# # # # # print(count_300)
# # # # # print(count_400)
# # # # # print(count_500)


# # # # codes = [200, 404, 200, 500, 666, 34523465262562565, "qwerty", 200, 404, 301]
# # # # result = {}
# # # # for i in codes:
# # # #     if i in result:
# # # #         result[i] += 1
# # # #     else:
# # # #         result[i] = 1
# # # # for key, value in result.items():
# # # #     print(key, "встретился", value, "раз")
# # # # print(result)

# # # expected = {"id": 1, "name": "Ivan", "role": "admin"}
# # # actual = {"id": 1, "name": "Ivan Petrov"}
# # # for key, value in expected.items():
# # #     if key in actual:
# # #         if actual[key] == value:
# # #             print(key, "OK")
# # #         else:
# # #             print(key, "— ожидалось:", value, "| получено:", actual[key])
# # #     else:
# # #         print(key, "— поле отсутствует в ответе")

# # expected = {"id": 15, "status": "approved", "sample_count": 3, "lab": "Химлаб"}
# # actual = {"id": 15, "status": "in_review", "sample_count": 3, "created_by": "admin"}
# # mismatches = 0
# # for key, value in expected.items():
# #     if key in actual:
# #         if actual[key] == value:
# #             print(key, "ok")
# #             # здесь ничего не увеличиваем — всё хорошо
# #         else:
# #             print(key, "- ожидалось", value, "- фактически", actual[key])
# #             mismatches += 1        # ← 1
# #     else:
# #         print(key, "- поле отсутствует в ответе")
# #         mismatches += 1            # ← 2

# # for field in actual:
# #     if field not in expected:
# #         print(field, "лишнее поле в ответе")
# #         mismatches += 1            # ← 3

# # if mismatches == 0:
# #     print("PASSED")
# # else:
# #     print("FAILED, расхождений:", mismatches)

# # def double(num):
# #     print(double)

# # num(5)

# def double(name):
#     print(2 * name)
#     return 2 * name
# double(1)
# double(100)



# def is_ok(code):
#     return code == 403
# print(is_ok(403))
# if is_ok(403):
#     print("тест пройден")
# else:
#     print("тест упал")

# def category(code):
#     if 200 <= code <= 299:
#         return "success"
#     elif 400 <= code <= 499:
#         return "client error"
#     else:
#         return "unknown"
# print(category(1))   # success
# print(category(404))   # client error
# print(category(999))   # unknown

# def count_slow(times, sla):
#     count = 0 
#     for time in times:
#         if time > sla:
#             count += 1
#     return count
#     # посчитать, сколько времён больше sla, и вернуть это число

# print(count_slow([120, 450, 890, 230, 1500, 310], 2))   # 2
# print(count_slow([100, 200, 300], 500))                   # 0

def compare(expected, actual):
    mismatches = 0
    for key, value in expected.items():
        if key in actual:
            if actual[key] == value:
                print(key, "ok")
            else:
                print(key, "- ожидалось", value, "- фактически", actual[key])
                mismatches += 1
        else:
            print(key, "- поле отсутствует в ответе")
            mismatches += 1

    for field in actual:
        if field not in expected:
            print(field, "лишнее поле в ответе")
            mismatches += 1

    return mismatches
    
expected = {"id": 15, "status": "approved", "sample_count": 3, "lab": "Химлаб"}
actual = {"id": 15, "status": "in_review", "sample_count": 3, "created_by": "admin"}
print("Расхождений:", compare(expected, actual))


изменение нахуй 