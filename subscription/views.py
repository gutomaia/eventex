def new(request):
	form = SubscriptionForm()
	context = RequestContext(request, {'form': form})
	return render_to_response('subscription/new.html', context)


def create(request):
	form = SubscriptionForm(request.POST)
	if not valid():
		context = RequestContext(request, {'form': form})
		return render_to_response('subscription/new.html', context)

	subscription = form.save()
	return HttpResponseRedirect(reverse('subscription:success', args=[subscription.pk]))


def subscribe(request):
	if request.method == 'POST':
		return create(request)
	else:
		return new(request)
