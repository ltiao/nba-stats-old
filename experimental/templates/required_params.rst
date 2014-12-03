{% for resource in resources %}
{{ '"' * resource.url|length }}
{{ resource.url }}
{{ '"' * resource.url|length }}

Required Parameters:

{% for param in resource.params -%}
* {{ param }}
{% endfor %}
{%- endfor %}