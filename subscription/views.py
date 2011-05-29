def subscribe(request):
	if request.method == 'POST':
		form = SubscriptionForm(request.POST)
		if form.is_valid():
			subscription = form.save()
			return HttpResponseRedirect(reverse('subscription:success', args=[subscription.pk]))
	else:
		form = SubscriptionForm()

	context = RequestContext(request, {'form': form})
	return render_to_response('subscription/new.html', context)
