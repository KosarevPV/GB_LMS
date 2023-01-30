from django.contrib import admin


class PublishedYearFilter(admin.SimpleListFilter):
    title = "published year"
    parameter_name = "published_date"
    template = "admin_input_filter.html"

    def lookups(self, request, model_admin):
        return ((None, None),)

    def choices(self, changelist):
        query_params = changelist.get_filters_params()
        query_params.pop(self.parameter_name, None)
        all_choice = next(super().choices(changelist))
        all_choice["query_params"] = query_params
        yield all_choice

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(published_date__year=value)
