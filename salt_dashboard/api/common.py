def my_page(request,paging_len):
    current_page = int(request.GET.get("page",0))
    page_sum = 10
    page_extra = 3
    context = {}
    if current_page < 0:
        current_page = 0
    if ((current_page+1) * page_sum) >= paging_len:
        if paging_len%page_sum:
            current_page = paging_len/page_sum
        else:
            current_page = paging_len/page_sum-1
    if (page_extra*2+1) > paging_len/page_sum:
        context["page_num"] = range(paging_len/page_sum)
    elif (current_page-page_extra) < 0:
        context["page_num"] = range(page_extra*2+1)
    elif (current_page+page_extra)*page_sum >= paging_len:
        context["page_num"] =  range((paging_len/page_sum-7),paging_len/page_sum)
    else:
        context["page_num"] = range(current_page-page_extra,current_page+page_extra)
    context["current_page"] = current_page
    context['page_tables'] = []
    return context
