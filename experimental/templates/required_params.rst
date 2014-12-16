{% for resource in resources %}
{{ '"' * resource.url|length }}
{{ resource.url }}
{{ '"' * resource.url|length }}

Required Parameters:
{% for param in resource.params %}
* {{ param }}
{%- endfor %}

Results:
{% for result in resource.results %}
* {{ result.name }}
{% for header in result.headers %}
  * {{ header }}
{%- endfor %}
{% endfor %}
{%- endfor %}
