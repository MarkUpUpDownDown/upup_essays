import os
import datetime

import frontmatter

from markupupdowndown.config import load_main_config, resolve_path
from markupupdowndown.generators import find_skel_dir, render_skel_dir

__version__ = "0.1"


def _file_metadata(file_abspath):
    with open(file_abspath) as input_fd:
        slug_name = os.path.basename(os.path.dirname(file_abspath))
        metadata, content = frontmatter.parse(input_fd.read())

        title = metadata['title']
        published_at = metadata['published_at']

        return (title, slug_name, published_at)


def _get_essays_metadata(essays_dir):
    essays_metadata = dict()

    for root, dirs, files in os.walk(essays_dir):
        if root == essays_dir:
            continue

        for file in files:
            file_abspath = os.path.join(root, file)
            if file.endswith('.md'):
                (title, slug_name, published_at) = _file_metadata(file_abspath)

                published_dt = datetime.datetime.strptime(
                    published_at, '%B %d, %Y %I:%M %p'
                )
                essays_metadata[published_dt] = (title, slug_name, published_at)

    return essays_metadata


def render(config, metadata, essays_dir):
    essays_metadata = _get_essays_metadata(essays_dir)

    essays_list = list()
    for key in reversed(sorted(essays_metadata)):
        title, slug_name, published_at = essays_metadata[key]
        essay_item = {
            'title': title,
            'date': published_at,
            'slug': slug_name
        }
        essays_list.append(essay_item)

    essays_context = {'essays_list': essays_list}

    return essays_context


def render_essays_skel(args):
    config = load_main_config()
    theme_dir = resolve_path(config, config['theme_dir'])
    essays_skel_dir = find_skel_dir(__file__, skel_type='theme')
    context = {}
    render_skel_dir(essays_skel_dir, theme_dir, context)


def cmd_new(subparsers):
    help_msg = 'add essays skeleton data to project'
    parser_new_essays = subparsers.add_parser('essays', help=help_msg)
    parser_new_essays.set_defaults(func=render_essays_skel)

    return parser_new_essays


def essays(args):
    print("essays()")


def cmd_essays(subparsers):
    help_msg = 'does nothing!'
    parser_essays = subparsers.add_parser('essays', help=help_msg)
    parser_essays.set_defaults(func=essays)
    return parser_essays
