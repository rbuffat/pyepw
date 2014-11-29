class {{ class_name }}(object):
    """ Corresponds to EPW IDD object `{{ internal_name }}`
    """
    _internal_name = "{{ internal_name }}"
    field_count = {{ field_count}}

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `{{ internal_name }}`
        """
    {%- for field in fields %}
    {%- if field.is_list %}
        self._{{field.field_name}}s = []
    {%- else %}
        self._{{field.field_name}} = None
    {%- endif %}
    {%- endfor %}

    def read(self, vals):
        """ Read values
    
        Args:
            vals (list): list of strings representing values
        """
        i = 0
        {%- for field in fields %}
        {%- if field.is_list %}
        count = int(vals[i])
        i += 1
        for _ in range(count):
            obj = {{field.object_name}}()
            obj.read(vals[i:i + obj.field_count])
            self.add_{{field.field_name}}(obj)
            i += obj.field_count
        {%- else %}
        if len(vals[i]) == 0:
            self.{{field.field_name}} = None
        else:
            self.{{field.field_name}} = vals[i]
        i += 1
        {%- endif %}
        {%- endfor %}

    {%- for field in fields %}
    {%- if field.is_list %}

    @property
    def {{field.field_name}}s(self):
        """Get {{field.field_name}}s

        Returns:
            A list of {{ field.object_name }} objects
        """
        return self._{{field.field_name}}s

    def add_{{field.field_name}}(self, value):
        """Add {{field.field_name}}

        Args:
            {{ field.object_name }}: new value to add to `{{field.field_name}}s`
        """
        self._{{field.field_name}}s.append(value)
    {%- else %}

    @property
    def {{field.field_name}}(self):
        """Get {{ field.field_name }}

        Returns:
            {{ field.attributes.pytype }}: the value of `{{field.field_name}}` or None if not set
        """
        return self._{{field.field_name}}

    @{{field.field_name}}.setter
    def {{field.field_name}}(self, value={%if field.attributes.default and not (field.attributes.type=="alpha" or field.attributes.type=="choice") %}{{field.attributes.default}} {% elif field.attributes.default and (field.attributes.type=="alpha" or field.attributes.type=="choice") %}"{{field.attributes.default}}"{%elif not field.attributes.default and field.attributes.missing  %}{{field.attributes.missing}}{% else %}None{% endif %}):
        """  Corresponds to IDD Field `{{field.field_name}}`

        {%- for comment in field.attributes.note %}
        {{comment}}
        {%- endfor %}

        Args:
            value ({{ field.attributes.pytype }}): value for IDD Field `{{field.field_name}}`
                {%- if field.attributes.type == "choice" %}
                Accepted values are:
                    {%- for k in field.attributes.key %}
                      - {{ k }}
                    {%- endfor %}
                    {%- endif %}
                {%- if field.attributes.units %}
                Unit: {{ field.attributes.units }}
                {%- endif %}
                {%- if field.attributes.default %}
                Default value: {{ field.attributes.default }}
                {%- endif %}
                {%- if field.attributes.minimum %}
                value >= {{ field.attributes.minimum }}
                {%- endif %}
                {%- if field.attributes['minimum>'] %}
                value > {{ field.attributes['minimum>'] }}
                {%- endif %}
                {%- if field.attributes.maximum %}
                value <= {{ field.attributes.maximum }}
                {%- endif %}
                {%- if field.attributes['maximum<'] %}
                value < {{ field.attributes['maximum<'] }}
                {%- endif %}
                {%- if field.attributes.missing %}
                Missing value: {{ field.attributes.missing }}
                {%- endif %}
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        {%- if field.attributes|length > 0  %}
        if value is not None:
        {%- endif %}
            try:
                value = {{ field.attributes.pytype }}(value)
            except:
                raise ValueError('value {} need to be of type {{ field.attributes.pytype }} '
                                 'for field `{{field.field_name}}`'.format(value))
            {%- if field.attributes.pytype == "str" %}
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes.minimum %}
            if value < {{ field.attributes.minimum }}:
                raise ValueError('value need to be greater or equal {{ field.attributes.minimum }} '
                                 'for field `{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes['minimum>'] %}
            if value <= {{ field.attributes['minimum>'] }}:
                raise ValueError('value need to be greater {{ field.attributes["minimum>"] }} '
                                 'for field `{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes.maximum %}
            if value > {{ field.attributes.maximum }}:
                raise ValueError('value need to be smaller {{ field.attributes.maximum }} '
                                 'for field `{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes['maximum<'] %}
            if value >= {{ field.attributes['maximum<'] }}:
                raise ValueError('value need to be smaller {{ field.attributes["maximum<"] }} '
                                 'for field `{{field.field_name}}`')
            {%- endif %}
            {%- if field.attributes.type == "choice" %}
            vals = set()
            {%- for k in field.attributes.key %}
            vals.add("{{k}}")
            {%- endfor %}
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `{{field.field_name}}`'.format(value))
            {%- endif %}

        self._{{field.field_name}} = value
    {%- endif %}
    {%- endfor %}

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string
    
        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self, top=True):
        """ Exports object to its string representation
    
        Args:
            top (bool):  if True appends `internal_name` before values.
                All non list objects should be exported with value top=True,
                all list objects, that are embedded in as fields inlist objects
                should be exported with `top`=False
    
        Returns:
            str: The objects string representation
        """
        out = []
        if top:
            out.append(self._internal_name)
        {%- for field in fields %}
        {%- if field.is_list %}
        out.append(str(len(self.{{field.field_name}}s)))
        for obj in self.{{field.field_name}}s:
            out.append(obj.export(top=False))
        {%- else %}
        out.append(self._to_str(self.{{field.field_name}}))
        {%- endif %}
        {%- endfor %}
        return ",".join(out)

    def __str__(self):
        return self.export(True)
