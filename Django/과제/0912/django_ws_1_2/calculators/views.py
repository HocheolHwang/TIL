from django.shortcuts import render

# Create your views here.
def calculation(request):
	return render(request, 'calculators/calculation.html')


def result(request):
	first_num = request.GET.get('first_num')
	second_num = request.GET.get('second_num')
	context = {
		'first_num': first_num,
		'second_num': second_num,
		'mul_nums': int(first_num) * int(second_num),
		'sub_nums': int(first_num) - int(second_num),
		'div_nums': int(first_num) / int(second_num) if int(second_num) != 0 else None,
	}
	return render(request, 'calculators/result.html', context)