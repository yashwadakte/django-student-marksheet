# from django.shortcuts import render

# def even_odd(request):
#     result = ""

#     if request.method == "POST":
#         num = int(request.POST.get("number"))

#         if num % 2 == 0:
#             result = "Even Number"
#         else:
#             result = "Odd Number"

#     return render(request, "even_odd.html", {"result": result})

from django.shortcuts import render

def marksheet(request):
    data = {}

    if request.method == "POST":
        name = request.POST.get("name")

        m1 = int(request.POST.get("m1"))
        m2 = int(request.POST.get("m2"))
        m3 = int(request.POST.get("m3"))
        m4 = int(request.POST.get("m4"))
        m5 = int(request.POST.get("m5"))

        total = m1 + m2 + m3 + m4 + m5
        percentage = total / 5

        if percentage >= 80:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "Fail"

        data = {
            "name": name,
            "total": total,
            "percentage": percentage,
            "grade": grade
        }

    return render(request, "marksheet.html", data)