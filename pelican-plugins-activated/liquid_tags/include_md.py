"""
Include markdown file tag
----------------
This implements a Liquid-style video tag for Pelican,
based on the code tag_.
Syntax
------
{% include_md path/to/md %}

The "path to code" is specified relative to the ``othermd`` subdirectory of
the content directory  Optionally, this subdirectory can be specified in the
config file:

    MD_DIR = 'code'

Example
-------
{% include_md myfile.md %}

This will import myfile.md from content/othermd/myfile.md
and output the contents directly inside the present md file

"""
import re
import os
from .mdx_liquid_tags import LiquidTags


SYNTAX = "{% include_md /path/to/file.md %}"
FORMAT = re.compile(r"""^(?:\s+)?(?P<src>\S+)?$""")


@LiquidTags.register('include_md')
def include_md(preprocessor, tag, markup):
    title = None
    lang = None
    src = None

    match = FORMAT.search(markup)
    if match:
        argdict = match.groupdict()
        src = argdict['src']

    if not src:
        raise ValueError("Error processing input, "
                         "expected syntax: {0}".format(SYNTAX))

    settings = preprocessor.configs.config['settings']
    code_dir = settings.get('MD_DIR', 'othermd')
    code_path = os.path.join('content', code_dir, src)

    if not os.path.exists(code_path):
        raise ValueError("File {0} could not be found".format(code_path))

    code = open(code_path).read()

    source = code

    return source


#----------------------------------------------------------------------
# This import allows image tag to be a Pelican plugin
from liquid_tags import register
