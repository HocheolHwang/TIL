def detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)

    comment_form = CommentForm()

    count_a = question.comment_set.filter(pick=False).count()
    count_b = question.comment_set.filter(pick=True).count()
    total_count = count_a + count_b

    per_a = 0
    per_b = 0

    # 0으로 나누는 것 방지
    if total_count > 0:
        per_a = round(count_a / total_count * 100, 1)
        per_b = round(count_b / total_count * 100, 1)

    # 최근에 작성한 댓글 순서로 나타냄
    comments = question.comment_set.order_by('-created_at')
    context = {
        'question': question,
        'comment_form': comment_form,
        'count_a': count_a,
        'count_b': count_b,
        'per_a': per_a,
        'per_b': per_b,
        'comments': comments,
    }
    return render(request, 'eithers/detail.html', context)
